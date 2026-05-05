lista_de_usuario = ["matheus","joão"]
senha_do_usuario = ["th4us","jo123"]


usuario = input("digite seu usuario...\n").capitalize
senha = input("digite sua senha...\n")

usuario = (lista_de_usuario).index
senha = (senha_do_usuario).index

index_usuario = lista_de_usuario.index(usuario)
index_senha = senha_do_usuario.index(senha)

if index_usuario == index_senha:
    print("login bem sucedido!!!")
else:
    print("usuário ou senha invalida!!!")
