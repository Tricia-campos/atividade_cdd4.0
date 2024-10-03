usuarios = []
senhas = []

def cadastro():
      usuario = input("Digite o nome de usuario: ")
      if usuario in usuario:
            print("usuario cadastrado")
      senha = int(input("Digite a senha numerica:"))
      usuarios.append(usuario)
      senhas.append(senha)
      print("cadastro feito com sucesso")

def login():
      while True:
            usuario = input("Digite o nome de usuario: ")
            senha = int(input("Digite a senha numerica:"))
            if usuario in usuarios:
                  for i in range(len(usuarios)):
                        if usuarios[i] == usuario and senhas[i] == senha:
                              print(f"Bem vindo, {usuario}")
                              return
                        else:
                              print("usuario ou senhas incorretos")

def mostrar():

def menu():
      while True:
            print(f" BEM VINDO!!\n"
                  f"DIGITE 1 PARA REALIZAR CADASTRO\n"
                  f"DIGITE 2 PARA FAZER LOGIN\n"
                  f"DIGITE 3 PARA MOSTRAR OS USUARIOS\n"
                  f"DIGITE 4 PARA SAIR\n")

            bv = int(input("Digite a opcão desejada: "))
            if bv ==1:
                  cadastro()
            elif bv == 2:
                  login()
            elif bv == 3:
                  mostrar()
            elif bv == 4:
                  print("finalizando")
                  break
            else:
                  print("invalido")
menu()