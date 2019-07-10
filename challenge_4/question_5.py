def flo(n):
    n = float(n)
    try:
        print(n)
    except ValueError:
        print('Can not convert')

flo('python')

