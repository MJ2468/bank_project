import pymysql
import pandas as pd
import MYSQLBANK as msk
import random
import datetime


    



def main():
    
    while True:
        menu = input("업무 번호를 입력하세요 1:계좌 개설, 2: 계좌 조회, 3:입금, 4:출금, 5:계좌이체, 6:업무종료: ")
        print("2개 이상 항목 입력시 , 로 구분해주세요")
        if menu == "1":
            cmd = input("개설하실 계좌의 계좌번호, 예금주, 생년월일, 비밀번호, 입금액 을 입력하세요. 최소 입금액은 1원 입니다: ").split(",")
            id, account, name, balance = cmd[0], cmd[1], cmd[2], cmd[3]
            
            msk.create_account(id=id, account=account, name=name, balance=balance)
            print("계좌가 생성되었습니다. 예금주:{}, 계좌번호:{}, 잔액:{}".format(name,account,balance))
            break
        elif menu == "2":
            cmd = input("조회하실 계좌의 계좌번호를 입력하세요: ")
            number = cmd
            a1 = account.find_account(number)
            return a1
        elif menu == "3":
            cmd = input("입금하실 계좌번호와 금액을 입력하세요: ").split(",")
            number, amount = cmd[0], int(cmd[1])
            b1 = bank.deposit(number=number, amount=amount)
            return b1
            
        elif menu == "4":
            cmd = input("출금하실 계좌번호와 금액을 입력하세요: ").split(",")
            number, amount = cmd[0], int(cmd[1])
            c1 = bank.withdraw(number=number, amount=amount)
            return c1
        
        elif menu == "5":
            cmd = input("출금하실계좌, 이체를 원하시는금액(1원 이상)을 입력하세요: ").split(",")
            cmd1 = input("받으시는계좌를 입력하세요: ")
            number, amount, number_tran = cmd[0], int(cmd[1]), cmd1
            d1 = bank.withdraw(number=number, amount=amount)
            e1 = bank.transfer(number_tran=number_tran, amount=amount)
            return d1, e1
            
        elif menu == "6":
            print("업무를 종료합니다")
            break
            
        else:
            print("잘못된 명령어 입니다.")
            break
            
main()


# 적금통장 이자율은 횟수 지정하여 정해진 횟수마다 부가 최소 지정 입금액 지정할 것. 만기날짜(횟수?) 지정 반복문 이용하여 입금때 마다 입금액에 이자율 계산

# 밸런스에서 금액 지정하여 등급으로 세분화 - 신용평가

# 외국환 거래

# 환율조회

# 거래내역 조회*

# 날짜입력*
