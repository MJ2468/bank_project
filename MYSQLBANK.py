import pymysql
import datetime
import pandas as pd


create = "INSERT INTO 고객정보 (계좌번호, 계좌형태, 예금주, 생년월일, 비밀번호, 잔액) VALUES (%s,%s,%s,%s,%s,%s)"
create_sa = "INSERT INTO 고객정보 (계좌번호, 계좌형태, 예금주, 생년월일, 비밀번호, 잔액, 만기해지일) VALUES (%s,%s,%s,%s,%s,%s,%s)"
in_out_create = "INSERT INTO 입출금통장 (계좌번호, 예금주, 입금액, 잔액) VALUES (%s,%s,%s,%s)"
saving_create = "INSERT INTO 적금통장 (계좌번호, 예금주, 입금액, 잔액, 만기일) VALUES (%s,%s,%s,%s,%s)"
#in_deposit = 
#out_deposit = "INSERT INTO 입출금통장 (account, name, withdraw, balance) VALUES (%s,%s,%s,%s,%s)"
db = 'banksysdb'

conn = pymysql.connect(host= 'localhost', port=3306, user = 'camel3118',
                        password = 'Pbldb1234',
                        db = 'banksysdb',
                        charset = 'utf8')


#create = "INSERT INTO 고객정보 (계좌번호, 계좌형태, 예금주, 생년월일, 비밀번호, 잔고) VALUES (%s,%s,%s,%s,%s,%s)"
def create_account_inout(account, kind, name, birth_date, pw, balance):

    with conn:
        with conn.cursor() as cur:
            cur.execute(create, (account, kind, name, birth_date, pw, balance))
            cur.execute(in_out_create, (account, name, balance, balance))
            conn.commit()

def create_account_saving(account, kind, name, birth_date, pw, balance, expire_date):
    
    with conn:
        with conn.cursor() as cur:
            cur.execute(create, (account, kind, name, birth_date, pw, balance, expire_date))
            cur.execute(saving_create, (account, name, balance, balance, expire_date))
            conn.commit()



def search_inout_account(account):
    search_inout = ("SELECT 거래일, 계좌번호, 입금액, 출금액, 보낸분_받는분, 잔액 FROM 입출금통장 WHERE account={} ORDER BY 거래일 DESc").format(account)
    result = pd.read_sql_query(search_inout, conn)
    print(result) 
   
def search_saving_account(account):
    search_saving = ("SELECT 거래일, 계좌번호, 입금액, 잔액 FROM 적금통장 WHERE account={} ORDER BY 거래일 DESC").format(account)
    result = pd.read_sql_query(search_saving, conn)
    return result
            
            
# def deposit_in(account):
#     sql = "SELECT * FROM 입출금통장 WHERE 계좌 = %s ORDER BY 날짜 DESC"
#     data1 = []
#     with conn:
#         with conn.cursor() as cur:
#             cur.execute(sql, (account))
#             result = cur.fetchone()
#             for data in result:
#                 return data1.append(list(data))
#     return data1

                
                
# def withdraw(account, balance):
#     sql = "UPDATE 입출금통장 SET balance = balance - %d WHERE account = %s"
#     with conn:
#         with conn.cursor() as cur:
#             cur.execute(sql, (balance, account))
#             result = cur.fetchall()
#             for data in result:
#                 print(data)
                
# def transfer(account, balance, account_trans):
#     sql = "UPDATE 입출금통장 SET balance = balance - %d WHERE account = %s"
#     trans = "UPDATE 입출금통장 SET balance = balance + %d WHERE account = %s"
#     with conn:
#         with conn.cursor() as cur:
#             cur.execute(sql, (balance, account))
#             cur.execute(trans, (balance, account_trans))
#             result = cur.fetchall()
#             for data in result:
#                 print(data)
    
    
    
