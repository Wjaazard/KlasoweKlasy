class Figure:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b


class Kwadrat(Figure):
    def __init__(self, a):
        self.pole = a * a
        super().__init__(self.pole)


class Prostokat(Figure):
    def __init__(self, a, b):
        self.pole = a * b
        super().__init__(self.pole)


class Pieciokat(Figure):
    def __init__(self, a):
        self.pole = a * a * a * a
        super().__init__(self.pole)

class mainProgram:
    def __init__(self):
        self. figures_list = list()
        self.figures_list.append(Kwadrat(4))
        self.figures_list.append(Prostokat(4, 5))
        self.figures_list.append(Pieciokat(6))
    def oblicz_sume(self):
        return sum(f.pole for f in self.figures_list)


if __name__ == "__main__":
    program = mainProgram()
    print(program.oblicz_sume())
