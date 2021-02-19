from math import floor
from random import randint
from Agenda import agenda

class ag():
    def __init__(self, numeroPopulacao = 100, numeroGeracoes = 30, taxaMutacao = 2e-3, taxaSobrevivencia = 0.4):
        self.genes = 45
        self.numeroPopulacao = numeroPopulacao
        self.numeroGeracoes = numeroGeracoes
        self.populacao = list()
        self.genemutados = (taxaMutacao * numeroPopulacao)
        self.numeroSobreviventes = floor(numeroPopulacao * taxaSobrevivencia)

    def gera_populacao(self):
        for i in range(self.numeroPopulacao):
            self.populacao.append(agenda())

    def selecao(self):
        #Dá um sort baseado na função custo
        self.populacao.sort()
        #Deixa só o numero de individuos da populacao que sobreviveram
        self.listasobreviventes = self.populacao[:self.numeroSobreviventes]

    def cruzamento(self):
        # Até completar a populacao
        while len(self.listasobreviventes) < self.numeroPopulacao:
            indMae = randint(0, self.numeroPopulacao-1)
            # escolhe A(ALterar)
            mae = self.populacao[indMae]
            # escolhe um B != A(Alterar)
            indPai = randint(0, self.numeroPopulacao-1)
            while indPai == indMae:
                indPai = randint(0, self.numeroPopulacao-1)
            pai = self.populacao[indPai]
            # cria item filho
            c = list()
            for i in range(self.genes):
                if 0 <= i <= self.genes//2:
                    c.append(mae.genes[i])
                else:
                    c.append(pai.genes[i])
            self.listasobreviventes.append(agenda(genes=c))

    def mutacao(self):
            for i in range(self.genemutados):
                self.populacao[randint(0, self.numeroPopulacao-1)].palestras[randint(0, 45)] = randint(0, 1)


    """
    Aplica os passos do algoritmo genético
    """
    def solve(self):
        geracao = 0
        # Cria a populacao original
        self.gera_populacao()
        # Evolução dos genes
        while geracao < self.numeroGeracoes:
            # selecao
            self.selecao()
            # cruzamento
            self.cruzamento()
            # mutacao
            # self.mutacao()
            self.populacao = self.listasobreviventes
            geracao += 1
        # exibe o gene com o resultado
        for i in range(10):
            print(f'------------------Agenda nº {i+1}-------------------')
            self.populacao[i].print()
            print()
            