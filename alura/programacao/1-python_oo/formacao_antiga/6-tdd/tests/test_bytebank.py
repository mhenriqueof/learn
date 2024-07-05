from codigo.bytebank import Funcionario
import pytest

def then(a, b):
    
    assert a == b    
    

class TestClass:
    
    # Given-When-Then
    
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        
        entry = '10/12/2000' # Given
        expect = 23 
        
        test_age = Funcionario('Test', entry, 1000)
        result = test_age.idade() # When - momento de uma ação executada
        
        assert result == expect # Then
        

    def test_quando_nome_recebe_Henrique_Oliveira_deve_retornar_Oliveira(self):
        
        entry = 'Henrique Oliveira'
        expect = 'Oliveira'

        test_name = Funcionario(entry, '10/12/2000',  1000)
        result = test_name.sobrenome()

        assert result == expect # Then
    
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        
        entry_salary = 100000
        entry_name = 'Paulo Bragança'
        expect = 90000
        
        test_salary = Funcionario(entry_name, '11/11/2011', entry_salary)
        test_salary.decrescimo_salario()
        
        result = test_salary.salario
        
        assert result == expect
        
    @pytest.mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        
        entry_salary = 1000
        expect = 100
        
        test_bonus = Funcionario('Tester', '10/10/2000', entry_salary)
        test_bonus.calcular_bonus()
        
        result = test_bonus.calcular_bonus()
        
        assert result == expect

    @pytest.mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_10000000_deve_retornar_exception(self):
        
        with pytest.raises(Exception):
            
            entry = 10000000
            test = Funcionario('test', '10/10/2000', entry)
            resultado = test.calcular_bonus()

            assert resultado
            
