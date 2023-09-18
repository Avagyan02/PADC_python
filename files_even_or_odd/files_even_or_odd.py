import os
from datetime import datetime


def homework():
    path = os.getcwd() + "/test"

    if (not os.path.isdir(path)):
        os.mkdir(path)

    for i in range(10):
        now = datetime.now()
        dt_string = now.strftime("%d_%m_%Y_%H_%M_%S_%f")
        miliseconds = dt_string.split('_')[-1]

        if (int(miliseconds) % 2 == 0):
            with open(path + "/" + dt_string + ".txt", "x") as f:
                f.write("Status = true\n")
        else:
            with open(path + "/" + dt_string + ".txt", "x") as f:
                f.write("Status = false\n")


homework()