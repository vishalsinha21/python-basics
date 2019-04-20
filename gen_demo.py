def fib_gen():
    a = 0
    b = 1

    yield a
    yield b

    while 1:
        c = a + b
        a = b
        b = c
        yield c


fs = fib_gen()

for i in range(10):
    print(next(fs))
