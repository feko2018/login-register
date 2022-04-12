# 使用方法
- 1.创建虚拟环境
- 2.使用pip安装第三方依赖
- 3.修改settings.example.py文件为settings.py
- 4.运行migrate命令，创建数据库和数据表
```python
python manage.py makemigrations
python manage.py migrate
```

- 5.运行启动服务器
```python
python manage.py runserver
```
