import collections


class StandardDie:
    def __init__(self):
        # Reading from opposite face and moving right
        self.xaxis = collections.deque([6, 5, 1, 2])
        # Reading from opposite face and moving upward
        self.yaxis = collections.deque([6, 3, 1, 4])

    def info(self):
        return {'x': list(self.xaxis), 'y': list(self.yaxis)}

    def __repr__(self):
        return "<StandardDie ({})>".format(self.face())

    def __str__(self):
        return """
            _____
            |   |
            | {5} |
     _______|___|___
    |   |   |   |   |
    | {2} | {3} | {0} | {1} |
    |___|___|___|___|
            |   |
            | {4} |
            |___|
        """.format(self.xaxis[0], self.xaxis[1], self.xaxis[2], self.xaxis[3],
                self.yaxis[3], self.yaxis[1])

    def tip(self, direction):
        """Tip (roll to adjacent edge) the die in the specified direction

        directions: forward, backward, left, right

        >>> D2.tip('right')
        >>> D2.info()
        {'y': [2, 3, 5, 4], 'x': [2, 6, 5, 1]}
        >>> D2.tip('right')
        >>> D2.tip('right')
        >>> D2.tip('right')
        >>> D2.info()
        {'y': [6, 3, 1, 4], 'x': [6, 5, 1, 2]}
        >>> D2.tip('forward')
        >>> D2.info()
        {'y': [4, 6, 3, 1], 'x': [4, 5, 3, 2]}

        """
        if direction == 'forward':
            self.yaxis.rotate(1)
            self.xaxis[0] = self.yaxis[0]
            self.xaxis[2] = self.yaxis[2]
        elif direction == 'backward':
            self.yaxis.rotate(-1)
            self.xaxis[0] = self.yaxis[0]
            self.xaxis[2] = self.yaxis[2]
        elif direction == 'left':
            self.xaxis.rotate(-1)
            self.yaxis[0] = self.xaxis[0]
            self.yaxis[2] = self.xaxis[2]
        elif direction == 'right':
            self.xaxis.rotate(1)
            self.yaxis[0] = self.xaxis[0]
            self.yaxis[2] = self.xaxis[2]
        else:
            raise Exception("Invalid direction parameter")

    def face(self):
        """ Returns the value on the face of the die """
        return self.xaxis[2]

    def opposite(self):
        """ Returns the value opposite the face of the die """
        return self.xaxis[0]


D1 = StandardDie()
D2 = StandardDie()

if __name__=="__main__":
    import doctest
    doctest.testmod()
