from PyQt5.QtWidgets import QStackedWidget, QLabel, QLineEdit

HIDDEN_MATRIX = "na"

class MatrixController:
    def __init__(self):
        self.matrix_fields = []

    def set_matriz_fields(self, matriz : list[list[QLineEdit]]):
        self.matrix_fields : list[list[QLineEdit]] = matriz

    def get_matriz_fields(self):
        return self.matrix_fields
    
    def get_matriz_values(self):
        values = []

        for row in self.matrix_fields:
            values_row = []

            for field in row:
                if(field.text() == HIDDEN_MATRIX):
                    continue

                try:
                    value = float(field.text())
                except ValueError:
                    value = 0.0

                values_row.append(value)

            if(len(values_row) > 0):
                values.append(values_row)

        return values
    
    def clear_matriz(self):
        for row in self.matrix_fields:
            for field in row:
                field.clear()

    def print_matriz(self):
        print("Matriz actual:")
        for row in self.get_matriz_values():
            print(row)

    def change_size(self, new_size: int):
        if(new_size == 2):
            # ocultar fila 2 y 3
            for j in range(5):
                self.matrix_fields[2][j].setText(HIDDEN_MATRIX)
                self.matrix_fields[3][j].setText(HIDDEN_MATRIX)

            # ocultar columna 2 y 3
            for i in range(4):
                self.matrix_fields[i][2].setText(HIDDEN_MATRIX)
                self.matrix_fields[i][3].setText(HIDDEN_MATRIX)

        elif(new_size == 3):
            self.clear_matriz()

            # ocultar la fila 4
            for j in range(5):
                self.matrix_fields[3][j].setText(HIDDEN_MATRIX)

            # ocultar la columna 4
            for i in range(4):
                self.matrix_fields[i][3].setText(HIDDEN_MATRIX)

        elif(new_size == 4):
            # mostrar todo
            self.clear_matriz()

        self.is_hidden_for_value()

    def set_size_to_default(self):
        self.change_size(4)

    def is_hidden_for_value(self):
        for i in range(4):
            for j in range(5):
                if self.matrix_fields[i][j].text() == HIDDEN_MATRIX:
                    self.matrix_fields[i][j].setVisible(False)
                else:
                    self.matrix_fields[i][j].setVisible(True)

    # Aquí puedes agregar métodos específicos para manejar la lógica relacionada con matrices
    # Por ejemplo, métodos para resolver sistemas de ecuaciones, realizar operaciones matriciales, etc.