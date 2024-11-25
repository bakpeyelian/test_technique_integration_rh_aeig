def are_anagrams(caractere1 : str, caratere2 : str):
    if sorted(caractere1) == sorted(caratere2):
        return True
    else:
        return False
    
""" print(are_anagrams("amour","amoru1")) """