import random
import string

def gerar_senha(comprimento=12, maiusculas=True, minusculas=True, numeros=True, especiais=True):
    caracteres = ''
    if maiusculas:
        caracteres += string.ascii_uppercase
    elif minusculas:
        caracteres += string.ascii_lowercase
    elif numeros:
        caracteres += string.digits
    elif especiais:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Pelo menos um tipo de caracteres deve ser selecionado")

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def main():
    print("Gerador de senhas ")

    comprimento = int(input("Informe o comprimento da senha: "))
    maiusculas = input("Incluir letras maiusculas? (s/n): ").lower() == "s"
    minusculas = input("Incluir letras minusculas? (s/n): ").lower() == "s"
    numeros = input("Incluir números? (s/n): ").lower() == "s"
    especiais = input("Incluir especiais? (s/n): ").lower() == "s"

    senha = gerar_senha(comprimento, maiusculas, minusculas, numeros, especiais)
    print(f"Senha gerada: {senha}")

if __name__ == "__main__":
    main()
