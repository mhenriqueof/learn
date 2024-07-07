from modulos import Casa, Pessoa

casa_tancredo = Casa()
tancredo = Pessoa('Tancredo')

tancredo.set_local(casa_tancredo)
casa_tancredo.set_proprietario(tancredo)

proprietario = casa_tancredo.get_proprietario()
proprietario.se_apresentar()

tancredo.apresentar_local()
