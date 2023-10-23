from math_stuff import *
from manim import *

class vectorPrueba(LinearTransformationScene):

    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            leave_ghost_vectors=True,
        )


    def construct(self):
        #splane = NumberPlane()
        #v_1 = Vector([1,1])
        #v_2 = Vector([-2,1])
        #self.add(plane, v_1, v_2)

        matrix = [[1/2, -1], [1, 1]]

        self.apply_matrix(matrix)
        self.wait()