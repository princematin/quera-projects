import os
import sys
import time

name = sys.argv[0]
source = sys.argv[1]
destiantion = sys.argv[2]

pictures = [
    "jpg",
    "jpeg",
    "png"
]

videos = [
    "mp4",
    "avi",
    "3gp",
    "mpeg",
    "mkv",
    "wmv",
    "mov"
]
for root, dirs, files in os.walk(source):

    for item in files:

        postfix = os.path.splitext(item)
        postfix = postfix[-1]
        postfix = postfix.lower()
        postfix = postfix.replace(".", "")

        last_using_time = os.path.getmtime(os.path.join(root, item))
        last_using_root1 = os.path.join(root, item)
        year = time.ctime(last_using_time).split()[-1]

        if postfix in pictures:
            road = os.path.join(destiantion, year, "photos")
            last_using_root2 = os.path.join(road, item)

            os.makedirs(road, exist_ok = True)

            with open(last_using_root1, 'rb') as f:
                components = f.read()

            with open(last_using_root2, "wb") as k:
                k.write(components)

        elif postfix in videos:
            road = os.path.join(destiantion, year, "videos")
            last_using_root2 = os.path.join(road, item)

            os.makedirs(road, exist_ok = True)

            with open(last_using_root1, 'rb') as f:
                components = f.read()

            with open(last_using_root2, "wb") as k:
                k.write(components)

        else:
            continue