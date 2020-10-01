import sys

from Header import *
from Random_new import *
from Matrix_new import *
from Matrix_generators_new import *
import First_task
import Second_task
import Third_task
import Forth_task
import Fifth_task


def Add_variant(doc, name, surname, group, index, tasks):
    if (index > 1):
        doc.append(pl.NewPage())

    page_header = pl.PageStyle("header")
    with page_header.create(pl.Head("C")):
        page_header.append(pl.Command('footnotesize'))
        # page_header.append(pl.Command('noindent'))
        page_header.append("Линейная алгебра и геометрия")
        page_header.append(pl.Command('hfill'))
        page_header.append('ФКН НИУ ВШЭ, 2020/2021, Пилотный поток, М+')

    main_header = pl.Center()
    main_header.append(pl.utils.bold('Индивидуальное Домашнее Задание'))

    variant_header = pl.Center()
    variant_header.append('Вариант №' + str(index))

    name_header = pl.Center()
    name_header.append(name + ' ' + surname)

    group_header = pl.Center()
    group_header.append('Группа БПМИ' + group)

    doc.preamble.append(page_header)
    doc.change_document_style("header")
    doc.append(main_header)
    doc.append(variant_header)
    doc.append(name_header)
    doc.append(group_header)

    enum = pl.Enumerate()
    for task in tasks:
        # index from 1 to amount, list from 0 to amount - 1
        enum.add_item(task(index - 1))
    doc.append(enum)


if __name__ == '__main__':
    doc = pl.Document(
        documentclass='article',
        inputenc='utf8',
        fontenc='T2A',
        textcomp=True,
        geometry_options={"margin": "0.71in"})
    doc.packages.append(pl.Package('babel', options=['english', 'russian']))
    doc.preamble.append(pl.Command('selectlanguage', 'russian'))

    tasks = []
    # 90 - is amount of variants
    amount = 90
    tasks.append(First_task.First_task(amount))
    tasks.append(Second_task.Second_task(amount))
    tasks.append(Third_task.Third_task(amount))
    tasks.append(Forth_task.Forth_task(amount))
    tasks.append(Fifth_task.Fifth_task(amount))

    index = 1
    for line in sys.stdin.readlines():
        name, surname, group = line.split()
        Add_variant(doc, name, surname, group, index, tasks)
        index += 1
    while (index <= amount):
        name, surname, group = ["None", "None", "None"]
        Add_variant(doc, name, surname, group, index, tasks)
        index += 1

    doc.generate_pdf()
