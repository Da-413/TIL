import requests

def recommend_best_savings_product(api_key):
    url = 'https://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params = {
        'auth': api_key,
        'topFinGrpNo': '020000',  # 예시로 사용된 그룹 번호, 실제로 사용할 그룹 번호로 변경해야 합니다.
        'pageNo': 1
    }

    try:
        # API 요청 보내기
        response = requests.get(url, params=params)
        
        # 응답 데이터 확인
        if response.status_code == 200:
            data = response.json()
            
            # 결과에서 저축 기간이 가장 짧고 금리가 가장 높은 상품 찾기
            best_product = None
            shortest_period = float('inf')  # 초기화: 무한대 값으로 설정
            highest_interest_rate = 0.0     # 초기화: 0으로 설정
            
            for product in data['result']['optionList']:
                print(product)
                deposit_period = int(product['save_trm'])  # 기간 정보 가져오기
                interest_rate = float(product['intr_rate'])  # 금리 정보 가져오기
                
                # 현재까지의 최적 상품보다 기간이 짧거나 금리가 높으면 업데이트
                if deposit_period < shortest_period or (deposit_period == shortest_period and interest_rate > highest_interest_rate):
                    shortest_period = deposit_period
                    highest_interest_rate = interest_rate
                    best_product = product
            
            return best_product
        
        else:
            print(f"Failed to retrieve data: {response.status_code}")
            return None
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# 실제 API 키를 사용하여 추천 상품 조회
api_key = "f32e4b34e9c7dfc82f8092d98ef09be2"  # 실제 발급받은 API 키를 입력해야 합니다.
recommended_product = recommend_best_savings_product(api_key)

if recommended_product:
    print("가장 짧은 기간과 가장 높은 금리를 가진 상품 정보:")
    print(recommended_product)