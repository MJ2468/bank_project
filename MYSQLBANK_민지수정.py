

import pymysql
import datetime
import pandas as pd


create = "INSERT INTO 고객정보 (계좌번호, 계좌형태, 예금주, 생년월일, 비밀번호, 잔액) VALUES (%s,%s,%s,%s,%s,%s)"
create_sa = "INSERT INTO 고객정보 (계좌번호, 계좌형태, 예금주, 생년월일, 비밀번호, 잔액, 만기해지일) VALUES (%s,%s,%s,%s,%s,%s,%s)"
in_out_create = "INSERT INTO 입출금통장 (계좌번호, 예금주, 입금액, 잔액) VALUES (%s,%s,%s,%s)"
saving_create = "INSERT INTO 적금통장 (계좌번호, 예금주, 입금액, 잔액, 만기일) VALUES (%s,%s,%s,%s,%s)"
#in_deposit = 
#out_deposit = "INSERT INTO 입출금통장 (account, name, withdraw, balance) VALUES (%s,%s,%s,%s,%s)"
db = 'pbldb'

conn = pymysql.connect(host= 'localhost', port= 3306, db='pbldb', passwd='pblpw', user='pbluser')


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
            cur.execute(create_sa, (account, kind, name, birth_date, pw, balance, expire_date))
            cur.execute(saving_create, (account, name, balance, balance, expire_date))
            conn.commit()


def search_account(account): #12345
    search = "SELECT 계좌번호, 예금주, 생년월일, 비밀번호, 잔액 FROM 고객정보 WHERE 계좌번호=%s"
    list1 = [] # 계좌번호
    with conn:
        with conn.cursor() as cur :
            cur.execute(search, (account)) ## 여기서 오류 # while 써주기
            result = cur.fetchall() 
            for data in result:
                list1= list1+list(data) # list1 = [계좌번호, 예금주, 생년월일, 비밀번호, 잔액]
                
###집에가서 보기!!!                
        while account == list1[0]: # true 
            print('있는 계좌번호입니다.') # 계속 시행
            break
                
            
        

def search_inout_account(account):
    search_inout = ("SELECT 거래일, 계좌번호, 입금액, 출금액, 보낸분_받는분, 잔액 FROM 입출금통장 WHERE account={} ORDER BY 거래일 DESc").format(account)
    result = pd.read_sql_query(search_inout, conn)
    print(result) 
   
def search_saving_account(account):
    search_saving = ("SELECT 거래일, 계좌번호, 입금액, 잔액 FROM 적금통장 WHERE account={} ORDER BY 거래일 DESC").format(account)
    result = pd.read_sql_query(search_saving, conn)
    return result
            



    
    
