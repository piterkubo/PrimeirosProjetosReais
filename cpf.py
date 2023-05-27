from validate_docbr import CPF

class DOC:

    def __init__(self, cpf):
        self.cpf = str(cpf)
        self.quantidade = 11

    ''' def formatar(self):
    format1 = self.cpf[:3]
    format2 = self.cpf[3:6]
    format3 = self.cpf[6:9]
    format4 = self.cpf[9:]
    return f'{format1}.{format2}.{format3}-{format4}'''


    def validar(self):
        cpf = CPF()
        print(cpf.validate(self.cpf))
        print(cpf.mask(self.cpf))


        if self.quantidade == len(self.cpf):

            print('CPF Valido!!!')

        else:
            raise ValueError('Dados invalidos')

        return f'{cpf.mask(self.cpf)}'


    def __str__(self):
        return f'O numero de CPF {self.validar()} esta nos padrões'






