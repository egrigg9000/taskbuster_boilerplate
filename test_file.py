import os

curent_wd = os.getcwd()
dirname = os.path.dirname(os.path.abspath(__file__))
realpath = os.path.dirname(os.path.realpath(__file__))
abspath = os.path.dirname(os.path.abspath(__file__))

print (curent_wd)

print (dirname)

print (realpath)

print (abspath)
