def longuest_unique_substring(caractere :str) :
    longueur = len(caractere)
    longueurSubstring = 0
    tab = []
    for x in range(longueur):
        if(x == 0):
            tab.append(caractere[x])
        elif(x > 0):
            if caractere[x] not in tab :
                tab.append(caractere[x])
    return len(tab)
""" print(longuest_unique_substring("aaaabb")) """