from Header import *
from Random_new import *
from Matrix_new import *
from Matrix_generators_new import *


class Third_task():

    def __init__(self, amount):
        self.variants = [None] * amount
        R = Random(-5, 5)
        A_gen = MatrixForm(form='Ranked', rows=3, columns=5, random=R)
        for i in range(amount):
            self.variants[i] = pl.base_classes.Environment()
            self.variants[i].append('Let A = ')
            self.variants[i].append(pl.Matrix(A_gen()))
            self.variants[i].append('. Find rank of A')
            self.variants[i].append('\n\n')

    def __call__(self, index):
        return self.variants[index]
