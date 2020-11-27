import os, sys
import xml.etree.ElementTree as ET
import numpy as np

path = "VOC/Annotations/"  # 待读取的文件夹
path_list = os.listdir(path)
path_list.sort(key=lambda x: int(x[:-4]))  # 对读取的路径进行排序
count = 0
for filename in path_list:
    # 解析xml
    DOMTree = ET.parse(os.path.join(path, filename))
    # 返回文档的根节点
    root1 = DOMTree.getroot()
    # 查找根节点下'object'节点，返回nodelist
    obj = root1.findall("object")
    for i in obj:
        bbox = i.find("bndbox")
        xmin = int(float(bbox.find("xmin").text)) - 1
        ymin = int(float(bbox.find("ymin").text)) - 1
        xmax = int(float(bbox.find("xmax").text))
        ymax = int(float(bbox.find("ymax").text))

        assert xmax > xmin, '%s' % xml_file
        assert ymax > ymin, '%s' % xml_file
        width = abs(xmax - xmin)
        height = abs(ymax - ymin)

        wh = np.array([width,height])
        count += 1
        print(wh)

print('done!')
print(count)