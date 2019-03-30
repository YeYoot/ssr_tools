# batch_create_account
批量创建账号脚本

## 使用说明

1. 拷贝脚本和表格到与ssrmu.sh文件的同级目录下

2. 将需要新增的用户名，端口号，密码输入到userinfo.xlsx表格中

3. 如果需要重新配置加密方式，协议等，在create_account.py的main函数中的config字典中修改

4. 运行脚本

   ```
   python create_account.py
   ```

