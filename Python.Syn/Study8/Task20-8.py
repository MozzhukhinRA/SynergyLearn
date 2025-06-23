dict_unit = {}
print("Enter the beginning of the interval")
num_start = int(input())
print("Enter the end of the interval")
num_end = int(input())

if num_start >= num_end:
    num_start += 1
    while num_start != num_end:
        num_start -= 1
        dict_unit[num_start] = num_start
        dict_unit[num_start] = num_start ** num_start

elif num_start <= num_end:
    num_start -= 1
    while num_start != num_end:
        num_start += 1
        dict_unit[num_start] = num_start
        dict_unit[num_start] = num_start ** num_start

print(dict_unit)

#значениями этих ключей будут сами эти числа возведённые в степени равных этим числам