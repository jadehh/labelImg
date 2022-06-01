#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File     : test.py
# @Author   : jade
# @Date     : 2022/6/1 9:38
# @Email    : jadehh@1ive.com
# @Software : Samples
# @Desc     :
import os
import shutil
def qt_resource_to_py(resource_path,save_path):
    os.system("pyrcc5 -o {} {}".format(save_path,resource_path))
    # with open("tmp.py", "wb") as f1:
    #     with open(save_path, "rb") as f:
    #         content_all = str(f.read(),encoding="utf-8")
    #         # content_all = "a = b'1235466789090\n\n123456789'"
    #         content_list = content_all.split("=")
    #         for (k,content) in enumerate(content_list):
    #             tmp_content = ""
    #             # max_length = 2
    #             max_length = 10000
    #
    #             if len(content) > max_length:
    #                 for content_str in content.split('"'):
    #                     content_str_tmp = ""
    #
    #
    #                     if len(content_str) > max_length:
    #                         for (k,content_str_1) in enumerate(content_str.split("\n")[:-1]):
    #                             if k < len(content_str.split("\n")[:-1])-1:
    #                                 content_str_tmp = content_str_tmp + 'b"{}"'.format(content_str_1.replace("\r","").replace("\\","\\\\")) + "+"
    #                             else:
    #                                 content_str_tmp = content_str_tmp + 'b"{}"'.format(content_str_1.replace("\r","").replace("\\","\\\\"))+ "\n"
    #
    #                     else:
    #                         content_str = content_str.strip()
    #                         if len(content_str) > 1:
    #                             content_str_tmp ='qt_resource_data = qt_resource_data.encode("utf-8")\n' +content_str
    #                     tmp_content = tmp_content + content_str_tmp
    #             else:
    #                 tmp_content = content
    #             if k == len(content_list) - 1:
    #                 f1.write((tmp_content).encode("utf-8"))
    #             else:
    #                 f1.write((tmp_content + "=").encode("utf-8"))
    #
    # os.remove(save_path)
    # shutil.copy("tmp.py",save_path)
    # os.remove("tmp.py")







if __name__ == '__main__':
    qt_resource_to_py("resources.qrc","src/labelImg_resources.py")