from die import StandardDie


class Maze:
    def __init__(self, name, rows, columns, starting_row, starting_column, 
            die_top, die_front, row_data):
        self.name = name.rstrip()
        self.rows = rows
        self.columns = columns
        self.position = [starting_row, starting_column]
        self.die = StandardDie(top=die_top, front=die_front)

    def __repr__(self):
        return "<{}x{} Maze '{}' @ r:{}, c:{}>".format(self.rows, self.columns,
                self.name, self.position[0], self.position[1])


def main():
    with open('./data/sample_maze.txt') as f:
        name = f.readline()
        starting_params = map(int, f.readline().split())
        row_data = [map(int, f.readline().split()) 
                for x in range(starting_params[0])]
        M = Maze(name, *starting_params, row_data=row_data)
        print(M)


if __name__=="__main__":
    main()
