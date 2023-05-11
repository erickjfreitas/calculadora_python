def menu():  #criando o menu
    iniciar=1   #defini a variavel 'iniciar' com valor de 1
    while iniciar:
        iniciar = int(input("0. Sair \n"+ "1. Começar o jogo\n")) #recebo a resposta do jogador
        if iniciar:  # se a opção escolhida for 1 então o jogo é iniciado
            jogada()
        else:
            print("Saindo...")

def jogada(): #definindo jogadas
    rodada=0 
    controle=0
    while controle<10: 

     while ganhador()==0:
       print('\nJogador', rodada%2 + 1 )
       mostrar()
       l=int(input("Linha:  "))
       c=int(input("Coluna:  "))
       if l >3 or c >3:
         print ("!!! COMANDO INVÁLIDO !!!")

       if velha [l-1][c-1]==0:
         if (rodada%2+1)==1:
             velha [l-1][c-1]=1
         else:
             velha[l-1][c-1]=-1

       else :
         print('O espaço já está preenchido')
         rodada-=1

       if ganhador():
         print ('O jogador', rodada%2 +1 , 'Ganhou' )
     
       rodada+=1
       controle+=1
    
def ganhador():

    for i in range (3):
        soma = velha[i][0]+ velha[i][1]+ velha[i][2]
        if soma ==3 or soma ==-3:
          return 1
    for i in range (3):
        soma=velha[0][i] + velha[1][i] + velha [2][i]
        if soma ==3 or soma==-3:
            return 1
    principal=velha[0][0]+velha[1][1]+velha[2][2]
    secundaria=velha[2][0]+velha[1][1]+velha[0][2]
    if principal==3 or principal==-3 or secundaria==3 or secundaria==-3:
        return 1

    return 0

def mostrar():

    for i in range(3):
        for j in range (3):
            if velha [i][j]==0:
                print (' _ ', end=' ')
            elif velha [i][j]==1:
                print (' X ', end=' ')
            elif velha [i][j]==-1:
                print (' O ', end=' ')
        print ()


velha = [ [0,0,0],
          [0,0,0],
          [0,0,0]]


menu()