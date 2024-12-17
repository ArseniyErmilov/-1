import random

random_number = random.randint(0, 100)

num = int(input('введите число от 0 до 100:'))
if random_number > num:
    print('число больше')
elif random_number < num:
    print('число меньше')
else:print("вы угадали число")
