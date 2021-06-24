import os
import random
import shutil

a = os.listdir("Mushrooms_V50_T50")
os.chdir("Mushrooms_V50_T50")
if os.path.isdir("train/0/") is False:
    os.mkdir("train")
    os.mkdir("valid")
    os.mkdir("test")

for i in a:
    shutil.move(f"{i}", "train")
    os.mkdir(f"valid/{i}")
    os.mkdir(f"test/{i}")

    valid_samples = random.sample(os.listdir(f"train/{i}"), 50)
    for j in valid_samples:
        shutil.move(f"train/{i}/{j}", f"valid/{i}")

    test_samples = random.sample(os.listdir(f"train/{i}"), 50)
    for k in test_samples:
        shutil.move(f"train/{i}/{k}", f"test/{i}")

os.chdir("..")