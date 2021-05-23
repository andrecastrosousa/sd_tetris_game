class Tabuleiro:

    def __init__(self):
        self._locked_positions = {}
        self._shapes = []
        self._grid = [[(0, 0, 0) for x in range(10)] for x in range(20)]

    @property
    def locked_positions(self):
        return self._locked_positions

    @locked_positions.setter
    def locked_positions(self, locked_positions):
        self._locked_positions = locked_positions

    def create_grid(self):
        grid = [[(0, 0, 0) for x in range(10)] for x in range(20)]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (j, i) in self._locked_positions:
                    c = self._locked_positions[(j, i)]
                    grid[i][j] = c
        self._grid = grid
        return grid

    def clear_rows(self):
        # need to see if row is clear the shift every other row above down one

        inc = 0
        for i in range(len(self._grid) - 1, -1, -1):
            row = self._grid[i]
            if (0, 0, 0) not in row:
                inc += 1
                # add positions to remove from locked
                ind = i
                for j in range(len(row)):
                    try:
                        del self._locked_positions[(j, i)]
                    except:
                        continue
        if inc > 0:
            for key in sorted(list(self._locked_positions), key=lambda x: x[1])[::-1]:
                x, y = key
                if y < ind:
                    new_key = (x, y + inc)
                    self._locked_positions[new_key] = self._locked_positions.pop(key)

        return inc

    def valid_space(self, shape):
        accepted_positions = [[(j, i) for j in range(10) if self._grid[i][j] == (0, 0, 0)] for i in range(20)]
        accepted_positions = [j for sub in accepted_positions for j in sub]
        formatted = self.convert_shape_format(shape)

        for pos in formatted:
            if pos not in accepted_positions and pos[1] > -1:
                return False

        return True

    @staticmethod
    def convert_shape_format(shape):
        positions = []
        format_shape = shape.shape[shape.rotation % len(shape.shape)]

        for i, line in enumerate(format_shape):
            row = list(line)
            for j, column in enumerate(row):
                if column == '0':
                    positions.append((shape.x + j, shape.y + i))

        for i, pos in enumerate(positions):
            positions[i] = (pos[0] - 2, pos[1] - 4)

        return positions