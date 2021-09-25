import calculadclasses
from unittest import TestCase
import unittest
parar_no_primeiro_erro = False


class Testes(TestCase):
    def test_soma1(self):
        calculo1 = calculadclasses.Calculadora()
        result = calculo1.calcular(3, 5, "soma")
        self.assertEqual(result, 8)

    def test_soma2(self):
        calculo2 = calculadclasses.Calculadora()
        result = calculo2.calcular(10, 5, "soma")
        self.assertEqual(result, 15)

    def test_soma3(self):
        calculo3 = calculadclasses.Calculadora()
        result = calculo3.calcular(25, 10, "soma")
        self.assertEqual(result, 35)

    def test_soma4(self):
        calculo4 = calculadclasses.Calculadora()
        result = calculo4.calcular(8, 5, "soma")
        self.assertEqual(result, 13)

    def test_soma5(self):
        calculo5 = calculadclasses.Calculadora()
        result = calculo5.calcular(100, 50, "soma")
        self.assertEqual(result, 150)

    def test_soma6_operador(self):
        calculo5 = calculadclasses.Calculadora()
        result = calculo5.calcular(21, 50, "Soma")
        self.assertEqual(result, 0)

    ####################################################
    def test_subtracao1(self):
        calculo1 = calculadclasses.Calculadora()
        result = calculo1.calcular(3, 5, "subtracao")
        self.assertEqual(result, -2)

    def test_subtracao2(self):
        calculo2 = calculadclasses.Calculadora()
        result = calculo2.calcular(10, 5, "subtracao")
        self.assertEqual(result, 5)

    def test_subtracao3(self):
        calculo3 = calculadclasses.Calculadora()
        result = calculo3.calcular(25, 10, "subtracao")
        self.assertEqual(result, 15)

    def test_subtracao4(self):
        calculo4 = calculadclasses.Calculadora()
        result = calculo4.calcular(8, 5, "subtracao")
        self.assertEqual(result, 3)

    def test_subtracao5(self):
        calculo5 = calculadclasses.Calculadora()
        result = calculo5.calcular(100, 50, "subtracao")
        self.assertEqual(result, 50)

    def test_subtracao6_operador(self):
        calculo5 = calculadclasses.Calculadora()
        result = calculo5.calcular(20, 15, "menos")
        self.assertEqual(result, 0)

    def test_subtracao7_operador(self):
        calculo5 = calculadclasses.Calculadora()
        result = calculo5.calcular(21, 50, "sutracao")
        self.assertEqual(result, 0)

    ########################################################
    def test_multiplicacao1(self):
        calculo1 = calculadclasses.Calculadora()
        result = calculo1.calcular(3, 5, "multiplicacao")
        self.assertEqual(result, 15)

    def test_multiplicacao2(self):
        calculo2 = calculadclasses.Calculadora()
        result = calculo2.calcular(10, 5, "multiplicacao")
        self.assertEqual(result, 50)

    def test_multiplicacao3(self):
        calculo3 = calculadclasses.Calculadora()
        result = calculo3.calcular(25, 10, "multiplicacao")
        self.assertEqual(result, 250)

    def test_multiplicacao4(self):
        calculo4 = calculadclasses.Calculadora()
        result = calculo4.calcular(8, 5, "multiplicacao")
        self.assertEqual(result, 40)

    def test_multiplicacao5(self):
        calculo5 = calculadclasses.Calculadora()
        result = calculo5.calcular(100, 50, "multiplicacao")
        self.assertEqual(result, 5000)

    def test_multiplicacao6_operador(self):
        calculo5 = calculadclasses.Calculadora()
        result = calculo5.calcular(21, 50, "vezes")
        self.assertEqual(result, 0)

    ###################################################
    def test_divisao(self):
        calculo1 = calculadclasses.Calculadora()
        result = calculo1.calcular(15, 5, "divisao")
        self.assertEqual(result, 3)

    def test_divisao2(self):
        calculo2 = calculadclasses.Calculadora()
        result = calculo2.calcular(10, 5, "divisao")
        self.assertEqual(result, 2)

    def test_divisao3(self):
        calculo3 = calculadclasses.Calculadora()
        result = calculo3.calcular(25, 10, "divisao")
        self.assertEqual(result, 2.5)

    def test_divisao4(self):
        calculo4 = calculadclasses.Calculadora()
        result = calculo4.calcular(18, 3, "divisao")
        self.assertEqual(result, 6)

    def test_divisao5(self):
        calculo5 = calculadclasses.Calculadora()
        result = calculo5.calcular(100, 50, "divisao")
        self.assertEqual(result, 2)

    def test_divisao6_operador(self):
        calculo5 = calculadclasses.Calculadora()
        result = calculo5.calcular(50, 2, "dividido")
        self.assertEqual(result, 0)

    def test_divisao7_operador(self):
        calculo5 = calculadclasses.Calculadora()
        result = calculo5.calcular(32, 16, "por")
        self.assertEqual(result, 0)


def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Testes)
    unittest.TextTestRunner(
        verbosity=2, failfast=parar_no_primeiro_erro).run(suite)


if __name__ == '__main__':
    runTests()
