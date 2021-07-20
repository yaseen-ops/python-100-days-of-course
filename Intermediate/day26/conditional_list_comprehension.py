range_list = [num for num in range(1, 20) if num % 3 == 0]
print(range_list)

name_list = ["Dhoni", "Tendulkar", "Yuvraj", "Kohli", "Abd"]
short_names = [name for name in name_list if len(name) <= 5]
print(short_names)

long_names = [name.upper() for name in name_list if len(name) > 5]
print(long_names)


