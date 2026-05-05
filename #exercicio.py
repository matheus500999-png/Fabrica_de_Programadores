#exercicio

arquivo = open("arquivo.txt", "w", encoding="utf-8")
arquivo.write("\nMatheus\n")
arquivo.close()
nome = input("digite seu nome: \n")
arquivo.write("-"*10)
arquivo.write(f"\naluno: {nome}\n")
arquivo.write("-"*10)