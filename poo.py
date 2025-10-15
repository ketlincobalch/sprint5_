class Paciente:
    def __init__(self, nome_paciente, idade, endereco_paciente, nome_mae):
        self.nome = nome_paciente
        self.idade = idade
        self.endereco = endereco_paciente
        self.nome_mae = nome_mae
        
    def __str__(self):
        return f'Paciente: {self.nome}, Idade: {self.idade}, Endereço: {self.endereco}, Nome da Mãe: {self.nome_mae}'
        
    def getDataNascimento(self):
        ano_nasc = 2025 - self.idade
        return ano_nasc
    
    def foiAtendido(self, atendido):
        if atendido:
            print(f'O paciente {self.nome} foi atendido')
        else:
            print(f'O paciente {self.nome} não foi atendido')
        
        

paciente1 = Paciente('Pedro', 33, 'Rua Espanha, 123', 'Ana')

print(paciente1.nome)
print(f'O ano de nascimento do Paciente {paciente1.nome} é {paciente1.getDataNascimento()}')
paciente1.foiAtendido(True)
print()

print(paciente1)
