# Python 3.7连接到MySQL数据库的模块推荐使用PyMySQL模块
# pip install pymysql
#  /usr/local/mysql/support-files/mysql.server start
# 一般流程
# 开始-创建connection-获取cursor-CRUD(查询并获取数据)-关闭cursor-关闭connection-结束
import pymysql

dbInfo = {
    'host' : 'cnode01',
    'port' : 3306,
    'user' : 'root',
    'password' : '123456',
    'db' : 'kkb'
}

sqls = ['select 1', 'select VERSION()']

result = []

class ConnDB(object):
    def __init__(self, dbInfo, sqls, params):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']
        self.sqls = sqls
        self.params = params

        # self.run()

    def run(self):
        conn = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            db = self.db
        )
        # 游标建立的时候就开启了一个隐形的事物
        cur = conn.cursor()
        try:
            for command in self.sqls:
                cur.execute(command)
                result.append(cur.fetchone())
            print(result)
            # 关闭游标
            cur.close()
            conn.commit()
        except:
            conn.rollback()
        # 关闭数据库连接
        conn.close()

    def save2MySql(self):
        conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db
        )
        # 游标建立的时候就开启了一个隐形的事物
        cur = conn.cursor()
        try:
            cur.execute(self.sqls, self.params)
            result.append(cur.fetchone())
            print(result)
            # 关闭游标
            cur.close()
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
        # 关闭数据库连接
        conn.close()


if __name__ == "__main__":
    sql = "INSERT INTO user (username, nickName,password,sex, birthday, job, email, phone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = ("1admin", "1超级管理员", "123", "1", "2018-03-08", "管理员", "admin@test.com.cn", "18187654321")

    db = ConnDB(dbInfo, sql, val)
    # db.run()
    # print(result)

    db.save2MySql()