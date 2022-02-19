def ops(num):
    lis = [i for i in range(1, num +1) if num % i == 0]
    return lis
    

def main():
    try:
        num = int(input("dame un valor de tipo entero "))
        if num <0:
            raise ValueError
        print(ops(num))
    except ValueError:
        print('eso no se puede hacer :(')


if __name__ == '__main__':
    main()