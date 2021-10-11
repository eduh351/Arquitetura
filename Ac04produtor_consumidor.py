# Eduardo Rodrigues da Silva RA: 1903171

from threading import Thread, Condition

import time

import random

vitrine = []

condition = Condition()

class Fabrica(Thread):

    def run(self):

        pecas = ["Blusa", "Calça", "Meia", "Teniz", "Bermuda", "Boné", "Cinto", "Sandália"]

        global vitrine

        while True:
            pecaItem = random.choice(pecas)

            condition.acquire()

            vitrine.append(pecaItem)

            print(f"Repondo peça {pecaItem} na loja ")

            condition.notify()

            condition.release()

            time.sleep(3)

class Loja(Thread):

    def run(self):

        global vitrine
        while True:

            condition.acquire()

            if not vitrine:

                print ("Vitrines da loja vazias ...")

                condition.wait()

            pecaItem = vitrine.pop(0)

            print("Cliente comprou peça ", pecaItem)

            condition.release()

            time.sleep(3)
Fabrica().start()

Loja().start()
