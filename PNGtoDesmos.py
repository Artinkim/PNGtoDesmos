import cv2
import os

def imageToDesmos(path):
    image = cv2.imread(path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 10, 70)
    ret, mask = cv2.threshold(canny, 70, 255, cv2.THRESH_BINARY)
    nameWithExtension = path.split("/")[-1]
    name = nameWithExtension.split(".")[0]
    nameBMP = name+".bmp"
    cv2.imwrite(nameBMP, image)
    os.system("potrace "+nameBMP+" -b svg")
    print("BMP to SVG Coversion Done")
    os.system("java -jar svgeq.jar "+name+".svg")
    print("SVG to Desmos Coversion Done")
imageToDesmos("DylanW.png")
