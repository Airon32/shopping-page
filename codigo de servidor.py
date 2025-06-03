print("codigo de login")
from time import sleep 

capacidade_do_servidor = 30
servidores_ativos = 1
usuarios_cadastrados = 0
cadastro = []

while True:
    print("\n=== pagina de compras ===")
    opcoes = int(input(
        "[1] - casastro\n"
        "[2] - entrar" \
        ": "
    ))
    if opcoes == 1:

        nome = input("digite o seu nome: ").lower()
        senha = str(int(input("digite a sua senha: "))).lower
        email = input("digite o seu email: ")

        login = {
            "nome": nome,
            "senha": senha, 
            "email": email
        }

        print(f"o login com o nome: {nome} foi criado com sucesso")

        cadastro.append(login)
        usuarios_cadastrados += 1 

    if opcoes == 2:
        saldo = 1000

        print("=== pagina de login ===\n")

        email = input("digite o seu email: ")
        senha = input("digite a sua senha: ")

        encontrados = False

        for usuario in cadastro:
                
                if usuario['email'] == email and usuario['senha'] == senha:
                    encontrado = True
                    
                    print("verificando dados...")
                    sleep(2)

                    print(f"bem vindo {usuario['email']} ao sistema")
                else:
                    print("senha ou email incorretos")

                print("seja bem vindo a tela principal")
                print(f"seu saldo para realizar suas comprar ou vender produtos é R${saldo}\n")

                escolhas = int(input(
                     "[1] - compra um produto\n"
                     "[2] - vender der algum produto\n"
                     "[3] - ver carrinho"
                ))

                if escolhas == 1:
                     