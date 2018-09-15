import numpy as np


class Matrix:
    """A matrix implementation based on numpy array"""

    def __init__(self, rows=None, cols=None):
        if cols is None:
            if isinstance(rows, (list, tuple)):
                self.rows = len(rows)
                self.cols = len(rows[0])
                self.items = np.array(rows)
            else:
                raise ValueError("Number of columns not provided.")
        else:
            if isinstance(rows, int) and isinstance(cols, int):
                self.rows = rows
                self.cols = cols
                self.items = np.zeros((self.rows, self.cols))
            else:
                raise ValueError("Rows and columns need to be integers.")

    @property
    def determinant(self):
        if self.cols != self.rows:
            raise ArithmeticError(
                "The matrix has to have an equal number of columns and rows")

        if self.cols == 2:
            return self.items[0][0] * self.items[1][1] - self.items[0][1] * self.items[1][0]
        elif self.cols == 3:
            matrices = {
                "a": Matrix([[self.items[1][1], self.items[1][2]], [self.items[2][1], self.items[2][2]]]),
                "b": Matrix([[self.items[1][0], self.items[1][2]], [self.items[2][0], self.items[2][2]]]),
                "c": Matrix([[self.items[1][0], self.items[1][1]], [self.items[2][0], self.items[2][1]]]),
            }
            dets = {k: matrices[k].determinant for k in matrices}

            return self.items[0][0] * dets["a"] - self.items[0][1] * self.items[0][2] * dets["b"] + dets["c"]
        else:
            return "Not implemented yet"

    def __str__(self):
        return str(self.items)

    def copy(self):
        matrix = Matrix(self.rows, self.cols)
        matrix.items = self.items.copy()
        return matrix
