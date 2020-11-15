def generate_hashtag(s):
    lista = list(s)
    if len(lista)>140:
        return False
    if len(s) > 0:

        lista = list(s.split())

        for i in range(len(lista)):
            lista[i] = lista[i].capitalize()

        lista.insert(0,"#")

        return "".join(lista)
    else:
        return False


print(generate_hashtag("Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat"))
