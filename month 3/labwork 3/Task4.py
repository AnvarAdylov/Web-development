class Checker:
    def __init__(self, field):
        self.field = field

    def did_i_win(self):
        return self.check_win()

    def search(self, field):
        filled = []
        for i in range(len(field)):
            for j in range(len(field[i])):
                if field[i][j] != ' ' and field[i][j] == self.symbol:
                    filled.append([i, j])
        return filled

    def check_win(self):
        for row in self.field.gamefield:
            if all(cell == row[0] for cell in row) and row[0] != '_':
                return True
        for col in range(len(self.field.gamefield[0])):
            if (all(row[col] == self.field.gamefield[0][col]
                    for row in self.field.gamefield) and
                    self.field.gamefield[0][col] != '_'):
                return True
        if (all(self.field.gamefield[i][i] ==
                self.field.gamefield[0][0] for i in
                range(len(self.field.gamefield))) and
                self.field.gamefield[0][0] != '_'):
            return True
        if (all(self.field.gamefield[i][len(self.field.gamefield)
                - 1 - i] == self.field.gamefield[0][len(self.field.gamefield)
                - 1] for i in range(len(self.field.gamefield))) and
                self.field.gamefield[0][len(self.field.gamefield) - 1] != '_'):
            return True

        return False

    def check_segments(self):
        if len(self.field.gamefield) > 5:
            segments = self.generate_segments(self.field.gamefield)
            for segment in segments:
                checker = Checker(segment)
                if checker.check_win_static(segment):
                    return True
        return False

    @staticmethod
    def generate_segments(matrix, segment_size=5):
        segments = []
        num_segments_row = len(matrix[0]) - segment_size + 1
        num_segments_col = len(matrix) - segment_size + 1

        if num_segments_row <= 0 or num_segments_col <= 0:
            raise ValueError("Segment size is too large for the given matrix")

        for i in range(num_segments_col):
            for j in range(num_segments_row):
                segment = [row[j:j + segment_size]
                           for row in matrix[i:i + segment_size]]
                segments.append(segment)

        return segments

    @staticmethod
    def check_win_static(field):
        for row in field:
            if all(cell == row[0] for cell in row) and row[0] != '_':
                return True
        for col in range(len(field[0])):
            if (all(row[col] == field[0][col] for row in field) and
                    field[0][col] != '_'):
                return True
        if (all(field[i][i] == field[0][0] for i in range(len(field))) and
                field[0][0] != '_'):
            return True
        if (all(field[i][len(field) - 1 - i] == field[0][len(field) - 1]
                for i in range(len(field))) and
                field[0][len(field) - 1] != '_'):
            return True
        return False
