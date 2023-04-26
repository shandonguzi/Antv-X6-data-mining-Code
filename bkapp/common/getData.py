def get_data(dataId):
    # import pandas as pd
    # import pymysql
    #
    # db_conn = pymysql.connect(
    #     host='localhost',  # 连接名称，默认127.0.0.1
    #     user='root',  # 用户名
    #     password='12345678',  # 密码
    #     port=3306,  # 端口，默认为3306
    #     db='dataBase',  # 数据库名称
    #     charset='utf8',  # 字符编码
    # )
    #
    # id_to_name = {
    #     1: 'yuanweihua',
    #     2: 'graduateIncome',
    # }
    #
    # sql = "select * from {}".format(id_to_name[dataId])
    # data = pd.read_sql(sql, con=db_conn)
    # data.drop(['id'], axis=1, inplace=True)

    import pandas as pd

    id_to_name = {
        1: './bkapp/database/鸢尾花数据集.csv',
        2: './bkapp/database/大学毕业生收入数据集.csv'
    }

    data = pd.read_csv(id_to_name[dataId])

    return data
