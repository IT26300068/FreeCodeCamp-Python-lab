def number_pattern(n):
    if type(n) is not int:
        return 'Argument must be an integer value.'

    if n < 1:
        return 'Argument must be an integer greater than 0.'

    results = []

    for i in range(1, n + 1):
        results.append(str(i))

    return ' '.join(results)

print(number_pattern(4))
