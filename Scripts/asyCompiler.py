import glob
import os

for file in glob.glob("*.asy"):
    os.system("asy " + file)
