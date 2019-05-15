# batch_create_account
批量创建/删除账号脚本

## 使用说明

### 批量创建账号

1. 拷贝create_account.py脚本和create_account.xlsx表格到与ssrmu.sh文件的同级目录下

2. 将需要新增的用户名，端口号，密码，限制设备数，总流量填入到create_account.xlsx表格中

3. 运行脚本

   ```
   python create_account.py
   ```

注：如果需要重新配置加密方式，协议等，在create_account.py的main函数中的config字典中修改

### 批量删除账号

1. 拷贝delete_account.py脚本和delete_account.xlsx表格到与ssrmu.sh文件的同级目录下

2. 将需要删除的端口号填入到delete_account.xlsx表格中

3. 运行脚本

   ```
   python delete_account.py
   ```
