def leer():
    with open ("./archivos/numeros.txt", "r", encoding="utf-8") as f:
        for leer in f:
            print(int(leer))

def write():
    lis = ["carlos", "marta", "michel", "jatzoñ"]
    with open ("./archivos/names.txt", "a", encoding="utf-8") as f:
        for i in lis:
            f.write(i)
            f.write("\n")

if __name__ == "__main__":
    write()