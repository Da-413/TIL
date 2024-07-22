import pprint
import requests

# 상품과 옵션 정보들을 담고 있는 새로운 객체를 만들어 반환하시오.
# [힌트] 상품 리스트와 옵션 리스트를 금융상품 코드를 기준으로 매칭할 수 있습니다.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터를 변수에 저장합니다.
# 3. 2번의 결과 중 key 값이 "baseList" 인 데이터를 변수에 저장합니다.
# 4. 2번의 결과 중 key 값이 "optionList" 인 데이터를 변수에 저장합니다.
# 5. 3번에서 저장된 변수를 순회하며, 4번에서 저장된 값들에서 금융 상품 코드가 
#     같은 모든 데이터들을 가져와 새로운 딕셔너리로 저장합니다.
#     저장 시, 명세서에 맞게 출력되도록 저장합니다.
# 6. 5번에서 만든 딕셔너리를 결과 리스트에 추가합니다.


def get_deposit_products():
    api_key = "f32e4b34e9c7dfc82f8092d98ef09be2"
    url = 'https://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params = {
        'auth': api_key,
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    # 요구사항에 맞도록 이곳의 코드를 수정합니다.
    response = requests.get(url, params = params).json()
    option = response['result']['optionList']
    base_list = response['result']['baseList']
    
    option_list = []
    for data in option:
        temp_dict = {}
        temp_dict['금융상품코드'] = data['fin_co_no']
        temp_dict['저축 금리'] = data['intr_rate']
        temp_dict['저축 기간'] = data['save_trm']
        temp_dict['저축금리유형'] = data['intr_rate_type']
        temp_dict['저축금리유형명'] = data['intr_rate_type_nm']
        temp_dict['최고 우대금리'] = data['intr_rate2']
    
        option_list.append(temp_dict)
    
    result = []

    for info in base_list:
        temp_dict = {'금리정보': []}
        for opt in option_list:

            if opt['금융상품코드'] == info['fin_co_no']:
                opt_dict = {}
                opt_dict['저축 금리'] = opt['저축 금리']
                opt_dict['저축 기간'] = opt['저축 기간']
                opt_dict['저축금리유형'] = opt['저축금리유형']
                opt_dict['저축금리유형명'] = opt['저축금리유형명']
                opt_dict['최고 우대금리'] = opt['최고 우대금리']
                temp_dict['금리정보'].append(opt_dict)
                temp_dict['금융상품명'] = info['fin_prdt_nm']
                temp_dict['금융회사명'] = info['kor_co_nm']
        
        result.append(temp_dict)

    return result


if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)