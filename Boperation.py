import sys
from bExcept import WithdrawError,InsuffFundError,DepositError,InvalidAccountError
import random
import cx_Oracle
con=cx_Oracle.connect('surya','AshoK1775')
bcur=con.cursor()
acur=con.cursor()
def OpenAccount():
    print("="*60)
    Name=input("Enter your name :")
    DOB=input("Enter your DOB :")
    Mobile=int(input("Enter your Mobile number :"))
    Address=input("Enter your Address :")
    ac=str(random.randrange(10000,100000))
    AccountNumber="283101000"+ac
    print("Your A/C number is : ",AccountNumber)
    Amount=int(input("Enter the ammount for openning Account:"))
    if Amount<500:
              print("="*60)
              print("Sorry your minimum amount should be 1000 for Opening A/C:")
              op=input("Do you want to try Again(yes/no):")
              if(op=='Yes' or op=='yes'):
                  OpenAccount()
              else:
                  print("\tThanks for using my Bank Application")
                  print("="*60)
                  sys.exit()
            
    else:
              print("="*60)
              bcur.execute("insert into Bbank values('%s','%s',%d,'%s','%s',%d)"%(Name,DOB,Mobile,Address,AccountNumber,Amount))
              acur.execute("update Aatm set Amount=%d where AccountNumber='%s'"%(Amount,AccountNumber))
              con.commit()
              print("\tWelcome to '{}' in my Bank Application".format(Name))
              print("\tYour A/C is Open Successfully")
              print("="*60)
    bcur.execute("select* from Bbank where AccountNumber='%s'"%AccountNumber)
    for data in bcur:
            print("\tName  :\t\t",data[0])
            print("\tDOB  : \t\t",data[1])
            print("\tMobile No.:\t",data[2])
            print("\tAddress  :\t",data[3])
            print("\tA/C Number:\t",data[4])
            print("\tAmount  :\t",data[5])
                          
def Withdraw():
    print("="*60)
    ac=input("Enter your A/C number:")
    bcur.execute("select* from Bbank where AccountNumber='%s'"%ac)
    for data in bcur:
        if(ac==data[4]):
            amo=int(input("Enter your amount for debit:"))
            if(amo<=0):
                raise WithdrawError
            elif(amo+500>data[5]):
                raise InsuffFundError
            elif(amo<=data[5]):          
                totm=data[5]-amo
                print("Welcome successfully debited balance :",amo)
                print("Youe total amount is :",totm)
                break
    else:
        raise InvalidAccountError   
    bcur.execute("update Bbank set Amount=%d where AccountNumber='%s'"%(totm,ac))
    acur.execute("update Aatm set Amount=%d where AccountNumber='%s'"%(totm,ac))
    con.commit()
                
           
def Deposit():
    ac=input("Enter your A/C number:")
    bcur.execute("select* from Bbank where AccountNumber='%s'"%ac)
    for data in bcur:
        if(ac==data[4]):
            print("="*60)
            nm=float(input("Enter your amount for Deposit:"))
            if(nm<=0):
                raise DepositError
            else:
                totm=data[5]+nm
                print("Welcome successfully credited balance :",nm)
                print("Youe total amount is :",totm)
                break
    else:
        raise InvalidAccountError   
    bcur.execute("update Bbank set Amount=%d where AccountNumber='%s'"%(totm,ac))
    acur.execute("update Aatm set Amount=%d where AccountNumber='%s'"%(totm,ac))
    con.commit()
         

def BalanceEnq():
    ac=input("Enter your A/C number:")
    bcur.execute("select* from Bbank where AccountNumber='%s'"%ac)
    for data in bcur:
        if(ac==data[4]):
            print("="*60)
            print("A/C Number:\t",data[4])
            print("Total amount:\t",data[5])
            break
    else:
        raise InvalidAccountError
            
def ChangeNum():
    ac=input("Enter your A/C number:")
    bcur.execute("select* from Bbank where AccountNumber='%s'"%ac)
    for data in bcur:
        if(ac==data[4]):
            print("="*60)
            omn=int(input("Enter Your old Mobile number:"))
            if(omn==data[2]):
                nmn=int(input("Enter Your new Mobile number:"))
                print("Welcome to you successfully Mobile number changed :")
                print("******************* Thanku **********************")
                bcur.execute("update Bbank set Mobile=%d where AccountNumber='%s'"%(nmn,ac))
                acur.execute("update Aatm set Mobile=%d where AccountNumber='%s'"%(nmn,ac))
                con.commit()
                break
            else:
                print("="*60)
                print("Sorry Your old Mobile number did't match from registered Number")
                break
    else:
        raise InvalidAccountError

def CloseAccount():
    ac=input("Enter your A/C number:")
    bcur.execute("select* from Bbank where AccountNumber='%s'"%ac)
    for data in bcur:
        if(ac==data[4]):
            print("="*60)
            print("Welcom to you.Your A/C successfully closed")
            print("\tName  :\t\t",data[0])
            print("\tDOB  : \t\t",data[1])
            print("\tMobile No.:\t",data[2])
            print("\tAddress  :\t",data[3])
            print("\tA/C Number:\t",data[4])
            print("\tAmount  :\t",data[5])
            print("="*60)
            bcur.execute("delete  from Bbank  where AccountNumber='%s'"%ac)
            acur.execute("delete from Aatm where AccountNumber='%s'"%ac)
            con.commit()
            break
    else:
        raise InvalidAccountError
def FundTransfer():
          ac=input("Enter your A/C number:")
          bcur.execute("select* from Bbank where AccountNumber='%s'"%ac)
          for data1 in bcur:
                if(ac==data1[4]):                    
                          fac=input("Enter the another A/C number where you want to transfer fund:")
                          if(ac==fac):
                                    print("="*60)
                                    print("Sorry you entered same A/C number. Please try again")
                                    break
                          bcur.execute("select* from Bbank where AccountNumber='%s'"%fac)
                          for data2 in bcur:
                                if(fac==data2[4]):
                                          am=int(input("Enter the amount:"))
                                          if(am<=0):
                                              raise WithdrawError
                                          elif(am+500>data1[5]):
                                              raise InsuffFundError
                                          elif(am<=data1[5]):          
                                              totm1=am+data2[5]
                                              totm2=data1[5]-am
                                              print("="*60)
                                              print("{} Rs transfer from {} A/C to {} A/C".format(am,ac,fac))
                                              print("Your total balance is :",totm2)
                                              break                          
                                                                                            
                          else:
                                    print("="*60)
                                    print("A/C number is not correct where you transfer  your fund")
                                    break
                          bcur.execute("update Bbank set Amount=%d where AccountNumber='%s'"%(totm1,fac))
                          acur.execute("update Aatm set Amount=%d where AccountNumber='%s'"%(totm1,fac))
                          bcur.execute("update Bbank set Amount=%d where AccountNumber='%s'"%(totm2,ac))
                          acur.execute("update Aatm set Amount=%d where AccountNumber='%s'"%(totm2,ac))
                          con.commit()
                          break
                                    
          else:
                    raise InvalidAccountError
         
            
  
    
