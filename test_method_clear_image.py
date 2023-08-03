import cv2

methods = [
    cv2.THRESH_BINARY,
    cv2.THRESH_BINARY_INV,
    cv2.THRESH_TRUNC,
    cv2.THRESH_TOZERO,
    cv2.THRESH_TOZERO_INV,
]

img = cv2.imread('./projeto_find/captcha_database/captcha1.png')

# transform image to gray scale
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

i = 1
for method in methods:
   _, fclear_img = cv2.threshold(gray_img, 127, 255, method or cv2.THRESH_OTSU)
   cv2.imwrite(f"./projeto_find/test_clear_method/fclear_img{i}.png", fclear_img)
   i+=1