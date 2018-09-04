#coding=utf-8

import os
from common.readconfig import ReadConfig
# 读取配置文件
config_file_path = os.path.split(os.path.realpath(__file__))[0]

# print("config_file_path:",config_file_path)
read_config = ReadConfig(os.path.join(config_file_path,'config.ini'))
# print("read_config:",read_config)
# 项目参数设置
prj_path = read_config.getValue('projectConfig','project_path')

# print("prj_path:",prj_path)
# 日志路径
log_path = os.path.join(prj_path, 'report', 'log')
# print("log-path:",log_path)
# 截图文件路径
img_path = os.path.join(prj_path, 'report', 'image')
# print("img_path:",img_path)
# 测试报告路径
report_path = os.path.join(prj_path, 'report', 'testreport')
# print("report_path:",report_path)
# 默认浏览器
yaml_path = os.path.join(prj_path,'pages','pageelements')
# print(yaml_path)
browser = 'chrome'

# 测试数据路径
data_path = os.path.join(prj_path, 'data', 'testdata')
# print("data-path:",data_path)

