import time
import datetime
import mysql.connector
def all_fuc(no,name="unknown",amount=0.0,Id=0):
    if no=="A" or no=="a" or no==1:
        conn=mysql.connector.connect(host='localhost',username='root',password='1234',database='bank_sys')
        cursor=conn.cursor()
        query="INSERT INTO info(name,balance) VALUES(%s, %s)"
        values=(name, amount)
        cursor.execute(query,values)
        conn.commit()
        conn.close()
        pass
    elif no=="B" or no=="b" or no==2:
        conn=mysql.connector.connect(host='localhost',username='root',password='1234',database='bank_sys')
        cursor=conn.cursor()
        query="SELECT * FROM info"
        cursor.execute(query)
        my_data=cursor.fetchall()
        conn.commit()
        conn.close()
        return my_data
    elif no=="C" or no=="c" or no==3:
        conn=mysql.connector.connect(host='localhost',username='root',password='1234',database='bank_sys')
        cursor=conn.cursor()
        query="UPDATE info SET balance=%s WHERE id=%s"
        values=(amount,Id)
        cursor.execute(query,values)
        conn.commit()
        conn.close()
def endscreen():
     user_list=all_fuc("b")
     ids,names,balances=zip(*user_list)
     ids,names,balances=list(ids),list(names),list(balances)
     print("_________________________________________________________________________________")
     print("---------------------**Enter any given options**---------------------------------")
     print("--------------------------------(A): Main Menu-----------------------------------")
     print("--------------------------------(B): Exit----------------------------------------")
     print("---------------------------------------------------------------------------------")
     choice=input("Enter Any Of Above Option : ")
     if(choice=="A" or choice=="a"):
          print("Please Wait......")
          time.sleep(1)
          menu()
     elif(choice=="B" or choice=="b"):
          print("#-----------------------Have a Nice Day------------------------------------#")
     else:
          print("Invalid Choice Enter Again")
          time.sleep(1)
          endscreen()

def menu():
     user_list=all_fuc("b")
     ids,names,balances=zip(*user_list)
     ids,names,balances=list(ids),list(names),list(balances)
     print(ids,names,balances)
     print("--------------------------------------------------------------------------------|")
     print("---------------------**WELCOME TO BANK'S MANAGEMENT SYSTEM**--------------------|")
     print("--------------------------Avaliable option to check/create accounts-------------|")
     print("--------------------------(A): Create an Account--------------------------------|")
     print("--------------------------(B): Deposit Money in your Account--------------------|")
     print("--------------------------(C): Withdraw Money from your Account-----------------|")
     print("--------------------------(D): See Details and Balance of your Account----------|")
     print("--------------------------------------------------------------------------------|")
     userchoice=input("Enter Your Choice From Above Options : ")

     if(userchoice=="A" or userchoice=="a"):
          create(names,ids,balances)
     elif(userchoice=="B" or userchoice=="b"):
          deposit(names,ids,balances)
     elif(userchoice=="C" or userchoice=="c"):
          withdraw(names,ids,balances)
     elif(userchoice=="D" or userchoice=="d"):
          display(names,ids,balances)
     else:
          print("Invalid Choice Enter Again")
          time.sleep(1)
          menu()
     time.sleep(1)
     endscreen()
def create(names,ids,balances):
     user_name=input("Enter Your Name : ")
     if user_name:
          if(len(ids)==0):
               user_id=1
          else:
               user_id=ids[-1]+1
          all_fuc("a",user_name)
          print("Creating Account...")
          time.sleep(1)
          print("**********************Your Account has Been Succesfully Created *****************************")
          print("Your ID is:",user_id)
          want_to_deposit(names,ids,balances)
     else:
          print("Enter both Name and Id")
          create(names,ids,balances)
def deposit(names,ids,balances):
     user_name=input("Enter Your Name : ")
     try:
          user_id=int(input("Enter Your ID : "))
     except:
          print("Enter ID correctly")
          deposit(names,ids,balances)
     else:
          invalid=0
          if user_name and user_id:
               for i in range(0,len(names)):
                    if(int(user_id)==ids[i]):
                         invalid+=1
                         if user_name==names[i]:
                              amount=float(input("Enter Amount To Deposit : "))
                              abs(amount)
                              if(len(balances)==0):
                                   all_fuc("c",user_name,amount,user_id)
                              else:
                                   balances[i]+=amount
                                   all_fuc("c",user_name,balances[i],user_id)
                                   print("Your Account has Been Credited by amount : ", amount)
                                   print("Your Total Balance is : ", balances[i])
                                   break
                         else:
                              print("Your Name is Not Found , Please Enter Your Name Again")
                              deposit(names,ids,balances)
                    else:
                         continue
               if(invalid==0):
                    print("*******************Invalid ID*************************************")
                    print("*******************Enter Details Again****************************")
                    deposit(names,ids,balances)
          else:
               print("Enter both Name and Id!")
               deposit(names,ids,balances)

