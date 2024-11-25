def sum_of_digits(nombre : int):
    s = 0
    if nombre >= 0 :
        for k in str(nombre):
            s += int(k)
        return s
    else :
        print("Merci d'entrer un nombre positif")
        
""" print(sum_of_digits(-12)) """