#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pexpect
import xlrd
import sys
import logging
import time

def get_userinfo(excel_name, sheet_name):
    logging.info("读取{}表格，{}页签。")
    try:
        wb = xlrd.open_workbook(excel_name)
        ws = wb.sheet_by_name(sheet_name)
    except:
        logging.info("打开EXCEL表格失败，请确认{0}文件，{1}页签是否存在。".format(excel_name, sheet_name))
        return {}
    user_info = {}
    password_col = 0
    port_col = 0
    user_col = 0
    for i in range(0, ws.ncols):
        if ws.cell(rowx=0, colx=i).value == u"密码":
            password_col = i
        elif ws.cell(rowx=0, colx=i).value == u"端口":
            port_col = i
        elif ws.cell(rowx=0, colx=i).value == u"用户名":
            user_col = i

    for j in range(1, ws.nrows):
        user_name = str(ws.cell(rowx=j, colx=user_col).value)
        port = str(int(ws.cell(rowx=j, colx=port_col).value))
        if not ws.cell(rowx=j, colx=password_col).value:
            continue
        password = (ws.cell(rowx=j, colx=password_col).value)[-4:]
        user_info.update({user_name: {"pass_word": password, "port": port}})

    return user_info


def delete_one_account(port):
    process = pexpect.spawn("bash ssrmu.sh", logfile=sys.stdout)
    process.expect("管理脚本")
    process.sendline("7")
    process.expect("用户配置")
    process.sendline("2")
    process.expect("要删除的用户")
    process.sendline(port)
    time.sleep(0.5)


def delete_account(user_info):
    sorted_user = sorted(user_info.items(), key=lambda x: x[0])
    for key, value in sorted_user:
        delete_one_account(value["port"])
    show_account()
    return True


def show_account():
    process = pexpect.spawn("bash ssrmu.sh", logfile=sys.stdout)
    process.expect("请输入数字")
    process.sendline("5")
    process.expect("用户总数")
    time.sleep(1)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        excel_name = sys.argv[1]
        sheet_name = sys.argv[2]
    except:
        excel_name = "userinfo.xlsx"
        sheet_name = "Sheet1"
        logging.info("未指定EXCEL与页签，默认读取{0}表格，{1}页签。".format(excel_name, sheet_name))
    user_info = get_userinfo(excel_name, sheet_name)
    delete_account(user_info)
