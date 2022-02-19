def ops(num):
    lis = [i for i in range(1, num +1) if num % i == 0]
    return lis
    

def main():
    num = input("dame un valor de tipo entero ")
    assert num.isnumeric(), "no estan disponibles las letras ni los numeros negativos"
    print(ops(int(num)))
 


if __name__ == '__main__':
    main()