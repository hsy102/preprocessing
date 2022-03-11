import os
import argparse
import xml.etree.ElementTree as et
from tqdm.auto import tqdm



def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--nodedelete", dest="nodedelete", help="labeling node edit and delete")
    args = parser.parse_args()
    nodedelete = args.nodedelete


    x_list = []

    xml_list = os.listdir(nodedelete)

    for xml in xml_list:
        if xml.endswith('png') or xml.endswith('jpg'):
            pass
        else:
            x_list.append(xml)



    # x값과 y값이 같으면 해당 object 삭제

    xf_list = []
    yf_list = []

    for xml_file in tqdm(x_list):
        tree = et.parse(os.path.join(nodedelete, xml_file))
        root = tree.getroot() # 최상위 경로 가져오기
        obj_list = root.findall('object')
        
        for obj in obj_list:
            points_list = obj.findall('points')
            xf_list.clear()
            yf_list.clear()
            
            for points in points_list:
                xf = points.findall('x')
                yf = points.findall('y')
                
                for x in xf:
                    xf_list.append(x.text)
                    xf_list = [int(float(i_xf)) for i_xf in xf_list]
                    
                for y in yf:
                    yf_list.append(y.text)
                    yf_list = [int(float(i_yf)) for i_yf in yf_list]
                    
                if xf_list == yf_list:
                    root.remove(obj)
                else:
                    pass
                
        tree.write(os.path.join(nodedelete, xml_file))



    # x값과 y값이 0 이하면 0으로 맞추기

    for xml_file in tqdm(x_list):
        tree = et.parse(os.path.join(nodedelete, xml_file))
        root = tree.getroot() # 최상위 경로 가져오기
        obj_list = root.findall('object')
        
        for obj in obj_list:
            points_list = obj.findall('points')
            
            for points in points_list:
                xf = points.findall('x')
                yf = points.findall('y')
                
                for xv in xf:
                    x1t = xv.text
                    
                    if float(x1t) < 0:
                        x0 = x1t.replace(str(float(x1t)), '0')
                        xv.text = x0
                    else:
                        pass
                    
                for yv in yf:
                    y1t = yv.text
                    
                    if float(y1t) < 0:
                        y0 = y1t.replace(str(float(y1t)), '0')
                        yv.text = y0
                    else:
                        pass
                
        tree.write(os.path.join(nodedelete, xml_file))



    # x값과 y값이 width와 height 값 이상이면 최대값/최소값을 width/height 값에 맞추기

    for xml_file in tqdm(x_list):
        tree = et.parse(os.path.join(nodedelete, xml_file))
        root = tree.getroot() # 최상위 경로 가져오기
        obj_list = root.findall('object')
        s_list = root.findall('size')
        
        for wh in s_list:
            w = wh.findall('width')
            w1t = w[0].text
            
            h = wh.findall('height')
            h1t = h[0].text

        for obj in obj_list:
            points_list = obj.findall('points')
            
            for points in points_list:
                xf = points.findall('x')
                yf = points.findall('y')
                
                for xv in xf:
                    if float(xv.text) >= float(w1t):
                        xv.text = str(w1t)
                    else:
                        pass
                    
                for yv in yf:
                    if float(yv.text) >= float(h1t):
                        yv.text = str(h1t)
                    else:
                        pass
                    
        tree.write(os.path.join(nodedelete, xml_file))



if __name__ == "__main__":
    main()