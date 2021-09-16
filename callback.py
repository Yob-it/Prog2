def my_sum(*val):
    result = 0
    for x in val:
        result = result + x
    return result

print(my_sum(1, 4, 5))
