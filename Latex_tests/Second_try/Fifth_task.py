from Header import *
from Random_new import *
from Matrix_new import *
from Matrix_generators_new import *


class Fifth_task():

    def __init__(self, amount):
        self.variants = [None] * amount
        R = Random(-5, 5)
        L_gen = MatrixForm(form='Upper', size=3, type="Uni", random=R)
        U_gen = MatrixForm(form='Upper', size=3, type="OneZero", random=R)
        for i in range(amount):
            self.variants[i] = pl.base_classes.Environment()
            self.variants[i].append('Let L = ')
            self.variants[i].append(pl.Matrix(L_gen()))
            self.variants[i].append('U = ')
            self.variants[i].append(pl.Matrix(U_gen().T))
            self.variants[i].append('. Find LU')
            self.variants[i].append('\n\n')

    def __call__(self, index):
        return self.variants[index]
