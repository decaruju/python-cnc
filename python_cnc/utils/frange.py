def frange(start, end, step):
    current = start
    while (end-current)/step >= 0:
        yield current
        current += step
