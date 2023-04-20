import pymysql
import configparser


# 专门用来写数据库内容的
class my_db:
    # 连接   init函数  初始化函数 只要调用类，就会执行这个init函数
    # 合理

    def __init__(self, configPath, db):
        # 实例config工具
        config = configparser.ConfigParser()
        # 从配置文件里读取数据库服务器IP  账号 密码.....
        config.read(configPath)
        host = config[db]['host']
        port = int(config[db]['port'])
        user = config[db]['user']
        passwd = config[db]['passwd']
        db_name = config[db]['database']
        charset = config[db]['charset']
        try:
            self.con = pymysql.connect(host=host, port=port, user=user,
                                       password=passwd, database=db_name, charset=charset)
        except Exception as e:
            print('初始化数据库连接失败：%s' % e)
        self.cur = self.con.cursor()

    # 增删改查
    def select_query(self, sql):
        try:
            # 执行sql语句
            self.cur.execute(sql)
            # 显示结果
            result = self.cur.fetchall()
            return result
        except Exception as e:
            print('查询失败%s' % e)

    def insert_query(self, sql):
        try:
            # 执行sql语句
            self.cur.execute(sql)
            self.cur.execute('commit')
            return True
        except Exception as e:
            self.cur.execute('rollback')
            print('语句增删改失败%s' % e)
if __name__ == '__main__':
    # select =my_db('db.ini','TEST_DB')
    # sql = 'select host,user from mysql.user f where user="root"'
    # result = select.select_query(sql)
    # assert ('127.0.0.1', 'root') in result
    config = configparser.ConfigParser()
    config.read('db.ini')
    host = config['TEST_DB']['host']
    port = int(config['TEST_DB']['port'])
    user = config['TEST_DB']['user']
    passwd = config['TEST_DB']['passwd']
    db_name = config['TEST_DB']['database']
    charset = config['TEST_DB']['charset']
    print(host)