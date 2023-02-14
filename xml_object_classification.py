import os
from xml.dom import minidom
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, ElementTree
from tqdm import tqdm
import pandas as pd
import shutil
import argparse



def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--path_from", dest="path_from", help="복사할 폴더(복사할 원본폴더가 있는 상위폴더 지정")
    parser.add_argument("--path_to", dest="path_to", help="복사될 폴더(해당 경로에 원본폴더명으로 폴더가 생성되고 그안에 분류가 됨")
    args = parser.parse_args()
    path_from = args.path_from
    path_to = args.path_to

    list_folder = os.listdir(path_from)

    #파일 도구별로 복사
    for folder in list_folder:
        path_from_folder = os.path.join(path_from,folder)
        path_to_folder = os.path.join(path_to,folder)
        list_folder_xml = [file for file in os.listdir(path_from_folder) if file[-3:] == 'xml']
        for xml in tqdm(list_folder_xml):
            path_from_folder_xml = os.path.join(path_from_folder,xml)
            file = open(path_from_folder_xml,'r', encoding = 'utf-8')
            tree = ET.parse(file)
            root = tree.getroot()
            root_obj = root.findall('object')
            for obj in root_obj:
                classname = obj.find('name').text
                if not os.path.isdir(path_to_folder):
                    os.mkdir(path_to_folder)
                if not os.path.isdir(os.path.join(path_to_folder, classname)):
                    os.mkdir(os.path.join(path_to_folder, classname))

                if os.path.isfile(path_from_folder_xml[:-3]+'png') and os.path.isfile(path_from_folder_xml):
                    try:
                        shutil.copy(path_from_folder_xml,os.path.join(os.path.join(path_to_folder, classname),xml))
                        shutil.copy(path_from_folder_xml[:-3]+'png',os.path.join(os.path.join(path_to_folder, classname),xml[:-3]+'png'))
                    except:
                        pass
                    
    # 분류된 클래스별 폴더명과 xml의 <name>@@@</name> 클래스명을 비교하여 다른 클래스들은 object 삭제

    list_folder_pt = os.listdir(path_to)

    for folder in tqdm(list_folder_pt):
        pf = os.path.join(path_to, folder)
        list_folder_f = os.listdir(pf)
        
        for ff in list_folder_f:
            pff = os.path.join(pf, ff)
            list_pff_xml = [file for file in os.listdir(pff) if file[-3:] == 'xml']
            
            for xml in list_pff_xml:
                pff_xml = os.path.join(pff, xml)
                file = open(pff_xml, 'r', encoding = 'utf-8')
                tree = ET.parse(file)
                root = tree.getroot()
                root_obj = root.findall('object')
                
                for obj in root_obj:
                    classname = obj.find('name').text
                    
                    if not classname == ff:
                        root.remove(obj)
                        
                tree.write(pff_xml, encoding = 'utf-8')

if __name__ == "__main__":
    main()

exit()