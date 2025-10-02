import unittest
import main
class TestMain(unittest.TestCase): 
  def test_verificar_aprovacao(self): 
    casos_de_teste = [ 
      (0, "Reprovado"), 
      (4, "Reprovado"), 
      (5, "Recuperação"), 
      (6, "Recuperação"), 
      (7, "Aprovado"), 
      (8, "Aprovado"), 
    ]
    for media, resultado_esperado in casos_de_teste:
      resultado_obtido = main.verificar_aprovacao(media)
      self.assertEqual(resultado_obtido, resultado_esperado, f"media: {media}")
  def test_calcular_media(self):
    casos_de_teste = [
    #   (nota1, nota2, media)
        (0, 0, 0),
        (10, 0, 5),
        (10, 10, 10),
        (5, 5, 5),
        (8, 2, 5),
        (7, 3, 5),
    ]    
    for nota1, nota2, resultado_esperado in casos_de_teste:
        resultado_obtido = main.calcular_media(nota1, nota2)
        self.assertEqual(resultado_obtido, resultado_esperado, f"nota1: {nota1}, nota2: {nota2}")
 
if __name__ == '__main__': unittest.main()

# NESTE EXEMPLO ESTAMOS CRIANDO TRESTES POR MEIO DA DEFINIÇÃO DE UMA CLASSE DE HERDA DE 'UNITTEST.TESTCASE'
# Ai implementamos métodos que representam testes individuais que sao executados individualmente plea sferramentas ao invocar unittest.main()
#Aqui estamos criando uma classe para testar as funções definidas dentro do aquivoY
#Estamos testando agora o "validar_aprovacao;
#no codigo temos as tuplas, cada tupla é percorrida, os casos sao percorridos. Vamos percorrer cada um dos casos de teste e verificar se o resultado da execução de "validar_aprovacao" correspondee ao esperado utilizando o método "assertEqual".
#Caso o teste de rrado ele sera interrompido e marca o teste como falho.