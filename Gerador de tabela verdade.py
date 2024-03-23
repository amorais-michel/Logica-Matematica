# Importando a biblioteca Truth Table Generator
import ttg


# Criando uma função que vai fazer as nossas paradas
def menu():
    # Perguntando qual é o conectivo que o usuário quer trabalhar

    print("\n1. Conjunção \n2. Disjunção \n3.Condicional \n4.Bicondicional \n5.Disjunção exlusiva \n6.Conectivos de Scheffer \n7.Encerrar")
    escolha = input(("\nDigite uma opção:"))  # Dando uma opção pro usuário escolher

    if escolha == '1':  # se o usuario digita 1, geramos a tabela verdade da conjunção

        print("\n*****************************************************************")
        print("\nTABELA DA CONJUNÇÃO")
        print(ttg.Truths(['p', 'q'], ['p and q '], ints=False))  # gerando a tabela verdade da conjunção
        print("\nVoce quer voltar ao menu? Digite 1, se quer sair, pressione qualquer tecla")
        digito = input()

        if digito == '1':
            menu()
        else:
            exit()

    if escolha == '2':
        print("\n*****************************************************************")
        print("\nTABELA VERDADE DA DISJUNÇÃO")
        print(ttg.Truths(['p', 'q'], ['p or q '], ints=False))
        print("\nVoce quer voltar ao menu? Digite 1, se quer sair, pressione qualquer tecla")
        digito2 = input()

        if digito2 == '1':
            menu()
        else:
            exit()

    if escolha == '3':
        print("\n*****************************************************************")
        print("\nTABELA DA CONDICIONAL")
        print(ttg.Truths(['p', 'q'], ['p => q '], ints=False))
        print("\nVoce quer voltar ao menu? Digite 1, se quer sair, pressione qualquer tecla")
        digito3 = input()

        if digito3 == '1':
            menu()
        else:
            exit()

    if escolha == '4':
        print("\n*****************************************************************")
        print("\nTABELA VERDADE DA BICONDICIONAL")
        print(ttg.Truths(['p', 'q'], ['p = q '], ints=False))
        print("\nVoce quer voltar ao menu? Digite 1, se quer sair, pressione qualquer tecla")
        digito4 = input()

        if digito4 == '1':
            menu()
        else:
            exit()

    if escolha == '5':
        print("\n*****************************************************************")
        print("\nTABELA VERDADE DA DISJUNÇÃO EXCLUSIVA")
        print(ttg.Truths(['p', 'q'], ['p xor q '], ints=False))
        print("\nVoce quer voltar ao menu? Digite 1, se quer sair, pressione qualquer tecla")
        digito5 = input()

        if digito5 == '1':
            menu()
        else:
            exit()

    if escolha == '6':
        print("\n*****************************************************************")
        print("\nTABELA VERDADE DA NEGAÇÃO DISJUNTA (NÃO P OU NÃO Q")
        print(ttg.Truths(['p', 'q'], ['p nand q '], ints=False))
        print("\n*****************************************************************")
        print("\nTABELA VERDADE DA NEGAÇÃO CONJUNTA (NEM...NEM)")
        print(ttg.Truths(['p', 'q'], ['p nor q '], ints=False))
        print("\nVoce quer voltar ao menu? Digite 1, se quer sair, pressione qualquer tecla")
        digito6 = input()

        if digito6 == '1':
            menu()
        else:
            exit()

    if escolha == '7':
        exit()


while True:
    menu()
