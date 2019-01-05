def mann(bitmap, length, breadth, i, j):
    if i == length - 1 or j == breadth - 1 or i == 0 or j == 0:
        return False

    count = 0
    for a in range(i - 1, i + 2):
        for b in range(j - 1, j + 2):
            if (not (i == a and b == j)) and bitmap[a][b]:
                count += 1

    # loneliness or overcrowding
    if count % 3 == 1:
        return True
    else:
        return False
 
def conway(bitmap, length, breadth, i, j):
    # kill the edge case headaches
    if i == length - 1 or j == breadth - 1 or i == 0 or j == 0:
        return bitmap[i][j]

    count = 0
    for a in range(i - 1, i + 2):
        for b in range(j - 1, j + 2):
            if (not (i == a and b == j)) and bitmap[a][b]:
                count += 1

    # loneliness or overcrowding
    if count <= 2 or count >= 5:
        return False
    else:
        return True


