数据库测试能连接也能查到数据
>>> from django.db import connection
>>> cursor = connection.cursor()
>>> cursor.execute("select * from west_character");
3L
>>> wc=cursor.fetchall();
>>> print wc
((1L, u'Vamei'), (2L, u'Django'), (3L, u'John'))
