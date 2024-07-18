food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]

# 아래에 코드를 작성하시오.
for food_dict in food_list:

    if food_dict['이름'] == '토마토':
        food_dict['종류'] = '과일'

    elif food_dict['이름'] == '자장면':
        print('자장면엔 고춧가루지')

    print(f"{food_dict['이름']} 은/는 {food_dict['종류']} (이)다")

print(food_list)


idx = 0

while(idx < 3):

    food_dict = food_list[idx]

    if food_dict['이름'] == '토마토':
        food_dict['종류'] = '과일'

    elif food_dict['이름'] == '자장면':
        print('자장면엔 고춧가루지')

    print(f"{food_dict['이름']} 은/는 {food_dict['종류']} (이)다")
    
    idx += 1

print(food_list)