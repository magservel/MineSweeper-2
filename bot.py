import random

#TODO: Have a propoer initiation
#TODO: Compute next move at receiving data from back


class Bot:
    def __init__(self):
        self.game_grid = []
        self.bot_grid = []
        self.count_of_mine = 0
        self.nb_rows = 0
        self.nb_columns = 0
        pass

    def __str__(self):
        return "Count of mines : " + str(self.count_of_mine)

    def update_game_grid(self, request_json):
        self.game_grid = request_json['data']
        self.count_of_mine = int(request_json['countOfMines'])
        self.nb_rows = int(request_json['columns'])
        self.nb_columns = int(request_json['rows'])

    def update_bot_grid(self, request_json):
        # For every case
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                #print 'Update case'
                pass

    def click_grid(self, request_json):
        self.update_game_grid(request_json)
        self.update_bot_grid(request_json)
        result = request_json
        c_x, c_y = self.compute_next_move()

        result['clickedX'] = c_x
        result['clickedY'] = c_y
        return result

    def compute_next_move(self):
        c_x = random.randint(0, self.nb_columns - 1)
        c_y = random.randint(0, self.nb_rows - 1)
        print '1: ', c_x, ' ', c_y

        while not bool(self.game_grid[c_x][c_y]['clickable']):
            c_x = random.randint(0, self.nb_columns - 1)
            c_y = random.randint(0, self.nb_rows - 1)
            print '2    : ', c_x, ' ', c_y

        return c_x, c_y

    def get_neighboors(self):
        pass