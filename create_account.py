#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import xlrd
import pexpect
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


def create_one_account(process, user_name, port, password, config):
    process.expect("要设置的用户")
    process.sendline(user_name)
    process.expect("端口")
    process.sendline(port)
    process.expect("密码")
    process.sendline(password)
    process.expect("加密方式")
    process.sendline(config["加密方式"])
    process.expect("协议插件")
    process.sendline(config["协议插件"])
    process.expect("混淆插件")
    process.sendline(config["混淆插件"])
    process.expect("限制的设备数")
    process.sendline(config["限制的设备数"])
    process.expect("单线程 限速上限")
    process.sendline(config["单线程 限速上限"])
    process.expect("总速度 限速上限")
    process.sendline(config["总速度 限速上限"])
    process.expect("总流量上限")
    process.sendline(config["总流量上限"])
    process.expect("禁止访问的端口")
    process.sendline(config["禁止访问的端口"])


def create_account(user_info, config):
    process = pexpect.spawn("bash ssrmu.sh", logfile=sys.stdout)
    process.expect("管理脚本")
    process.sendline("7")
    process.expect("用户配置")
    process.sendline("1")

    sorted_user = sorted(user_info.items(), key=lambda x: x[0])
    for key, value in sorted_user:
        create_one_account(process, key, value["port"], value["pass_word"], config)
        process.expect("是否继续")
        process.sendline("Y")

    show_account()
    return True


def show_account():
    process = pexpect.spawn("bash ssrmu.sh", logfile=sys.stdout)
    process.expect("请输入数字")
    process.sendline("5")
    process.expect("已使用流量总和")
    time.sleep(1)


if __name__ == '__main__':
    # 配置项
    config = {
        "加密方式": "10",
        "协议插件": "1",
        "混淆插件": "1",
        "限制的设备数": "5",
        "单线程 限速上限": "",
        "总速度 限速上限": "",
        "总流量上限": "30",
        "禁止访问的端口": "",
    }
    logging.basicConfig(level=logging.INFO)
    try:
        excel_name = sys.argv[1]
        sheet_name = sys.argv[2]
    except:
        excel_name = "userinfo.xlsx"
        sheet_name = "Sheet1"
        logging.info("未指定EXCEL与页签，默认读取{0}表格，{1}页签。".format(excel_name, sheet_name))
    # 获取EXCEL信息
    user_info = get_userinfo(excel_name, sheet_name)
    if not user_info:
        logging.error("读取EXCEL内容为空，任务失败。")
        sys.exit(-1)
    # 创建账号
    create_account(user_info, config)

    logging.info("任务完成。")
