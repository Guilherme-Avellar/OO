class Funcionario:

    def __init__(self, nome, salario_bruto, total_acrescimos, total_descontos):
        self.nome = nome
        self.salario_bruto = salario_bruto
        self.total_acrescimos = total_acrescimos
        self.total_descontos = total_descontos

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setSalario_bruto(self, salario_bruto):
        self.salario_bruto = salario_bruto

    def getSalario_bruto(self):
        return salario_bruto

    def setTotal_acrescimos(self, total_acrescimos):
        self.total_acrescimos = total_acrescimos

    def getTotal_acrescimos(self):
        return total_acrescimos

    def setTotal_descontos(self, total_descontos):
        self.total_descontos = total_descontos

    def getTotal_descontos(self):
        return total_descontos

    def getSalario_liquido(self):
        return (self.salario_bruto + self.total_acrescimos) - self.total_descontos



nome = input("Digite o nome do funcionário: ")
salario_bruto = int(input("Digite o salário bruto: "))
total_acrescimos = int(input("Digite acrécimo feito: "))
total_descontos = int(input("Digite a soma de todos os descontos: "))
funcionario = Funcionario(nome, salario_bruto, total_acrescimos, total_descontos)

print(f"Nome = {funcionario.getNome()}")
print(f"Salário Bruto = {funcionario.getSalario_bruto()}")
print(f"Total de acréscimos = {funcionario.getTotal_acrescimos()}")
print(f"Total de descontos = {funcionario.getTotal_descontos()}")
print(f"Salário líquido = {funcionario.getSalario_liquido()}")


