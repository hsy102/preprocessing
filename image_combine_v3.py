import os
import cv2
import xml.etree.ElementTree as ET
import numpy as np

def cordinate_annovie2cv2polylines(annovie_points):
    
    xf_list = []
    yf_list = []

    for points in annovie_points:
        xf = points.findall('x')
        yf = points.findall('y')
        
        for x in xf:
            xf_list.append(x.text)
        for y in yf:
            yf_list.append(y.text)
            
        list_cordinate = [(float(x), float(y)) for x, y in zip(xf_list, yf_list)]
        
    list_cordinate = np.array(list_cordinate, dtype=np.int32)
    return list_cordinate


def hex2RGB(color_hex):
    color_hex = color_hex.lstrip('#')
    color_RGB = tuple(int(color_hex[i:i+2], 16) for i in (0, 2, 4))
    return color_RGB


# File extensions
tuple_extension_forimg = ('png', 'jpg', 'PNG', 'JPG')
path = r'D:\test\a'
path_to_save = r'D:\test\a\aa'
alpha = 0.1 # 높을수록 라벨링 투명도가 높음

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
        cordinate_forcv2 = cordinate_annovie2cv2polylines(cordinate_annotation)
        color_RGB = hex2RGB(color_annotation)

        #img_read = cv2.fillPoly(img_read, [cordinate_forcv2], color_RGB)
        img_read = cv2.polylines(img_read, [cordinate_forcv2], True, color_RGB, thickness=4, lineType=None, shift=None)

        dst = cv2.addWeighted(img_origin, alpha, img_read, (1-alpha), 0)
        dst_added = cv2.hconcat([img_origin, dst])
        cv2.imwrite(path_to_save_image, dst_added)