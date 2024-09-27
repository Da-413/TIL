from django.shortcuts import render
from .models import Weather

import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
from datetime import datetime

from io import BytesIO
import base64

plt.switch_backend('Agg')

csv_path = 'weathers/data/austin_weather.csv'
df = pd.read_csv(csv_path)

# Create your views here.
def index(request):
    return render(request, 'weathers/index.html')

def problem1(request):
    html_table = df.to_html(classes='table table-striped', index=False)

    context = {
        'html_table': html_table
    }
    return render(request, 'weathers/problem1.html', context)

def problem2(request):
    df['Date'] = pd.to_datetime(df['Date'])
    plt.figure(figsize=(10,6))

    plt.plot(df['Date'], df['TempHighF'], label='High Temperature(°F)')
    plt.plot(df['Date'], df['TempAvgF'], label='Average Temperature(°F)')
    plt.plot(df['Date'], df['TempLowF'], label='Low Temperature(°F)')

    plt.xlabel('Date')
    plt.ylabel('Temperature(°F)')
    plt.title('Temperature Variation')
    plt.legend()
    plt.grid(True)

    buffer = BytesIO()

    plt.savefig(buffer, format='png')
    
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    context = {
        'image_base64': image_base64
    }

    return render(request, 'weathers/problem2.html', context)

def problem3(request):
    df['Date'] = pd.to_datetime(df['Date'])
    # new_df = df.groupby()
    plt.figure(figsize=(10,6))

    monthly_df = df.groupby(pd.Grouper(key='Date', freq='M')).agg({
        'TempHighF': 'mean',
        'TempAvgF': 'mean',
        'TempLowF': 'mean'
    })

    plt.plot(monthly_df.index, monthly_df['TempHighF'], label='High Temperature(°F)')
    plt.plot(monthly_df.index, monthly_df['TempAvgF'], label='Average Temperature(°F)')
    plt.plot(monthly_df.index, monthly_df['TempLowF'], label='Low Temperature(°F)')

    plt.xlabel('Month')
    plt.ylabel('Temperature(°F)')
    plt.title('Temperature Variation')
    plt.legend()
    plt.grid(True)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')  
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    context = {
        'image_base64': image_base64
    }

    return render(request, 'weathers/problem3.html', context)

def problem4(request):
    df['Events'] = df['Events'].fillna('')
    events = df.loc[:,'Events'].to_list()

    new_events = []
    for items in events:
        if ',' in items:
            items = list(map(str.strip, items.split(',')))
            new_events.extend(items)
        elif items == ' ':
            new_events.append('No_Event')
        else:
            new_events.append(items)

    event_counts = Counter(new_events)
    event_count_df = pd.DataFrame(event_counts.items(), columns=['Event', 'Count']).sort_values(by='Count', ascending=False)

    plt.figure(figsize = (10, 6))
    plt.bar(event_count_df['Event'], event_count_df['Count'])

    plt.xlabel('Events')
    plt.ylabel('count')
    plt.title('Event Counts')
    plt.grid(True)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')  
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    context = {
        'image_base64': image_base64
    }
    return render(request, 'weathers/problem4.html', context)

def problem5(request):
    df['Date'] = pd.to_datetime(df['Date'])
    if request.method == 'POST':
        # 사용자가 입력한 시작 날짜와 종료 날짜를 받음
        start_date_str = request.POST.get('start_date')
        end_date_str = request.POST.get('end_date')
        
        # 문자열을 datetime 객체로 변환
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
        
        # 입력된 기간 동안의 데이터를 필터링
        filtered_data = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
        
        # 데이터가 존재하는지 확인
        if filtered_data.empty:
            best_day_message = "해당 기간 동안의 데이터가 없습니다."
        else:
            # 적당한 기온과 강수량이 없는 날을 기준으로 선택 (예: 온도 범위와 비가 없는 날)
            ideal_days = filtered_data[
                (filtered_data['TempHighF'] >= 60) & (filtered_data['TempHighF'] <= 80) & 
                (filtered_data['PrecipitationSumInches'] == 0)
            ]
            
            if ideal_days.empty:
                best_day_message = "해당 기간에는 가족 여행에 적합한 날이 없습니다."
            else:
                # 가장 적합한 날 찾기 (날짜가 가장 가까운 날을 선택)
                best_day = ideal_days.iloc[0]['Date']
                best_day_message = f"가족 여행에 가장 좋은 날은 {best_day.date()}입니다!"

        # 결과를 context로 템플릿에 전달
        context = {
            'best_day_message': best_day_message,
            'start_date': start_date_str,
            'end_date': end_date_str
        }

        return render(request, 'weathers/problem5.html', context)

    return render(request, 'weathers/problem5.html')