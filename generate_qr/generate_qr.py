#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os
import xlrd
import base64
import logging
from MyQR import myqr


def get_config(excel_name, sheet_name):
    logging.info("读取{}表格，{}页签。")
    try:
        wb = xlrd.open_workbook(excel_name)
        ws = wb.sheet_by_name(sheet_name)
    except:
        logging.info("打开EXCEL表格失败，请确认{0}文件，{1}页签是否存在。".format(excel_name, sheet_name))
        exit(-1)
    col = {
        "IP": -1,
        "端口": -1,
        "密码": -1,
        "协议": -1,
    }
    for i in range(0, ws.ncols):
        for key, val in col.items():
            if ws.cell(rowx=0, colx=i).value == key:
                col[key] = i
    config = {}
    for j in range(1, ws.nrows):
        config.update({
            str(int(ws.cell(rowx=j, colx=col["端口"]).value)):
                {
                    "password": str(ws.cell(rowx=j, colx=col["密码"]).value),
                    "ip": str(ws.cell(rowx=j, colx=col["IP"]).value),
                    "method": str(ws.cell(rowx=j, colx=col["协议"]).value),

                }})

    return config


def generate_qr(config, picture="ye.png"):
    file_dir = os.path.join(os.getcwd(), "二维码")
    if not os.path.exists(file_dir):
        os.mkdir(file_dir)
    for port, val in config.items():
        ori_str = val["method"] + ":" + val["password"] + "@" + val["ip"] + ":" + port
        encode_str = base64.b64encode(ori_str.encode('utf-8'))
        des_str = "ss://".encode('utf-8') + encode_str
        pic_name = str(port) + ".jpg"
        myqr.run(des_str.decode(), save_name=pic_name, picture=picture, save_dir=file_dir)


if __name__ == '__main__':
    config = get_config("config.xlsx", "Sheet1")
    generate_qr(config)
