import pandas as pd 
import xlrd


def showCu():
 try:
        path='Enter Path Of Excel File'

        print('what do you want to Show: ')
        print('1.Names','\t','2.Account Numbers',
            '\t','3.Phone Number','\t','4.Ammount','\t'
            ,'5.All Data','\t','6.Specfic Person')
        c=input('enter your choise: ')
        print()
        loc =(path)
        
        ########### Names ################
        if c=='1':
            # loc = (path)
            wb = xlrd.open_workbook(loc)
            sheet = wb.sheet_by_index(0)
            sheet.cell_value(0, 0)

            for i in range(sheet.nrows):
                            print(sheet.cell_value(i, 0))
            print()
            
        ############ Acoount Number ##########
                    
        if c=='2':
                wb = xlrd.open_workbook(loc)
                sheet = wb.sheet_by_index(0)
                sheet.cell_value(0,0)

                for i in range(sheet.nrows):
                            print(sheet.cell_value(i, 1))
                print()
        
        ########### Phone Number #############
        
        if c=='3':
                wb = xlrd.open_workbook(loc)
                sheet = wb.sheet_by_index(0)
                sheet.cell_value(0,0)

                for i in range(sheet.nrows):
                            print(sheet.cell_value(i, 2))
                print()
        
        ############# Amount ###########
        
        if c=='4':
                wb = xlrd.open_workbook(loc)
                sheet = wb.sheet_by_index(0)
                sheet.cell_value(0,0)

                for i in range(sheet.nrows):
                            print(sheet.cell_value(i, 3))
                print()
        
        ############ All Data #############
        if c=='5':
            data = pd.ExcelFile(path)
            df = data.parse('Sheet1')
            df.info
            location = (path)
            wb1= xlrd.open_workbook(location)
            s1 = wb1.sheet_by_index(0)
            print(df.head(s1.nrows))
            print()

            
            
        ########Specific People#########
        
        if c=='6':
            wb = xlrd.open_workbook(path)
            sheet = wb.sheet_by_index(0)

            sheet.cell_value(0, 0)

            a=input('Enter Account Number: ')
            location = (path)
            wb1= xlrd.open_workbook(location)
            s1 = wb1.sheet_by_index(0)


            print()

            for i in range(0,s1.nrows):
                if(sheet.cell_value(i,1)==float(a)):
                    print('Name: {0} '.format(sheet.cell_value(i,0)),'\t',
                        'AccountNumber: {0}'.format(sheet.cell_value(i,1)),'\t',
                        'PhoneNumber: {0}'.format(sheet.cell_value(i,2)),'\t',
                        'Amount: {0}'.format(sheet.cell_value(i,3)),sep=" ")
    
 except:
     print("Enter Valid Data")   
#showCu()
#github: - @padalakiran
