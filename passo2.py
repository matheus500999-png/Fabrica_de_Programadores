contador = 0
while contador <3:
    contador = contador +1
    arquivo = open("arquivo2.txt","a", encoding="utf-8")
    nome = input("digite um nome: \n")
    arquivo.write(f"\n{nome}\n")

    arquivp.close()
print("\n","-"*20,"\narquivo criado com sucesso\n","-"*20)
