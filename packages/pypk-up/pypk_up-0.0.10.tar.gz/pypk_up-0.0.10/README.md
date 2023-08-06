# pypk-up----简单管理python包

## 1、下载安装：
```pip install pypk_up```

## 2、可以尝试在控制台直接使用pypk_up去使用短命令形式运行

## 3、使用程序进行上传pypi时，请先注册好账号，避免出现登录等问题
[pypi官方网站](https://pypi.org/)

## 4、上传pypi文件请按照序号目录进行顺序执行

## 5、上传pypi的自动化，创建文件后，请手动去修改setup.py、LICENSE、README.md文件
[LICENSE开源](https://choosealicense.com/)

## 6、导入包使用：
### 导入更新包程序 
```from pypk.pypi_update import pypi_update```
### 导入pypi上传程序 
```from pypk.pypi_upload import pypi_upload```