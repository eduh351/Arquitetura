import json
import time
from unittest import TestCase
import unittest
import requests
parar_no_primeiro_erro = False


class Pokemon:

    def __init__(self, nome):
        self.nome = nome

    def info_pokemon(self):
        endereco = "https://pokeapi.co/api/v2/pokemon/"
        response = requests.get(endereco)
        return response.json()

    def __repr__(self):
        return '<Pokemon: {}>'.format(self.nome)


class Testes(TestCase):
    def teste_dowload(self):
        start = time.time()
        pokemon = Pokemon("Teste")
        resultado = pokemon.info_pokemon()
        with open('pokemon.json', 'w') as json_file:
            json.dump(resultado, json_file)
        end = time.time()
        execution_time = end - start
        print("%0.3f ms" % (execution_time * 1000.))
        self.assertIsNotNone(resultado)
        self.assertIsInstance(resultado, dict)

    def teste_nome_pokemon(self):
        start = time.time()
        pokemon = Pokemon("Teste")
        resultado = pokemon.info_pokemon()
        end = time.time()
        execution_time = end - start
        print("%0.3f ms" % (execution_time * 1000.))
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado
                         ['results'][0]['name'], 'bulbasaur')

    def teste_nome_pokemon2(self):
        start = time.time()
        pokemon = Pokemon("Teste")
        resultado = pokemon.info_pokemon()
        end = time.time()
        execution_time = end - start
        print("%0.3f ms" % (execution_time * 1000.))
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado
                         ['results'][1]['name'], 'ivysaur')


def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Testes)
    unittest.TextTestRunner(
        verbosity=2, failfast=parar_no_primeiro_erro).run(suite)


if __name__ == "__main__":
    runTests()
