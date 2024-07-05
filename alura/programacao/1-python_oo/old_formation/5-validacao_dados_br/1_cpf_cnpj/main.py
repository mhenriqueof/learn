from cpf_cnpj import Document

cpf  = '10086316982'
cnpj = '35379838000112'

# cpf_1  = CpfCnpj('cpf', cpf)
cnpj_1 = Document.create_doc(cpf)

# print(cpf_1)
print(cnpj_1)
