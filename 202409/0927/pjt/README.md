# PJT 0n

### 오늘 pjt 를 통해 배운 내용

* Django를 이용해 csv 파일을 시각화 할 수 있다.

* 생성형 AI를 이용해 추천 서비스를 만들 수 있다.


## A. 데이터 읽어오기

* 주요 요구 사항 : csv 파일을 웹으로 출력한다

* 결과
  
  * 데이터베이스를 만들어서 송출할 필요는 없다.
  
    ```python
    def problem1(request):
    html_table = df.to_html(classes='table table-striped', index=False)

    context = {
        'html_table': html_table
    }
    return render(request, 'weathers/problem1.html', context)
    ```

  * database를 제작하려다가 포기하고 바로 웹 페이지로 출력했다.
  
-----

## B. 일 별 최고, 최저, 평균 기온 출력

* 주요 요구 사항 : 일별 기온 변화를 그래프로 출력한다.

* 결과
  
  * plt에서 데이터를 겹쳐 그려 그래프를 출력한다.
  
    ```python
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
    ```

  * 한글로 제목이나 변수명을 송출하면 인코딩 오류가 나서 영어로 대체했다.
  
-----

## C. 월별 기온 변화 출력

* 주요 요구 사항 : 월별 기온 변화를 그래프로 출력한다.

* 결과
  
  * B 문제와 같지만 월별 기온 통계를 구해야 한다.
  
    ```python
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
    ```

  * groupby 함수를 이용해 월별 기온 추이를 그래프로 출력한다.


## D. EVENTS count 출력

* 주요 요구 사항 : event 열의 변수들의 개수를 세어 히스토그램을 출력한다

* 결과
  
  * 결측치는 no event로 출력하고 중복 event는 따로 처리한다.
  
    ```python
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
    ```

  * fillna('No_Event')에서 fillna(' ') / if string == ' ':  coutn += 1  로 수정해 해결했다.
  
  -----

## E. 가족 여행 추천 서비스

* 주요 요구 사항 : 생성형 AI를 이용해 가족 여행 추천 서비스를 제작한다.

* 결과
  
  * 생성형 AI를 이용해 서비스를 제작했다.
  
    ```python
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
    ```

  * request.method == 'POST' 인 경우만 제작하므로 다른 요청이 왔을 경우에도 render하는 경로가 필요하다. 이 때 context는 포함하지 않는다.



# 오늘 후기

* 데이터베이스를 제작하지 않고 프로젝트를 진행했다.

* 생성형 AI를 활용해서 도움을 받았다.

* 데이터 사이언스를 장고를 이용해 웹페이지에 구현한 경험이 처음인데 미래에 도움이 되는 경험일 것 같다. 



### 참고 사이트

* [챗 지피티](https://chatgpt.com/)

