import random


class Bot:
    def __init__(self):
        self.grid = []
        self.count_of_mine = 0
        self.nb_rows = 0
        self.nb_columns = 0
        pass

    def __str__(self):
        return "Count of mines : " + str(self.count_of_mine)

    def click_grid(self, request_json):
        self.update_data(request_json['data'], int(request_json['countOfMines']), int(request_json['columns']), int(request_json['rows']))
        print 'Bot: ', self
        result = request_json
        c_x, c_y = self.compute_next_case(request_json['data'], int(request_json['columns']), int(request_json['rows']))

        result['clickedX'] = c_x
        result['clickedY'] = c_y
        return request_json

    def compute_next_case(self, grid_data, nb_colums, nb_rows):
        c_x = 0
        c_y = 0
        while not bool(self.grid[c_y][c_x]['clickable']):
            c_x = random.randint(0, nb_colums - 1)
            c_y = random.randint(0, nb_rows - 1)
        return c_x, c_y

    def update_data(self, grid, count_of_mine, rows, columns):
        self.grid = grid
        self.count_of_mine = count_of_mine
        self.nb_rows = rows
        self.nb_columns = columns

    def get_neighboors(self):
        pass