import sys,cx_Oracle
from bmenu import menu
from bExcept import*
from Boperation import Withdraw,Deposit,BalanceEnq,ChangeNum,OpenAccount,CloseAccount,FundTransfer

ch1=input("Are you new customer of Bank (Yes/No):")
if(ch1=='Yes' or ch1=='yes'):
          try:
                    OpenAccount()
          except cx_Oracle.DatabaseError as ap:
                    print("Database Error:",ap)
elif(ch1=='No' or ch1=='no'):
          while(True):
                    menu()
                    try:
                              ch2=int(input("Enter your Choice:"))
                              if(ch2==1):
                                        try:
                                                  Withdraw()
                                        except WithdrawError:
                                                  print("="*60)
                                                  print("Don't try invalid amount for Withdraw")
                                        except InsuffFundError:
                                                  print("="*60)
                                                  print("You do not have sufficient balance for withdraw")
                                        except InvalidAccountError:
                                                  print("="*60)
                                                  print("You entered invalid A/C number:Please try again")
                                        except ValueError:
                                                  print("="*60)
                                                  print("Dont't enter String/Special symbol/Alphanumeric for Withdraw")
                                        except:
                                                  print("Exception Occures:")
                                                  
                              elif(ch2==2):
                                        try:
                                                  Deposit()
                                        except DepositError:
                                                  print("="*60)
                                                  print("Don't enter invalid amount for Deposit")
                                        except InvalidAccountError:
                                                  print("="*60)
                                                  print("You entered invalid A/C number:Please try again")
                                        
                                        except:
                                                  print("Exception Occures:")
                                                  
                              elif(ch2==3):
                                        try:
                                                  BalanceEnq()
                                        except InvalidAccountError:
                                                  print("="*60)
                                                  print("You entered invalid A/C number:Please try again")
                                        except ValueError:
                                                  print("="*60)
                                                  print("Dont't enter String/Special symbol/Alphanumeric for Withdraw")
                                        except:
                                                  print("="*60)
                                                  print("Exception Occures:")
                                                
                              elif(ch2==4):
                                        try:
                                                  ChangeNum()
                                        except InvalidAccountError:
                                                  print("="*60)
                                                  print("You entered invalid A/C number:Please try again")
                              elif(ch2==5):
                                        try:
                                                  FundTransfer()
                                        except WithdrawError:
                                                  print("="*60)
                                                  print("Don't try invalid amount for Withdraw")
                                        except InsuffFundError:
                                                  print("="*60)
                                                  print("You do not have sufficient balance for Transfer")
                                        except InvalidAccountError:
                                                  print("="*60)
                                                  print("You entered invalid A/C number:Please try again")
                                        except ValueError:
                                                  print("="*60)
                                                  print("Dont't enter String/Special symbol/Alphanumeric for Withdraw")
                                        except:
                                                  print("="*60)
                                                  print("Exception Occures:")
                                                  
                              elif(ch2==6):
                                        try:
                                                  CloseAccount()
                                        except InvalidAccountError:
                                                  print("="*60)
                                                  print("You entered invalid A/C number:Please try again")
                              elif(ch2==7):
                                        print("="*60)
                                        print("\tThanks for using my Bank Application")
                                        print("="*60)
                                        sys.exit()
                              else:
                                        print("="*60)
                                        print("Sorry your choice is wrong please try again")
                    except ValueError:
                              print("="*60)
                              print("Don't enter String / AlphaNumeri / Special Symbol")
                              
else:
          print("="*60)
          print("Sorry your is wrong please try again")
