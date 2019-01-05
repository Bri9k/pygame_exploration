def norule(bitmap, length, breadth, i, j):
        # no change in values in bitmap
        return bitmap[i][j]

class cellularAutomaton:

    """Rule is a function that takes bitmap, and returns nextbitmap[i][j] """
    def __init__(self, bitmap, rule = None):
        self.length = len(bitmap) # number of rows
        self.breadth = len(bitmap[0]) # number of columns
        self.bitmap = [bitmap[i][:] for i in range(len(bitmap))]
        if rule is None:
            self.rule = norule
        else:
            self.rule = rule

    def propagate(self, rule=None):
        if rule is None:
            rule = self.rule

        copyofbitmap = [[self.bitmap[i][j] for j in range(self.breadth)] for i in range(self.length)]

        for i in range(self.length):
            for j in range(self.breadth):
                self.bitmap[i][j] = rule(copyofbitmap, self.length, self.breadth, i, j)

    def cell(self, i, j):
        return self.bitmap[i][j]
