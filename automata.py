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
            self.bitmap1 = json.loads(json_str)
            self.bitmap2 = json.loads(json_str)
            print("Loaded:")
            print(self.bitmap1)
            fp.close()



