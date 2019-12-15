"""Les lettres normales ont été remplacé par la 7ème lettre précédente. Crée une fonction qui prend en paramètre un message sous forme de liste ou de chaine de caractère, et affiche le message correctement(décrypté)"""


def decode(lettres):
    dico = {}
    for i in range(26):
        i_decalage = (i + 26 - 7)
        if i_decalage >= 26:
            i_decalage = i_decalage - 26
        message_decalage = chr(i_decalage + ord('a'))
        decale = chr(i + ord('a'))
        dico[decale] = message_decalage
        message_decalage = chr(i_decalage + ord('A'))
        decale = chr(i + ord('A'))
        dico[decale] = message_decalage
    dico[' '] = ' '

    result = ""
    for decale in lettres:
        result = result + dico[decale]
    return result


messagecrypte = "Dlzo iyv ab jvklz lu wfaovu thpualuhua"
message = decode(messagecrypte)
print(message)
