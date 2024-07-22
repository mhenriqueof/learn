from terrenos.quadrangular import TerrenoQuadrangular
from terrenos.retangular import TerrenoRetangular
from engenheiro import Engenheiro

engenheiro = Engenheiro('Tancredo')
terrenoQuadrangular = TerrenoQuadrangular(4)
terrenoRetangular = TerrenoRetangular(2, 3)

engenheiro.medir_area(terrenoQuadrangular)
engenheiro.medir_area(terrenoRetangular)

engenheiro.medir_perimetro(terrenoRetangular)
