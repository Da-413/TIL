# 원주율
pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
# 반지름
radius = 15

pi_value = '원주율 : '
radius_value = '반지름 : '
circumference = '원의 둘레 : '
area = '원의 넓이 : '

print(f'{pi_value}{pi}')
print(f'{radius_value}{radius}')
print(f'{circumference}{2 * radius * pi}')
print(f'{area}{radius * radius * pi}')