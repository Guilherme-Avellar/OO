class Aluno:

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setSobrenome(self, sobrenome):
        self.sobrenome = sobrenome

    def getSobrenome(self):
        return self.sobrenome

    def getNomeCompleto(self):
        return self.nome + " " + self.sobrenome

    def setNota1(self, nota1):
        self.nota1 = nota1

    def getNota1(self):
        return self.nota1

    def setNota2(self, nota2):
        self.nota2 = nota2

    def getNota2(self):
        return self.nota2

    def getSomaNotas(self):
        return self.nota1 + self.nota2

    def getMediaNotas(self):
        return (self.nota1 + self.nota2) / 2



aluno = Aluno()
aluno.setNome("Joao")
aluno.setSobrenome("Reis")
aluno.setNota1(80)
aluno.setNota2(100)

aluno2 = Aluno()
aluno2.setNome("Ana")
aluno2.setSobrenome("Machado")
aluno2.setNota1(60)
aluno2.setNota2(80)

print(aluno.getNomeCompleto())
print(aluno.getSomaNotas())
print(aluno.getMediaNotas())
print()
print(aluno2.getNomeCompleto())
print(aluno2.getSomaNotas())
print(aluno2.getMediaNotas())