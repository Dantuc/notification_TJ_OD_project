import cv2
import os
import glob
from PIL import Image

def image_clear(current_path, destination_path="./projeto_find/clear_captcha"):

    files = glob.glob(f"{current_path}/*")
    print(files)

    for file in files:
        img = cv2.imread(file)
        gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        _, clear_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_TRUNC or cv2.THRESH_OTSU)
        file_name = os.path.basename(file)
        cv2.imwrite(f"{destination_path}/{file_name}", clear_img)
    

    files = glob.glob(f"{destination_path}/*")

    for file in files:
        image = Image.open(file)
        img2 = Image.new("L", image.size, 255)

        for x in range(image.size[1]):
            for y in range(image.size[0]):
                pixel_color = image.getpixel((y, x)) 

                if pixel_color < 127 and pixel_color > 40:
                    img2.putpixel((y, x), 0)
        
        file_name = os.path.basename(file)
        img2.save(f"{destination_path}/{file_name}")
    
    return print("Success!!")

if __name__ == "__main__":

    image_clear('./projeto_find/captcha_database')
