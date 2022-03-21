import pandas as pd
import time
import phonenumbers
import random




path = 'Enter Path Of Excel File'

def create_acc():

    print('Whoooo! Your going to be officially our coustomer....')
                #loading animation
    t = 1
    while t < 3:
        print("\rLoading, Please Wait " + ("." * (t*5)), end=" ")
        time.sleep(1)
        t = t + 1
    
    
    print('\n')
    name = input('Enter Name: ')
    AccountNumber=x = random.randint(10000000,999999999)
    print("Your AccountNumber is: {0}".format(AccountNumber))
    amount=int(input('Enter Amount: '))

                
                
    PhoneNo=input('Enter Phone No: ')
    ################ validating Phone number #####################
    
    E1 = phonenumbers.parse("+91"+PhoneNo)
    f=(phonenumbers.is_valid_number(E1))
    
    
                
    if f==True:
                
        ###########################################################################################################################
        ############################################## Adding Data In excelsheet ##################################################
        ###########################################################################################################################
        K = pd.read_excel(path)
        seriesA = K['Name']
        seriesB = K['AccountNumber']
        seriesC = K['PhoneNo']
        seriesD= K['Amount']
        
        A = pd.Series(name)
        B = pd.Series(AccountNumber)
        C=pd.Series(PhoneNo)
        D= pd.Series(amount)
        
        seriesA = seriesA.append(A)
        seriesB = seriesB.append(B)
        seriesC = seriesC.append(C)
        seriesD = seriesD.append(D)
        
        L = pd.DataFrame({"Name":seriesA,"AccountNumber":seriesB,"PhoneNo":seriesC,"Amount":seriesD})
        L.to_excel(path,index=False)
        print('You are officially Become Our Coustomer......................................')


    else:
        print('Phone Number Is not correct')
#create_acc()
#github: - @padalakiran
