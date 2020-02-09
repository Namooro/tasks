def fibonacci():
    """ function, that contains generator yielding Fibonacci numbers
        and prints Fibonacci number as an integer every 0.5 seconds
    """
    import time
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y
        time.sleep(0.5)


if __name__ == '__main__':
    ([print(i) for i in fibonacci()])
