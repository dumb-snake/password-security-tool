# score : faible[0 1], moyen[2], fort[3]
# exceptions :
# longeur --> LGR
# majuscule --> MAJ
# characteres spéciaux --> SPE
# chiffres --> NUM
# minuscule --> MIN


import string 

MAX_SCORE = 5 # 5 tests à réaliser 
MIN_LGR = 8
MIN_NUM = 1
MIN_UPPER = 1
MIN_LOWER = 1

def checker(password):

    score = MAX_SCORE
    missing = [] # si une exception --> retourner le code manquant
    strength = "unknown"

    # check length : MIN = 8
    if len(password) < MIN_LGR:
        missing.append("Length of 8 characters")
        score = score -1

    # check uppercase : MIN = 1

    if(sum(map(str.isupper, password))) < MIN_UPPER :
        missing.append("Uppercase letters")
        score = score -1

    # check lowercase : MIN = 1

    if(sum(map(str.islower, password))) < MIN_LOWER :
        missing.append("Lowercase letters")
        score = score -1

    # check numbers  : MIN = 2

    if(sum(map(str.isdigit, password))) <MIN_NUM:
        missing.append("Numbers")
        score = score -1


    # check special   : MIN = 1 
    found_sp = False 
    for item in password:
        if item in string.punctuation:
            found_sp = True
            break
    
    if found_sp == False :
        missing.append("Special characters")
        score = score -1

    
    # Final message 
    # 0 1 2 3 4 5
    match score :
        case 5:
            strength = "fort"
        case 3 | 4:
            strength = "moyen"
        case 0 | 1 | 2:
            strength = "faible"

    
    return score, missing, strength



