def factorial():
    count = 1
    while 1:
        product = 1

        for i in range(1, count+1):
            product *= i

        yield product
        count += 1;
        product = 1


fa = factorial()

for i in range(10):
    print(next(fa))


k = [print(i) for i in "maverick" if i not in "aeiou"]
