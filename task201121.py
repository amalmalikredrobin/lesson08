# from typing import Iterable


# cities = ['Tashkent', 'Bukhara', 'Samarkand', 'Khorezm', 'Fergana', 'Karshi', 'Nukus', 'Termez', 'Namangan', 'Andijan']
# three_cities = cities[3:6]
# print(three_cities)
# reversed_cities = cities[::-1]
# print(2 in cities)

# for city in cities:
#     print(city)

# text = 'My name is Amalmalik. I am 27 years old'
# for letter in text:
#     print(letter)


# cities = ('Tashkent', 'Bukhara', 'Samarkand', 'Khorezm', 'Fergana', 'Karshi', 
# 'Nukus', 'Termez', 'Namangan', 'Andijan')

# for city in cities:
#     print(city)

# range(10)
# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# for num in range(20, 10, -1):
#     print(num)

    # Iterable
    # 1. List  - []
    # 2. tuple - ()
    # 3. string - '', ""
    # 4. range()

# for i in range(11):
#     print(i * i)

# for i in range(0,1,2,3,4,5,6,7,8,9,10):
#     print(i * i, i * i * i)

# acc = 0
# for num in range(1, 11):
#     acc = acc + num    
    
# print(acc)

# acc = 1
# for num in range(1, 11):
#     acc = acc * num    
    
# print(acc)

# for num in range(0, 21, 2):
#     print(num)


cities = ['Tashkent', 'Bukhara', 'Samarkand', 'Khorezm', 'Fergana',
'Karshi', 'Nukus', 'Termez', 'Namangan', 'Andijan']

acc = ''
cities_len = len(cities)
for i in range(len(cities)):
    if i != len(cities) - 1:
        acc += cities[i] + ', '
else: acc += cities[i]
print(acc)