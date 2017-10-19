import os

DIR = "wallpaper/"
FORMAT = "%s.jpg"
START = 1

files = os.listdir(DIR)
cnt = START
for i in files:
    f = DIR + i
    t = DIR + FORMAT % str(cnt)
    os.rename(f, t)
    cnt += 1
