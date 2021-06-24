import os

def rename_img(img_folder):
    for dir1 in os.listdir(img_folder):

        for file in os.listdir(os.path.join(img_folder, dir1)):
            i = 0
            for c in os.listdir(os.path.join(img_folder, dir1, file)):
                image_path = os.path.join(img_folder, dir1, file,c)
                new_image_path = os.path.join(img_folder, dir1, file, f"{i}.jpg")
                os.rename(image_path, new_image_path)

                i = i + 1


    return print("Images renamed correctly!")


img_folder = r'C:/Users/polco/Documents/UNI/TFG/Mushrooms'
rename_img(img_folder)