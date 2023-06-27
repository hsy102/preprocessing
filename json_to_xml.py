import os
import json
from xml.etree.ElementTree import Element, SubElement, ElementTree, dump
import argparse


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--meta_folder_path") # meta folder path(json)
    parser.add_argument("--labels_folder_path") # labels folder path(json)
    parser.add_argument("--output_folder_path") # folder path to save the converted xml file
    args = parser.parse_args()

    meta_folder_path = args.meta_folder_path
    labels_folder_path = args.labels_folder_path
    output_folder_path = args.output_folder_path


    def indent(elem, level=0):
        i = "\n" + level*"  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                indent(elem, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i


    list_meta = [meta for meta in os.listdir(meta_folder_path) if meta.endswith('json')]
    list_labels = [labels for labels in os.listdir(labels_folder_path) if labels.endswith('json')]


    for meta in list_meta:
        meta_file_path = os.path.join(meta_folder_path, meta)
        with open(meta_file_path) as f:
            data_f = json.load(f)
        data_key = data_f.get('data_key')
        label_id = data_f.get('label_id')
        image_info_width = data_f.get('image_info').get('width')
        image_info_height = data_f.get('image_info').get('height')

        for labels in list_labels:
            if label_id == labels.split('.')[0]:
                labels_file_path = os.path.join(labels_folder_path, labels)
                with open(labels_file_path) as g:
                    data_g = json.load(g)
                if isinstance(data_g.get('objects'), list):
                    for obj in data_g.get('objects'):
                        tracking_id = obj.get('tracking_id')
                        class_name = obj.get('class_name')
                        annotation_type = obj.get('annotation_type')
                        coord = obj.get('annotation').get('coord')
                        meta = obj.get('annotation').get('meta')
                        color = meta.get('color')
                        points = coord.get('points')
                        
                        filename = data_key[:-4]
                        
                        root = Element('annotation2')
                        SubElement(root, 'folder').text = output_folder_path
                        SubElement(root, 'filename').text = filename + '.xml'
                        SubElement(root, 'path').text = output_folder_path

                        size = SubElement(root, 'size')
                        SubElement(size, 'width').text = str(image_info_width)
                        SubElement(size, 'height').text = str(image_info_height)
                        SubElement(size, 'depth').text = '3'

                        obj = SubElement(root, 'object')
                        SubElement(obj, 'name').text = class_name
                        SubElement(obj, 'id').text = str(tracking_id)
                        SubElement(obj, 'type').text = annotation_type[:4]
                        SubElement(obj, 'clr').text = color
                        points_element = SubElement(obj, 'points')
                        for point in points[0][0]:
                            x = point['x']
                            y = point['y']
                            x_element = SubElement(points_element, 'x')
                            x_element.text = str(x)
                            y_element = SubElement(points_element, 'y')
                            y_element.text = str(y)
                            
                        indent(root)

                        tree = ElementTree(root)
                        tree.write(os.path.join(output_folder_path, '') + filename + '.xml', encoding='utf-8')
                
                break
        
        else:
            print("No matching labels file found for label_id:", label_id)


if __name__ == '__main__':
    main()