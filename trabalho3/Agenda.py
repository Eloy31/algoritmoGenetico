from random import randint

class agenda:
    def __init__(self, genes = None, qtd = 45):
        self.qtd = qtd
        self.label = {
            1: "Segunda - 9hrs",
            2: "Segunda - 10hrs", 
            3: "Segunda - 11hrs",            
            4: "Segunda - 12hrs",
            5: "Segunda - 13hrs", 
            6: "Segunda - 14hrs",
            7: "Segunda - 15hrs",
            8: "Segunda - 16hrs",
            9: "Segunda - 17hrs",
            10: "terça - 9hrs",
            11: "terça - 10hrs",
            12: "terça - 11hrs",
            13: "terça - 12hrs",
            14: "terça - 13hrs",
            15: "terça - 14hrs",
            16: "terça - 15hrs",
            17: "terça - 16hrs",
            18: "terça - 17hrs",
            19: "quarta - 9hrs",
            20: "quarta - 10hrs",
            21: "quarta - 11hrs",
            22: "quarta - 12hrs",
            23: "quarta - 13hrs",
            24: "quarta - 14hrs",
            25: "quarta - 15hrs",
            26: "quarta - 16hrs",
            27: "quarta - 17hrs",
            28: "quinta - 9hrs",
            29: "quinta - 10hrs",
            30: "quinta - 11hrs",
            31: "quinta - 12hrs",
            32: "quinta - 13hrs",
            33: "quinta - 14hrs",
            34: "quinta - 15hrs",
            35: "quinta - 16hrs",
            36: "quinta - 17hrs",
            37: "sexta - 9hrs",
            38: "sexta - 10hrs",
            39: "sexta - 11hrs",
            40: "sexta - 12hrs",
            41: "sexta - 13hrs",
            42: "sexta - 14hrs",
            43: "sexta - 15hrs",
            44: "sexta - 16hrs",
            45: "sexta - 17hrs",
        }
        self.genes = list()
        count = 0
        if genes == None:
            for i in range(qtd):
                if i not in [3,12,21,30,39]:
                    if count >= 8:
                        self.genes.append(0)
                    else:
                        palestra = randint(0,1)
                        self.genes.append(palestra)
                        if palestra == 1:
                            count+=1
                else:
                    self.genes.append(1)
        else: 
            self.genes = genes
        self.calculo_custo()
    
    def __lt__(self, outro):
        return self.custo >= 13 and (self.custo < outro.custo)

    def calculo_custo(self):
        self.custo = 0
        for i in range(len(self.genes)):
            if self.genes[i] == 1:
                self.custo += 1
    
    def print(self):
        for i in range(len(self.genes)):
            if self.genes[i] == 1:
                if i in [3,12,21,30,39]:
                    texto = "Almoço" 
                else:
                    texto = "Palestra"
            else:
                texto = "Horário Vazio"
            print(f"{self.label[i+1]} = {texto}")