def withdraw(names,ids,balances):
     user_name=input("Enter Your Name : ")
     try:
          user_id=int(input("Enter Your ID : "))
     except:
          print("Enter ID correctly")
          withdraw(names,ids,balances)
     else:
          invalid=0
          if user_name and user_id:
               for i in range(0,len(names)):
                    if(int(user_id)==ids[i]):
                         invalid+=1
                         j=i
                         if user_name==names[i]:
                              amount=float(input("Enter Amount To withdraw : "))
                              abs(amount)
                              if(len(balances)==0):
                                   print("Your Account Has Insufficient Funds For This Transaction")
                                   endscreen()
                              else:
                                   if amount>balances[i]:
                                        print("Your Account Has Insufficient Funds For This Transaction")
                                        endscreen()
                                   else:
                                        balances[i]-=amount
                                        all_fuc("c",user_name,balances[i],user_id)
                                        print("Your Account has Been Debeted by amount : ", amount)
                                        print("Your Total Balance is : ", balances[i])
                                        break
                         else:
                              print("Your Name is Not Found , Please Enter Your Name Again")
                              withdraw(names,ids,balances)
                    else:
                         continue
               if(invalid==0):
                    print("*******************Invalid ID*************************************")
                    print("*******************Enter Details Again****************************")
                    withdraw(names,ids,balances)
               else:
                    reciept(user_name,user_id,balances[j],amount)
          else:
               print("Enter both Name and Id!")
               withdraw(names,ids,balances)
          

def display(names,ids,balances):
     user_name=str(input("Enter Your Name : "))
     try:
          user_id=int(input("Enter Your ID : "))
     except:
          print("enter Id correctly")
          display(names,ids,balances)
     else:
          invalid=0
          if user_name and user_id:
               for i in range(0,len(names)):
                    if(user_id==ids[i]):
                         invalid+=1
                         if(user_name==names[i]):
                              print("Your Name : ",names[i])
                              print("Your ID : ",ids[i])
                              print("Available Balance : ",balances[i])
                         else:
                              print("Your Name is Not Found , Please Enter Your Name Again")
                              display(names,ids,balances)
                    else:
                         continue
               if(invalid==0):
                    print("*******************Invalid ID*************************************")
                    print("*******************Enter Details Again****************************")
                    display(names,ids,balances)
          else:
               print("Enter Name and Id")
               diplay(names,ids,balances)
def want_to_deposit(names,ids,balances,f=0):
     user_list=all_fuc("b")
     ids,names,balances=zip(*user_list)
     ids,names,balances=list(ids),list(names),list(balances)
     print("_________________________________________________________________________________")
     print("---------------------**Do You Want To Deposit**---------------------------------")
     print("--------------------------------(A): Deposit-----------------------------------")
     print("--------------------------------Press Any Key To Skip--------------------------")
     print("---------------------------------------------------------------------------------")
     choice=input("Enter Any Of Above Option : ")
     if(choice=="A" or choice=="a"):
          deposit(names,ids,balances)
     else:
          pass
def reciept(user_name,user_id,balances,amount):
     print("_________________________________________________________________________________")
     print("------------------------------**Want a Reciept**---------------------------------")
     print("--------------------------------(A): Reciept-----------------------------------")
     print("--------------------------------Press Any Key To Skip-----------------------")
     print("---------------------------------------------------------------------------------")
     choice=input("Enter Any Of Above Option : ")
     if(choice=="A" or choice=="a"):
          print("_______________________________________________________________")
          print("|               ",datetime.datetime.today())
          print("|Account Name : ","              |", user_name)
          print("|Account ID : ","                |", user_id)
          print("|Withdrawal Amount : ","         |", amount)
          print("|Current Balance : ","           |",balances)
          print("|______________________________________________________________")
     else:
          pass
menu()
     
