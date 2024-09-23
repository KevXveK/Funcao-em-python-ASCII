def ascii():
    # Lê a entrada do usuário como uma string
    numeros = input("Digite a sequência numérica (separada por espaços ou virgulas): ")
    
    lista = []
    
    # Divide a string em partes e converte para inteiros
    for num in numeros.split(","):
        lista.append(chr(int(num)))  # Converte cada número e adiciona à lista

    return ''.join(lista)  # Retorna a string formada pela lista de caracteres

resultado = ascii()
print(resultado)







    
    

