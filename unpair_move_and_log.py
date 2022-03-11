import os 
import argparse
import shutil



def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--checkunpair", dest="checkunpair", help="Check if image and xml match") # dest: 적용 위치 지정
    args = parser.parse_args()
    checkunpair = args.checkunpair
    
    log_file = open(os.path.join(checkunpair, 'log.txt'), "w",  encoding='UTF8')
    
    if checkunpair:
        
        list_xml = [file for file in os.listdir(checkunpair) if file.endswith('xml')]
        list_img = [file for file in os.listdir(checkunpair) if file.endswith('png') or file.endswith('jpg')]
        
        list_unpaired_xml = []
        list_unpaired_img = []
        
        for index_outside, xml in enumerate(list_xml):
            count = 0
            for index_inside, img in enumerate(list_img):
                if xml.split('.')[0] == img.split('.')[0]:
                    count += 1
            if count == 0:
                list_unpaired_xml.append(xml)
                log_file.write('짝이없는 xml : ')
                log_file.write('\t')
                log_file.write(xml)
                log_file.write('\n')
                
        try:
            if os.path.isdir(os.path.join(checkunpair, 'unpair')) == True:
                for unpaired_xml in list_unpaired_xml:
                    shutil.move(os.path.join(checkunpair, unpaired_xml), os.path.join(checkunpair, 'unpair'))    
        except:
            pass
        
        try:
            if os.path.isdir(os.path.join(checkunpair, 'unpair')) == False:
                os.mkdir(os.path.join(checkunpair, 'unpair'))
                for unpaired_xml in list_unpaired_xml:
                    shutil.move(os.path.join(checkunpair, unpaired_xml), os.path.join(checkunpair, 'unpair'))
        except:
            pass
                
            
            
            
        
        for index_outside, img in enumerate(list_img):
            count = 0
            for index_inside, xml in enumerate(list_xml):
                if xml.split('.')[0] == img.split('.')[0]:
                    count += 1
            if count == 0:
                list_unpaired_img.append(img)
                log_file.write('짝이없는 img : ')
                log_file.write('\t')
                log_file.write(img)
                log_file.write('\n')

        try:
            if os.path.isdir(os.path.join(checkunpair, 'unpair')) == True:
                for unpaired_img in list_unpaired_img:
                    shutil.move(os.path.join(checkunpair, unpaired_img), os.path.join(checkunpair, 'unpair'))    
        except:
            pass

        try:
            if os.path.isdir(os.path.join(checkunpair, 'unpair')) == False:
                os.mkdir(os.path.join(checkunpair, 'unpair'))
                for unpaired_img in list_unpaired_img:
                    shutil.move(os.path.join(checkunpair, unpaired_img), os.path.join(checkunpair, 'unpair'))
        except:
            pass   


    print('짝이없는 xml : ',list_unpaired_xml)
    print('짝이없는 img : ',list_unpaired_img)

    log_file.close()

if __name__ == "__main__":
    main()