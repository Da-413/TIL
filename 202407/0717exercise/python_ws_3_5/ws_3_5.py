number_of_people = 0
number_of_book = 100

def increase_user():
    global number_of_people
    number_of_people += 1


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(name, age, address):
    increase_user()
    user_info = {'name': name, 'age': age, 'address': address}
    print(f'{name}님 환영합니다!')
    return user_info


many_user = list(map(create_user, name, age, address))


def decrease_book(num):
    global number_of_book
    number_of_book -= num
    print(f'남은 책의 수 : {number_of_book}')


info_ = list(map(lambda user_info: {'name': user_info['name'], 'age': user_info['age'], 'rental_book': user_info['age'] // 10}, many_user))


def rental_book(info):
    decrease_book(info['rental_book'])
    print(f"{info['name']}님이 {info['rental_book']}건의 책을 대여하셨습니다.")


list(map(rental_book, info_))
