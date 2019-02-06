import os
import json

def norule(bitmap, length, breadth, i, j):
        # no change in values in bitmap
        return bitmap[i][j]

class cellularAutomaton:

    def __init__(self, bitmap, rule = None):

        """Rule is a function that takes bitmap, and returns nextbitmap[i][j] """
        self.length = len(bitmap) # number of rows
        self.breadth = len(bitmap[0]) # number of columns

        self.bitmap1 = [bitmap[i][:] for i in range(len(bitmap))]
        self.bitmap2 = [bitmap[i][:] for i in range(len(bitmap))]

        self.first = True

        if rule is None:
            self.rule = norule
        else:
            self.rule = rule

    def currbitmap(self):
        """ Returns the active bitmap (the one to be shown to public)"""
        if self.first:
            return self.bitmap1
        else:
            return self.bitmap2

    def swapmap(self):
        """ Returns the inactive bitmap """
        if self.first:
            return self.bitmap2
        else:
            return self.bitmap1

    def propagate(self, rule=None):
        """ Applies rule to automaton. If no rule specified, uses the rule specified in constructor"""
        if rule is None:
            rule = self.rule

        seed = self.currbitmap()
        canvas = self.swapmap()

        for i in range(self.length):
            for j in range(self.breadth):
                canvas[i][j] = rule(seed, self.length, self.breadth, i, j)

        # flip canvas and seed
        self.first = not self.first

    def cell(self, i, j):
        """ Returns ijth cell of automaton """
        canvas = self.currbitmap()
        return canvas[i][j]
    
    def savefile_handler(self, filename):
        """ Saves current active bitmap to <filename>"""
        bitmap = self.currbitmap()

        if os.path.isfile(filename):
            os.remove(filename)
    
        fp = open(filename, "w")

        fp.write(json.dumps(bitmap))

    def read_saved(self, filename):
        """ Loads json bitmap stored in filename to both active and inactive bitmaps"""
        if os.path.isfile(filename):
            fp = open(filename, "r")
            json_str = fp.read()
            fp.close()
            self.bitmap1 = json.loads(json_str)
            self.bitmap2 = json.loads(json_str)


# several functions that can be used for demonstration

def mann(bitmap, length, breadth, i, j):
    """ From max mann's video """
    if i == length - 1 or j == breadth - 1 or i == 0 or j == 0:
        return 0

    count = 0
    for a in range(i - 1, i + 2):
        for b in range(j - 1, j + 2):
            if (not (i == a and b == j)) and bitmap[a][b] == 1:
                count += 1

    # loneliness or overcrowding
    if count % 3 == 1:
        return 1
    else:
        return 0
 
def conway(bitmap, length, breadth, i, j):
    """Conway's game of life"""
    # kill the edge case headaches
    if i == length - 1 or j == breadth - 1 or i == 0 or j == 0:
        return bitmap[i][j]

    count = 0
    for a in range(i - 1, i + 2):
        for b in range(j - 1, j + 2):
            if (not (i == a and b == j)) and bitmap[a][b] == 1:
                count += 1

    # loneliness or overcrowding
    if count <= 2 or count >= 5:
        return 0
    else:
        return 1

def blue_cells(bitmap, length, breadth, i, j):
    """ From max mann's video """

    # 35 35 works great with this

    if i == length - 1 or j == breadth - 1 or i == 0 or j == 0:
        return 0

    count = 0
    for a in range(i - 1, i + 2):
        for b in range(j - 1, j + 2):
            if (not (i == a and b == j)) and bitmap[a][b] > 0:
                count += 1

    # loneliness or overcrowding
    if i == length // 2 or j == breadth // 2:
        return 10
    elif count >= 2 and count <= 5 and bitmap[i][j] < 235:
        return bitmap[i][j] + 20
    else:
        return 0
