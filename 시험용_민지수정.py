

import pandas as pd
import MYSQLBANK_민지수정 as msk
import random
import datetime


def main():
    
    while True:
        menu = input("업무 번호를 입력하세요 1:계좌 개설, 2: 거래 내역 조회, 3:입금, 4:출금, 5:계좌이체, 6:업무종료: ")
        print("2개 이상 항목 입력시 , 로 구분해주세요")
        if menu == "1":
            make = input("개설하실 계좌의 종류를 입력하세요. 입출금통장:1 / 적금통장:2 : ")
            if make == "1": #입출금통장 개설
                
                cmd = input("개설하실 계좌의 계좌번호, 예금주, 생년월일, 비밀번호, 입금액 을 입력하세요.최소 입금액은 1원 입니다: ").split(",")
                
                계좌번호, 계좌형태, 예금주, 생년월일, 비밀번호, 입금액 = cmd[0], "입출금통장", cmd[1], cmd[2], cmd[3], cmd[4]

                msk.search_account(cmd[0]) ####

                msk.create_account_inout(계좌번호, 계좌형태, 예금주, 생년월일, 비밀번호, 입금액)
                
                print("계좌를 생성되었습니다. 예금주:{}, 계좌번호:{}, 잔액:{}".format(예금주, 계좌번호, 입금액))

            elif make == "2": #적금통장 개설
                
                cmd2 = input("개설하실 계좌의 계좌번호, 예금주, 생년월일, 비밀번호, 입금액 을 입력하세요.최소 입금액은 1원 입니다: ").split(",")
                
                계좌번호2, 계좌형태2, 예금주2, 생년월일2, 비밀번호2, 입금액2 = cmd2[0], "적금통장", cmd2[1], cmd2[2], cmd2[3], cmd2[4]
                
                msk.create_account_saving(계좌번호2, 계좌형태2, 예금주2, 생년월일2, 비밀번호2, 입금액2) # 여기가 db로 저장되는 함수
                
                print("계좌가 생성되었습니다. 예금주:{}, 계좌번호:{}, 잔액:{}".format(예금주2, 계좌번호2, 입금액2))
            else:
                print("잘못된 값을 입력하였습니다")
                
            
            break

        elif menu == "2":
            cmd3 = input("조회하실 계좌의 계좌번호를 입력하세요: ")
            result = msk.search_account(cmd3)
            print(result)


            # account_num = cmd3 #int 형으로 변환?
            # if account_num == msk.search_inout_account(cmd3) ##??
            # msk.search_inout_account(cmd3)

            # elif account_num == msk.search_saving_account(cmd3)
            # print()

            # else
            # print("잘못된 값을 입력하였습니다")
            
            
            
            
            
            
main()