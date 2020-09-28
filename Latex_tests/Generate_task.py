from Header import *
from Random_new import *
from Matrix_new import *
from Matrix_generators_new import *


def First_task():
    WorkPlace = pl.base_classes.Environment()
    # doc.append(pl.NoEscape('\item'))
    R = Random(-5, 5)
    A_gen = MatrixForm(form='Invertible', size=3, bound=5, random=R)
    WorkPlace.append('Let A = ')
    WorkPlace.append(pl.Matrix(A_gen()))
    WorkPlace.append('. Find such B, that AB = E')
    WorkPlace.append('\n\n')
    return WorkPlace


def Second_task():
    WorkPlace = pl.base_classes.Environment()
    # doc.append(pl.NoEscape('\item'))
    R = Random(-5, 5)
    A_gen = MatrixForm(form='Invertible', size=3, bound=5, random=R)
    WorkPlace.append('Find such B, that AB = E if:')
    WorkPlace.append(pl.Math(data=['A =', pl.Matrix(A_gen())]))
    WorkPlace.append('\n\n')
    return WorkPlace


if __name__ == '__main__':
    doc = pl.Document(documentclass='article',
                      geometry_options={"margin": "0.71in"})

    header = pl.PageStyle("header")
    with header.create(pl.Head("C")):
        header.append(pl.Command('footnotesize'))
        header.append(pl.Command('noindent'))
        '''
        Does the same as written below but too big
        header.append(pl.Command('makebox',
                                 arguments=pl.NoEscape(
                                     'Linear Algebra and Geometry \hfill FCS HSE, 2020/2021, Math+'),
                                 options=pl.Command('textwidth')))
        '''
        header.append("Linear Algebra and Geometry")
        header.append(pl.Command('hfill'))
        header.append('FCS HSE, 2020/2021, Math+')
    name_header = pl.Center()
    name_header.append(pl.utils.bold('\nIndividual hometask'))
    group_header = pl.Center()
    index = 1
    group_header.append('Group 202. Variant ' + str(index))

    doc.preamble.append(header)
    doc.change_document_style("header")
    doc.append(name_header)
    doc.append(group_header)

    with doc.create(pl.Enumerate()) as enum:
        # workplace.append(First_task(doc))
        # workplace.append(First_task(doc))
        # doc.append(pl.Command('end', arguments='enumerate'))
        enum.add_item(First_task())
        enum.add_item(Second_task())
    doc.generate_pdf()
