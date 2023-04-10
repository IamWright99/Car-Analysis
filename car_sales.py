import pandas as pd
from datetime import datetime
from decimal import *
import openpyxl


def main():

    pd.options.display.max_rows = 160
    df = pd.read_csv('Car_sales.csv')
    print(df.head())
    #1.) at immediate glance data is grouped by manufacturer(alphabetical order), sales in thousands column has data formatted differntly
    # there is high probability there are columns with NaN 
    #the biggest issue I see is the NaN mainly because lack of data may be due to the car being disontinued or wasn't recorded

    columns = list(df.columns)
    print(columns)

    #2.) looking at all possible NaN in data set

    print("missing values: ")
    print(df.isnull().mean())
    print("")

    # 3.) most of the missing data comes from the year resale value column (22%), which was already to be expected
    # I speculated whether I shpuld delete columns to make the data easier to read and use later 
    # I opted not to because I believe that all the columns would be useful in this analysis 
    # especially the column with the most NaN values (year resale value)

    # 4.) checking datatypes

    print("column datatype: ")
    print(df.dtypes)

    # 5.) most of the data has a floating point datatype which usually signifies that it can hold whole numbers or numbers with decimals
    # only two columns have an object datatype that can hold a mixture of numbers and strings ( aka. letters)

    # 6.) fillinng in empty entries with an arbitrary value

    tmpcolumns = ['Manufacturer', 'Model', 'Vehicle_type',  'Latest_Launch', '__year_resale_value','Price_in_thousands','Engine_size','Horsepower','Wheelbase','Width','Length','Curb_weight','Fuel_capacity','Fuel_efficiency','Power_perf_factor']
    DateExtract = ['Latest_Launch']

    for column in tmpcolumns:
        df[column] = df[column].fillna("")

    rows = []
    for i in range(len(df)):
        if df['Sales_in_thousands'].iloc[i] == "":
            rows.append(i)
        if df['__year_resale_value'].iloc[i] == "":
            rows.append(i)
        if df['Vehicle_type'].iloc[i] == "":
            rows.append(i)
        if df['Price_in_thousands'].iloc[i] == "":
            rows.append(i)
        if df['Engine_size'].iloc[i] == "":
            rows.append(i)
       
        
        
    # Examining rows to confirm null state of column

    df.loc[rows, :]

    # Extracting months and years from latest launch
    MonthsExtracted = []
    YearsExtracted = []

    for i in range(len(df)):
        if i in rows:
            MonthsExtracted.append(0)
            YearsExtracted.append(0)
        else:
            date = df['Latest_Launch'].iloc[i].split("/")
            MonthsExtracted.append(date[0])
            YearsExtracted.append(int(date[2]))

    # turning month names into their month numbers
    for i, month in enumerate(MonthsExtracted):
        if month !=0:
            Datetime_obj = datetime.strptime(month, "%m")
            MonthNumber = Datetime_obj.month
            MonthsExtracted[i] = MonthNumber

    # check all months
    print(set(MonthsExtracted))
    print(set(YearsExtracted))

    df.insert(16,"Months_Added", MonthsExtracted, allow_duplicates= True)
    df.insert(17,"Years_Added", YearsExtracted, allow_duplicates= True)
    print(df.head())

    # We have now created two knew columns that will be used later for further analysis

    # Checking unique values
    # this is mainly to do a final check to make sure the values I expect to be in the column is there (empty cells will have '' because they used to be nan)

    print(df['__year_resale_value'].unique())
    print(df['Manufacturer'].unique())
    print(df['Model'].unique())
    print(df['Sales_in_thousands'].unique())
    print(df['Vehicle_type'].unique())
    print(df['Price_in_thousands'].unique())
    print(df['Engine_size'].unique())
    print(df['Horsepower'].unique())
    print(df['Wheelbase'].unique())
    print(df['Width'].unique())
    print(df['Length'].unique())
    print(df['Curb_weight'].unique())
    print(df['Fuel_efficiency'].unique())
    print(df['Fuel_capacity'].unique())
    print(df['Latest_Launch'].unique())
    print(df['Power_perf_factor'].unique())

    #the data has no unexpected outliers or in the wrong place
    # Writing to excel file for further analysis

    df.to_excel("UsedCarDf.xlsx",sheet_name='UsedCarDF')


    

    

    
        
            



    #newdf = df.dropna()

    #print(newdf)

    #print(newdf.info())

    #carDF = pd.DataFrame(newdf)

    #carDF.rename(columns= {'__year_resale_value':'resale'}, inplace= True)

    #carDF.rename(columns= {'Sales_in_thousands':'sales(thousands)'}, inplace= True)

    #carDF.rename(columns= {'Price_in_thousands':'price(thousands)'}, inplace= True)

    #carDF.rename(columns= {'Engine_size':'Engine(size)'}, inplace= True)

    #AcuraDF = pd.DataFrame(carDF)
    #newAcuraDF= AcuraDF[(carDF["Manufacturer"] == 'Acura')]

    #print(newAcuraDF)
    #print(carDF)
    



if __name__ == '__main__':
    main()
