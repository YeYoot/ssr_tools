# batch_create_account
批量创建/删除账号脚本，批量生成ss二维码

科学上网自建ssr服务器：<https://github.com/Alvin9999/new-pac/wiki/%E8%87%AA%E5%BB%BAss%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%95%99%E7%A8%8B>

## 批量创建/删除账号

说明：批量创建/删除账号脚本需要在服务器上运行

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

## 批量生成ss二维码

说明：代码在generate_qr文件夹下，运行环境为python3，建议在本地pc上运行

需要安装的第三方库：

- xlrd
- MyQR

1. 将数据填入到config.xlsx表格中

2. 运行脚本

   ```
   python generate_qr.py
   ```





