import sqlite3
import os

conexao = sqlite3.connect("dados.db")
cursor = conexao.cursor()
opcao = "" #just creating one space with no info.

while opcao != 0: #The ! means NO, (about something)
    os.system('cls')
    print("O que você quer fazer?")
    print("1. Criar tabela usuarios")
    print("2. Apagar tabela usuarios")
    print("3. Criar dados na tabela usuarios")
    print("4. Acessar dados da tabela usuarios")
    print("5. Atualizar todos os nomes de dados na tabela usuarios para 'Alguma coisa'")
    print("6. Apagar todos os dados na tabela usuarios")
    print("Nenhum dos acima, fechar programa")

    print("")
    opcao = input("Digite o número da opção que você quer e aperte ENTER: ")
    print("")
    
    if opcao == "1":
        conexao.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, idade INTEGER NOT NULL)")
        print("Criado tabela usuarios")

    elif opcao == "2":
        conexao.execute("DROP TABLE usuarios")
        print("Apagado tabela usuarios")

    elif opcao == "3":
        conexao.execute("INSERT INTO usuarios(nome, idade) VALUES(?, ?)", ["Jonathan Santos", 22])
        conexao.execute("INSERT INTO usuarios(nome, idade) VALUES(?, ?)", ["Renan Santos", 27])
        conexao.execute("INSERT INTO usuarios(nome, idade) VALUES(?, ?)", ["Murillo Santos", 19])
        conexao.commit()
        print("Criado 3 dados na tabela usuarios")

    elif opcao == "4":
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM usuarios")
        rows = cursor.fetchall()

        if (len(rows) == 0): #lens means how much (quantify everything in the variable.. rows <> linhas)
            print("Sem usuarios")
        else:
            print("Resultados:")
            for row in rows:
                print(row)

    elif opcao == "5":
        cursor.execute("UPDATE usuarios SET nome=?", ["Alguma coisa"])
        conexao.commit()
        print("Atualizado todos os dados na tabela usuarios com o nome 'Alguma coisa'")

    elif opcao == "6":
        cursor.execute("DELETE FROM usuarios")
        conexao.commit()
        print("Apagado todos os usuários")
    else:
        print("Nenhuma opção válida selecionada, fechando o programa")
        opcao = 0

    print("")
    input("Para continuar, aperte ENTER")
    print("")