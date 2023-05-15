# django-restframework 项目脚手架
### 包含的功能
1、全局异常处理  
2、封装全局json响应  
3、全局日志记录  

### 项目流程
1、创建
```shell
django-admin startproject demo
```
2、修改 settings.py 的数据库配置  
3、安装相关依赖
```shell
pip install -r requirements.txt -i https://pypi.douban.com/simple/
```
4、创建子应用
```shell
python manage.py startapp <app_name>
```
5、生成数据库迁移文件&迁移
```shell
python manage.py makemigrations
python manage.py migrate
```