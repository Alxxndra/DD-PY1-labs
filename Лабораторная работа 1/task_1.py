numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
sum=0
count=len(numbers)
for i in range(count):
    if numbers[i] == None:
        j = i
        continue
    sum += numbers[i]

average = sum/count
numbers[j] = average
# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
