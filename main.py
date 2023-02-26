from time import sleep
class Aluno:
    #atributos
    func = "aluno"
    nome = ""
    tec = ""
    periodo = ""

    #métodos
    #adicionar
    def __init__(self):
        nome = input("Qual é seu nome? ")
        self.nome = nome

        tec = input("Qual é a sigla do seu curso técnico? ")
        self.tec = tec

        periodo = input("Qual é o número seu período ")
        self.periodo = periodo

    #Definir turma
    def turma(self):
        turma = self.tec + " 1" + self.periodo + "1"
        return turma

    
    #Perguntar nova pessoa
    def perguntar(self):
        pergunta = input("Então você é " + self.nome + " da turma "+ self.turma() + "? [S/N]").strip().upper()
        while pergunta != "S":
            self = Aluno()
            pergunta = input("Então você é " + self.nome + " da turma "+ self.turma() + "? [S/N]").strip().upper()
        
    #Cumprimentar pessoa 
    def cumprimentar(self):
        print("Oi, meu nome é " + self.nome +" e sou da turma " + self.turma())
        sleep (1)
        pessoa2 = Aluno() 
        pessoa2.perguntar()
        print ("Prazer em te conhecer!!!")

#Player 1
print("-" * 8)
print("Player 1")
print("-" * 8)
sleep(3)
pessoa1 = Aluno()

#Player 2
print("-" * 8)
print("Player 2")
print("-" * 8)
sleep(3)
pessoa1.cumprimentar()
