

def number_get_bigger2(n):
    if n == 1:
        return n
    else:
        return n * number_get_bigger2(n-1)

def number_get_bigger3(n):
    if n == 1:
        return 6
    else:
        return 10+number_get_bigger3(n-1)

a = number_get_bigger2(3)
print(a)
