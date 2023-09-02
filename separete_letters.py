import cv2
import os
import glob

files = glob.glob('./projeto_find/clear_captcha/*')
print(files)
for file in files:
    img = cv2.imread(file)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    #Black and white
    _, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV)
    #Find conturs
    conturs, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    letters_area = []
    #Filter conturs
    for contur in conturs:
        (x, y, w, h) = cv2.boundingRect(contur)
        area = cv2.contourArea(contur)
        if area > 115:
            letters_area.append((x, y, w, h))
    
    #if len(letters_area) != 5:
    #    continue
    #Draw conturs and separete letters in single images
    final_img = cv2.merge([img] *3)
    i = 0
    for rectangle in letters_area:
        x, y, w, h = rectangle
        letter_img = img[y-2:y+h+2, x-2:x+w+2]
        i+=1
        file_name = os.path.basename(file).replace(".png", f"letter{i}.png")
        cv2.imwrite(f"./projeto_find/captcha_letters/{file_name}", letter_img)
