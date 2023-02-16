print('Pesquisa ESPORTES')
print()

#Listas das respostas
respostas = list()
opcoesesportes = ["FUTEBOL", "VOLEI", "BASQUETE", "CICLISMO", "HANDBALL","OUTRO"]
opcoessemana = ["1 X NA SEMANA", "2 X NA SEMANA", "3 X NA SEMANA", "4 X NA SEMANA", "5 X NA SEMANA OU MAIS"]
esporte=0

while opcoessemana:
   print('''
   0 - Entrar no programa
   1 - Cadastrar esporte
   2 - Mostrar dados da lista
   3 - Remover dados da lista''')

   opcaomenu=int(input("Digite a opção desejada: "))
   if opcaomenu==0:
      #pergunta1
      print("Yasmin: Qual seu esporte favorito ? ")
      print(opcoesesportes)
      esporte=input("Digite o nome: ")
      if esporte=='outro':
         esportes=input("Julia: Qual é o esporte? ")
         opcoesesportes.append(esportes)
      if esporte!=opcoesesportes:
         print("Erro! Opção não existente")

      #pergunta2
      print("Yasmin: Quantas vezes você pratica na semana? ")
      for item in opcoessemana:
         print(item)  
      semana = int(input('Vinicius: Digite uma a frequência: '))      
   elif opcaomenu==1:
      opcoesesportes.append(str(input("Digite o nome do esporte: ")))
      print("Esporte cadastrado com sucesso!")
   elif opcaomenu==2:
      print("Lista de opções de esporte", opcoesesportes)
      print("Lista de opções de frequência", opcoessemana)
   elif opcaomenu==3:
      remover=input("Vinicius: Qual esporte deseja remover? ")
      for n in opcoesesportes:
         if n==remover:
            del opcoesesportes[n]
      print("Esporte removido com sucesso!")
   else:
      print("Erro! Opção não existe no menu")
      break


   #Finalizar
   resp = str(input('Deseja continuar? [S]/[N] => ')) 
   if resp in 'N,n':
      break
cont=0
#Print das repostas
print(esporte, semana)