texto = input("Digite aqui o seu texto:\n")

tamanho = len(texto.replace(" ", ""))

print (f"Quantidade de caracteres é {tamanho}, E o texto em maiúsculo: {texto.upper()}, o texto em minúsculo: {texto.lower()} e utilizando slice(fatiamento): {texto[-9:]}")