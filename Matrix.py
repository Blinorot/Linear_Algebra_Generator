import Matrix_generators.py


class MatrixForm(object):
    def __init__(self, **flags):
        self.form = flags["form"]
        if (form == "FirstElementary"):
            self.data = gen_FirstElementary(flags["size"])
        if (form == "Secondlementary"):
            self.data = gen_SecondElementary(flags["size"])
        if (form == "ThirdElementary"):
            self.data = gen_ThirdElementary(flags["size"])
        if (form == "Invertible"):
            self.data = gen_InvertibleM(flags["size"])
        if (form == "Permutation"):
            self.data = gen_PermutationM(flags["size"])
