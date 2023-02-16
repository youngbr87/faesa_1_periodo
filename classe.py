class Nó:
   esquerda, direita, valor = None, None, 0

   def __init__(self, valor):
     # construtor dos valores
     self.esquerda = None
     self.direita = None
     self.valor = valor

class Ordenação:
   def __init__(self):
     # inicializa a raiz da árvore
     self.raiz = None

   def AdicionaNo(self, valor):
     return Nó(valor)

   def Inserir(self, raiz, valor):
     # inserir novo valor
     if raiz == None:
         # não há nenhum valor
         return self.AdicionaNo(valor)
     else:
         # já está na árvore
         if valor <= raiz.valor:
            # se os dados forem menores do que os armazenados
            # entra na sub-árvore do lado esquerdo
            raiz.esquerda = self.Inserir (raiz.esquerda, valor)
         else:
            # entra na sub-árvore do lado direito
            raiz.direita = self.Inserir (raiz.direita, valor)
         return raiz
     
class A:
  a = 1 # atributo publico
__b = 2 # atributo privado a class A

class B:
 _c = 3 # atributo privado
   
def __init__(self):

        print(A)
        print(__b)

        a = A()
        print (isinstance(a, B)) # ''Objeto a'' é uma instância da ''classe B''? Falso.

        a = B() # Instancía o ''objeto a'' na ''classe B'' e imprime os atributos da classe.
        print (isinstance(a, B)) # ''Objeto a'' é uma instância da ''classe B''?Verdadeiro.

        b = B() # Instancía o ''objeto b'' na ''classe B'' e imprime os atributos da classe.
        print (isinstance(b, B)) # ''Objeto b'' é uma instância da ''classe B''? Verdadeiro.

        b = A() # Instancía o ''objeto b'' na ''classe A''.
        print (isinstance(b, A)) # ''Objeto b'' é uma instância da ''classe A''? Verdadeiro.