def sumaTodos(limitTo):
    output = 0
    for i in range(limitTo + 1):
        output += i
    return output

print(sumaTodos(100))