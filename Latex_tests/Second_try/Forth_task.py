from Header import *
from Random_new import *
from Matrix_new import *
from Matrix_generators_new import *


class Forth_task():

    def __init__(self, amount):
        self.variants = [None] * amount
        R = Random(-5, 5)
        A_gen = MatrixForm(form='SecondElementary', size=3, row=1, random=R)
        for i in range(amount):
            self.variants[i] = pl.base_classes.Environment()
            self.variants[i].append('Let A = ')
            self.variants[i].append(pl.Matrix(A_gen()))
            self.variants[i].append('. Which type of elementary matrix is it?')
            self.variants[i].append('\n\n')

    def __call__(self, index):
        return self.variants[index]
