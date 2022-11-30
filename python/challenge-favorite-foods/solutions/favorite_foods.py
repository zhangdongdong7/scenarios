foods = []

while True:
    food = input('Enter your favorite foods (press Enter on an empty line to stop): ')
    if food == '':
        break
    foods.append(food)
    
print('Your favorite foods are:')
for food in foods:
    print(food)