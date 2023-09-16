def promedio(*args):
    return sum(args) / len(args)


def combinacion(p1, p2, p3, *args, p4=500):
    print(p1)
    print(p2)
    print(args)
    print(p4)
combinacion(10, 20, 1, 5, 8)