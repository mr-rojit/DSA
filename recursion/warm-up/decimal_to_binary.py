def decimal_to_binary(n):
    if n == 1:
        return "1"
    div = n // 2
    rem = n % 2

    return decimal_to_binary(div) + str(rem)

print(decimal_to_binary(156))