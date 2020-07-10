import mysql.connector as mc

connect = mc.connect(
    host='localhost',
    user='root',
    password='root',
    database='test',
    charset='utf8'
)
print(connect)
my_cursor = connect.cursor()


def update():
    # 创建一张表,修改表结构
    # my_cursor.execute('ALTER TABLE test.customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY')
    # 向表中插入数据
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    # 当条数据
    value = ('莹莹', '灵宝')
    # 多条数据
    values = [
        ('少晴', '灵宝'),
        ('张三', '深圳'),
        ('李四', '西安'),
        ('马云', '杭州')
    ]
    # 执行sql
    my_cursor.executemany(sql, values)
    # 提交数据到数据库
    connect.commit()

    my_cursor.close()
    connect.close()


def select():
    sql = "select * from customers"
    my_cursor.execute(sql)
    result = my_cursor.fetchall()

    for one in result:
        print(one)
    connect.close()


select()
