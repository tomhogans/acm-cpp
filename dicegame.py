class StandardDie:
    def __init__(self):
        self.values = [5, 1, 3] # (top, front, right)

    def info(self):
        return dict(top=self.values[0], front=self.values[1], 
                right=self.values[2])

    def __repr__(self):
        return "<StandardDie ({})>".format(self.face())

    def __str__(self):
        return """
            _____
            |   |
            | {2} |
     _______|___|___
    |   |   |   |   |
    | {1} | {3} | {4} | {0} |
    |___|___|___|___|
            |   |
            | {5} |
            |___|
        """.format(self.values[0], self.values[1], self.values[2], 
                (7 - self.values[0]), (7 - self.values[1]), 
                (7 - self.values[2]))

    def tip(self, direction):
        """Tip (roll to adjacent edge) the die in the specified direction

        directions: front, back, left, right

        >>> D2.tip('right')
        >>> D2.info()
        {'front': 1, 'top': 4, 'right': 5}
        >>> D2.tip('right')
        >>> D2.tip('right')
        >>> D2.info()
        {'front': 1, 'top': 3, 'right': 2}
        >>> D2.tip('front')
        >>> D2.info()
        {'front': 3, 'top': 6, 'right': 2}

        """
        # Unpack values to local variables
        top, front, right = self.values

        if direction == 'front':
            top, front = (7 - front), top
        elif direction == 'back':
            top, front = front, (7 - top)
        elif direction == 'left':
            top, right = right, (7 - top)
        elif direction == 'right':
            top, right = (7 - right), top
        else:
            raise Exception("Invalid direction parameter")

        # Apply changed values
        self.values = [top, front, right]

    def face(self):
        """ Returns the value on the face of the die """
        return self.values[1]

    def opposite(self):
        """ Returns the value opposite the face of the die """
        return 7 - self.face()


D1 = StandardDie()
D2 = StandardDie()

if __name__=="__main__":
    import doctest
    doctest.testmod()
