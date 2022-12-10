# prompt the user for a temperature and a unit
temp_list = ['32F', '50F', '40C', '38F',
             '36C', '45F', '55C', '65F', '75C', '85F']

ans = ''

# 0C 10C 104F 3C 96F 7C 131F 18C 167F 29C

for i in temp_list:
    temp_num = float(i[:-1])
    temp_unit = i[-1]
    if temp_unit == "C":
        converted_temp = (temp_num * 9/5) + 32
        converted_temp = int(converted_temp)
        new_unit = "F"
        ans += f"{converted_temp}{new_unit} "
    else:
        converted_temp = (temp_num - 32) * 5/9
        converted_temp = int(converted_temp)
        new_unit = "C"
        ans += f"{converted_temp}{new_unit} "
print(ans)
