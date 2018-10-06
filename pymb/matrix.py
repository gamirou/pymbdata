import numpy as np

class Matrix:
    """A matrix implementation based on numpy array
    
    Features:
    * It is immutable (as the numpy array) (TODO: Thinking of scraping numpy),
    * When initialized, all values are set to 0

    Methods
    * To replace a value, use matrix[row, col] = value,
    * To get a value, use matrix[row][col] or matrix[row, col],
    * To get the determinant, use matrix.determinant (2x2 and 3x3),
    * To check if it is symmetric, use matrix.is_symmetric() -> True/False,
    * To transpose current matrix, use matrix.transposed(),
    * To get a new transposed matrix, use matrix.transpose()
    """

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

        self.__setvalcounter = 0

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

    def __setitem__(self, key, val):
        """It only works like this m[0, 0] and not this m[0][0]"""
        (row, col) = key
        self.items[row, col] = val

    def __getitem__(self, value):
        """It works both ways, m[0][0] and m[0, 0]"""
        if isinstance(value, tuple):
            return self.items[value[0]][value[1]]
        else:
            # Less efficient
            return self.items[value]

    def __str__(self):
        return str(self.items)

    def copy(self):
        """Returns a copy of itself"""
        matrix = Matrix(self.rows, self.cols)
        matrix.items = self.items.copy()
        return matrix

    def transpose(self):
        """Returns a new transposed matrix"""
        if self.rows != self.cols:
            raise ValueError("Your matrix has to have the same number of rows and columns.")
        
        transposed = Matrix(self.rows, self.cols)
        for i in range(self.rows): 
            for j in range(self.cols): 
                transposed.items[i][j] = self.items[j][i]

        return transposed

    def transposed(self):
        """Transposes the current matrix"""
        self = self.transpose()

    def is_symmetric(self):
        if self.rows != self.cols:
            raise ValueError("Your matrix has to have the same number of rows and columns.")
        
        transposed = self.transpose()
        for i in range(self.rows): 
            for j in range(self.cols): 
                if transposed.items[i][j] != self.items[i][j]:
                    return False

        return True