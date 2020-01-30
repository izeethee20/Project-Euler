def sum_step(number, degree):
    result = 0
    number **= degree
    num = len(str(number))
    for i in range(0, num):
        result += number % 10
        number = number // 10
    return result

print("Sum = ", sum_step(2, 1000))
