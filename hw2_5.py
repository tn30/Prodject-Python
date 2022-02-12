number = int(input("Ведите, пожалуйста, номер рейтинга: "))
numbers = [7, 5, 3, 3, 2]

numbers.append(number)
numbers.sort(reverse=-1)

print(numbers)