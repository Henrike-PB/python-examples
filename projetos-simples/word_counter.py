from collections import Counter
import string

texto = input("Digite um texto: ")

# Remover pontuação e converter para minúsculas
texto = texto.lower()
texto = texto.translate(str.maketrans("", "", string.punctuation))

palavras = texto.split()
contagem = Counter(palavras)

print("Contagem de palavras:")
for palavra, qtd in contagem.items():
    print(f"{palavra}: {qtd}")
