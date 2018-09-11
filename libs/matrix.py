class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.items = [[0] * self.cols for i in range(self.rows)]

    def __str__(self):
        strMatrix = ""
        for row in range(self.rows):
            for col in range(self.cols):
                strMatrix += "{} ".format(self.items[row][col])
            strMatrix += "\n"
        return strMatrix