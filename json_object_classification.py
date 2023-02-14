import os
from xml.dom import minidom
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, ElementTree
from tqdm import tqdm
import pandas as pd
import shutil
import json
import argparse



def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--path_from", dest="path_from", help="복사할 폴더(복사할 원본폴더가 있는 상위폴더 지정")
    parser.add_argument("--path_to", dest="path_to", help="복사될 폴더(해당 경로에 원본폴더명으로 폴더가 생성되고 그안에 분류가 됨")
    args = parser.parse_args()
    path_from = args.path_from
    path_to = args.path_to


    list_folder = os.listdir(path_from)

    # 파일 클래스별로 복사
    for folder in list_folder:
        path_from_folder = os.path.join(path_from,folder)
        path_to_folder = os.path.join(path_to,folder)
        list_folder_json = [file for file in os.listdir(path_from_folder) if file[-4:] == 'json']
        for folder_json in tqdm(list_folder_json):
            path_from_folder_json = os.path.join(path_from_folder,folder_json)
            with open(path_from_folder_json, 'r', encoding = 'utf-8') as file:
                data = json.load(file)
                json_annotations = data['annotations']
                for annotations in json_annotations:
                    category_name = annotations.get('category_name')
                    if not os.path.isdir(path_to_folder):
                        os.mkdir(path_to_folder)
                    if not os.path.isdir(os.path.join(path_to_folder, category_name)):
                        os.mkdir(os.path.join(path_to_folder, category_name))
                    if os.path.isfile(path_from_folder_json[:-4]+'png') and os.path.isfile(path_from_folder_json):
                        try:
                            shutil.copy(path_from_folder_json,os.path.join(os.path.join(path_to_folder, category_name), folder_json))
                            shutil.copy(path_from_folder_json[:-4]+'png',os.path.join(os.path.join(path_to_folder, category_name),folder_json[:-4]+'png'))
                        except:
                            pass


    # 분류된 클래스명과 다른 클래스들은 삭제

    list_folder_pt = os.listdir(path_to)

    for folder in tqdm(list_folder_pt):
        pf = os.path.join(path_to, folder)
        list_folder_f = os.listdir(pf)
        
        for ff in list_folder_f:
            pff = os.path.join(pf, ff)
            list_pff_json = [file for file in os.listdir(pff) if file[-4:] == 'json']
            
            for pff_json in list_pff_json:
                pff_json_files = os.path.join(pff, pff_json)
                
                with open(pff_json_files, 'r', encoding = 'utf-8') as files:
                    datas = json.load(files)
                    datas_annotations = datas['annotations']
                    list_idx = []
                    for datas_a_idx, datas_a in enumerate(datas_annotations):
                        cate_name = datas_a.get('category_name')
                        if cate_name != pff_json_files.split('\\')[-2]:
                            list_idx.append(datas_a_idx)
                    list_idx.sort(reverse = True)
                    for idx in list_idx:
                        del datas_annotations[idx]
                    datas['annotations'] = datas_annotations

                with open(pff_json_files, 'w', encoding = 'utf-8') as f:
                    json.dump(datas, f, indent = 4, ensure_ascii = False)


if __name__ == "__main__":
    main()

exit()