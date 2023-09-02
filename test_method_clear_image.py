import cv2
from PIL import Image

methods = [
    cv2.THRESH_BINARY,
    cv2.THRESH_BINARY_INV,
    cv2.THRESH_TRUNC,
    cv2.THRESH_TOZERO,
    cv2.THRESH_TOZERO_INV,
]

img = cv2.imread('./projeto_find/captcha_database/captcha3.png')

# transform image to gray scale
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

i = 1
for method in methods:
   _, fclear_img = cv2.threshold(gray_img, 127, 255, method or cv2.THRESH_OTSU)
   cv2.imwrite(f"./projeto_find/test_clear_method/fclear_img{i}.png", fclear_img)
   i+=1



image = Image.open('./projeto_find/test_clear_method/fclear_img3.png')
img2 = Image.new("L", image.size, 255)

for x in range(image.size[1]):
   for y in range(image.size[0]):
      pixel_color = image.getpixel((y, x)) 

      if pixel_color < 127 and pixel_color > 40:
        img2.putpixel((y, x), 0)
       
img2.save("./projeto_find/test_clear_method/fclear_img2_final.png")
