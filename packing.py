#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File     : packing.py
# @Author   : jade
# @Date     : 2022/6/1 15:00
# @Email    : jadehh@1ive.com
# @Software : Samples
# @Desc     :
from jade import *

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    if getOperationSystem() == "Windows":
        parser.add_argument('--extra_sys_list', type=list,
                            default=[])  ## 需要额外打包的路径
        parser.add_argument('--full', type=bool,
                            default=False)  ## 打包成一个完成的包
        parser.add_argument('--scripts_path', type=str,
                            default=r"C:\Python3.6.7\Scripts")  ## 打包成一个完成的包
        parser.add_argument('--lib_path', type=str, default="labelImg_lib32")  ## 是否lib包分开打包

    else:
        parser.add_argument('--extra_sys_list', type=list,
                            default=[])  ## sys.path.append需要额外打包的路径


        parser.add_argument('--full', type=bool,
                            default=True)  ## 打包成一个完成的包
        parser.add_argument('--lib_path', type=str, default="labelImg_lib64")  ## 是否lib包分开打包

    parser.add_argument('--extra_path_list', type=list,
                            default=["data"])
    parser.add_argument('--use_jade_log', type=bool,
                        default=True) ##是否使用JadeLog

    parser.add_argument('--console', type=str,
                        default="False")  ## 是否显示命令行窗口,只针对与Windows有效
    parser.add_argument("--app_version",type=str,default="1.0.1.1")
    parser.add_argument('--app_name', type=str,
                        default="labelImg")  ##需要打包的文件名称
    parser.add_argument('--name', type=str,
                        default="标注工具-LabelImg")  ##需要打包的文件名称
    parser.add_argument('--appimage', type=bool,
                        default=True)  ## 是否打包成AppImage

    parser.add_argument('--is_qt', type=bool, default=False)  ## qt 会将controller view src 都进行编译
    parser.add_argument('--specify_files',type=list,default=["labelImg_resources.py"]) ## 指定编译的文件
    args = parser.parse_args()
    # writePy(args)
    #build(args)
    #copy_build(args, r"G:\SVN\软件\标注工具\标注工具-labelImg\{}".format(args.name + "V" + args.app_version))
    # packAPP(args)
    packSetup(args,r"G:\SVN\软件\标注工具\标注工具-labelImg\{}\Windows".format(args.name + "V" + args.app_version),"ff33f6a2-2ce9-11ed-89e6-220db03570cb")

