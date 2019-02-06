import random

cont = True
k = 3

nos = [i for i in range(2 ** k)]
while cont and len(nos) > 0:
    rind = random.randrange(len(nos))
    print(str(nos[rind]))
    ip = input()
    if ip == "q":
        cont = False
    else:
        bincorr = str(format(nos[rind], '0' + str(k) + 'b'))
        if bincorr == ip:
            nos.pop(rind)
        else:
            print("Wrong! Correct representation is " + bincorr)

print("You got them all right!")
