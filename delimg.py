import os, sys
import shutil

# path = "Vehicules1024"  # 待读取的文件夹
# path_list = os.listdir(path)
#
# for filename in path_list:
#     file_split = filename.split('_')
#     if file_split[1]=='co.png':
#         new_dir = os.path.join(path, file_split[0] + '.png')
#         os.rename(os.path.join(path, filename), new_dir)
#     elif file_split[1]=='ir.png':
#         os.remove(os.path.join(path, filename))
#
# print('done!')


path = "xml/xml_test"  # 待读取的文件夹
path_list = os.listdir(path)
path_list.sort(key=lambda x: int(x[:-4]))  # 对读取的路径进行排序

path_img = 'VOC_COCO/images'
path_img_list = os.listdir(path_img)
path_img_list.sort(key=lambda y: int(y[:-4]))

new_img_path = 'VOC_COCO/test2017'

for filename_xml in path_list:
    for filename_img in path_img_list:
        if int(filename_img[:-4]) == int(filename_xml[:-4]):
            shutil.move(os.path.join(path_img, filename_img),new_img_path)
            break

print('done!')

