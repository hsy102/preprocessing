import os
import cv2
import xml.etree.ElementTree as ET
import numpy as np

def cordinate_annovie2cv2rectangles(annovie_points):
    
    xf_list = []
    yf_list = []

    for points in annovie_points:
        xf = points.findall('x')
        yf = points.findall('y')

        for x in xf:
            xf_list.append(x.text)
        for y in yf:
            yf_list.append(y.text)

    rectangles = []
    for i in range(0, len(xf_list), 2):
        x1 = float(xf_list[i])
        y1 = float(yf_list[i])
        x2 = float(xf_list[i+1])+x1
        y2 = float(yf_list[i+1])+y1
        rectangles.append((x1, y1, x2, y2))
    return rectangles


def hex2RGB(color_hex):
    color_hex = color_hex.lstrip('#')
    color_RGB = tuple(int(color_hex[i:i+2], 16) for i in (0, 2, 4))
    return color_RGB


# File extensions
tuple_extension_forimg = ('png', 'jpg', 'PNG', 'JPG')
path = r'D:\test\a'
path_to_save = r'D:\test\a\aa'
alpha = 0.1  # Higher alpha value for increased transparency

list_images = [file for file in os.listdir(path) if file.endswith(tuple_extension_forimg)]
os.makedirs(path_to_save, exist_ok=True)

for image in list_images:
    path_image = os.path.join(path, image)
    path_to_save_image = os.path.join(path_to_save, image)
    try:
        path_xml = os.path.join(path, image[:-3] + 'xml')
        tree = ET.parse(path_xml)
        root = tree.getroot()

    except:
        print(f'There is no XML for {image}')

    obj_list = root.findall('object')
    img_read = cv2.imread(path_image, cv2.IMREAD_COLOR)
    img_origin = cv2.imread(path_image, cv2.IMREAD_COLOR)

    for obj in obj_list:
        cordinate_annotation = obj.findall('points')
        color_annotation = obj.find('clr').text
        rectangles = cordinate_annovie2cv2rectangles(cordinate_annotation)
        color_RGB = hex2RGB(color_annotation)

        for rect in rectangles:
            x1, y1, x2, y2 = rect
            cv2.rectangle(img_read, (int(x1), int(y1)), (int(x2), int(y2)), color_RGB, thickness=4)

        dst = cv2.addWeighted(img_origin, alpha, img_read, (1-alpha), 0)
        dst_added = cv2.hconcat([img_origin, dst])
        cv2.imwrite(path_to_save_image, dst_added)