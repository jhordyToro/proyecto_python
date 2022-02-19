def main():
    
                                             # LIST COMPREHENSIONS
      #ELEVADO AL CUADRADO DE LOS NUMEROS DEL RANGO 1 AL 10
    # my_list = range(1,11)
    # m = [i ** 2 for i in my_list]
    # print(m)
     
      #VALOR AL CUADRADO DE LOS QUE NO SON MULTIPLOS DE 3
    # my_list = range(1,101)
    # m = [i ** 2 for i in my_list if i % 3 != 0]
    # print(m)
      
      #NUMEROS DEL 1 AL 99999 QUE SON MULTIPLOS DE 4,6 Y 9
    # rang = range(1, 100000)
    # challenge = [i for i in rang if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    # print(challenge)

                                                 #DICTIONARY COMPREHENSIONS
     
      #LO MISMO PERO EN UN DICCIONARIO, LA LLAVE COMO EL VALOR Y EL VALOR COMO LA LLAVE AL CUADRADO
    # rang = range(1, 101)
    # my_dictionary = {i: i**3 for i in rang}
    # print(my_dictionary)
      
      #MUESTRA EL VALOR AL CUADRADO SOLO LOS QUE SON MULTIPLOS DE 3, LA LLAVE COMO EL VALOR Y EL VALOR COMO RESULTADO
    # rang = range(1,101)
    # my_dictionary = {i: i**3 for i in rang if i % 3 != 0}
    # print(my_dictionary)
      
      #MUESTRA I COMO LLAVE DEL LOS NUMEROS DEL RANGO DEL 1 AL 1000 Y EL VALOR ES LA LAIS CUADRADA DE EL VALOR DE LA LLAVE
    rang = range(1,1001)
    my_dictionary = {i: i**0.5 for i in rang}
    print(my_dictionary)
     

if __name__ == "__main__":
    main()