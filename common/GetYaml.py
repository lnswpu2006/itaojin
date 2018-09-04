# coding:utf-8
import yaml
import os
from config.globalparam import yaml_path
def parseyaml():
    '''
    遍历读取yaml文件
    '''
    pageElements = {}
    # 遍历读取yaml文件
    for fpath, dirname, fnames in os.walk(yaml_path):
        for name in fnames:
            # yaml文件绝对路径
            yaml_file_path = os.path.join(fpath, name)
            # 排除一些非.yaml的文件
            if ".yaml" in str(yaml_file_path):
                with open(yaml_file_path, 'r', encoding='utf-8') as f:
                    page = yaml.load(f)
                    pageElements.update(page)
    return pageElements
def get_yaml(root):
    data = parseyaml()
    # print(data)
    # for i in data[root][tag]:
    #     if i["name"] == key:
    #         return i["css"]
    return data[root]["locators"]
def get_value(data,key):
    for i in data:
        if i["name"] == key:
            return i["css"]


if __name__ == "__main__":
    m=get_yaml("unlog_index")
    print(m)
    n = get_value(m,"login")
    print(n)
