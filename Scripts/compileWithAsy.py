import glob
import os
filename = input("File: ")
os.system("pdflatex " + filename)
for file in glob.glob("*.asy"):
    if file[:len(filename) - 4] == filename[:-4]:
        os.system("asy " + file)
os.system("pdflatex " + filename)
