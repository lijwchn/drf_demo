# django-restframework 项目脚手架
### 包含的功能
1、全局异常处理  
2、封装全局json响应  
3、日志中间件  
4、权限类的功能，未完成  
5、curd基类

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
6、git commit 提交规范  
```shell
<type>(<scope>): <subject>
<type>：表示 commit 的类型，常见的有以下几种：

feat：新增功能
fix：修复 bug
docs：文档更新
style：代码格式化、样式调整等非功能性更新
refactor：重构代码
test：添加或修改测试代码
chore：构建过程或辅助工具的变动

示例：
feat(登录): 添加登录时需要验证码
```