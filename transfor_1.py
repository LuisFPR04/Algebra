from math_stuff import *
from manim import *
from numpy import sqrt

class vectorPrueba(LinearTransformationScene):

    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            show_basis_vectors=False,
            include_background_plane=False
        )


    def construct(self):

        dot_1 = Dot(point=RIGHT + UP)
        dot_2 = Dot(point=2*RIGHT + 2*UP)
        self.add_moving_mobject(dot_1)
        self.add_moving_mobject(dot_2)

        matrix = rotation(-3*np.pi/2)

        self.apply_matrix(matrix)
        self.wait()

#print(type(LEFT))