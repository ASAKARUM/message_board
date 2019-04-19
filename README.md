# Django留言板

## 项目简介


> 项目描述


``` bash
1.该Django留言板支持基本的登录，注册和登出功能；
2.该Django还支持登录留言功能，以及点赞和点踩功能，一个用户可以允许同时点赞和点踩，但最多只能操作一次；
3.界面和内部的元素主要使用了Bootstrap进行了修饰，这里我采取引用CDN的方式避免下载较多的Bootstrap配置文件；
4.该留言板包含名为msgboard的数据库，其中有两个主要的表，分别为Post和Record，Post用于存储用户信息、留言、点赞和点踩数目，Record用于记录用户的点赞和点赞文章信息，以及判断点赞还是点踩的布尔量；
5.该项目全程使用gitlab进行开发，每次提交的注释中包含了修改的信息。
```

> 注意事项
``` bash
1.注意需要创建数据库create database msgboard,之后需要执行./manage.py makemigrations msgboard和./manage.py migrate完成数据表的迁移；
2../manage.py runserver 0.0.0.0:8000 即可从本地127.0.0.1:8000中看到留言板效果；
3.gitlab使用https协议进行push和pull
```





authored by Bin Chen.