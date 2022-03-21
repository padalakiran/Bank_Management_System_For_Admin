import add as create
import Show as show
import deposite as dsp
import withdraw as Withd

a=input('Enter Password: ')
print()
l=["Enter Your Passwords Here Which You Want To Set"]


path = "Enter Path Of Excel File"
try:
    if a in l:
        while True:
            print('These are the choises infront of You Choose One')
            print("\t","1.Create New Account")
            print("\t","2.Show coustomer Details")
            print("\t","3.Deposite")
            print("\t","4.WithDraw")
            print("\t","5.Exit")
            print()
            
            b=input('Enter your Command: ')
            
            if b=='1':
              create.create_acc()
            # pass
            elif b=='2':
                show.showCu()
            elif b=='3':
                dsp.dep()
            elif b=='4':
                Withd.with_dr()
                        
            elif b=='5':
                break
        
            
            else:
                print("oops Worng Selection,Enter Correct Option............")
                print()
                

                
    else:
        print('its worng man its not correct......')
except:
    print('Enter Correct Element')
    
#github: - @padalakiran
