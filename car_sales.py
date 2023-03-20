import pandas as pd

def main():

    pd.options.display.max_rows = 160
    df = pd.read_csv('Car_sales.csv')
    print(df.head())
    #1.) at immediate glance data is grouped by manufacturer, sales in thousands column has data is formatted differnt
    # there is high probability ther is columns with NaN 
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

    tmpcolumns = ['Manufacturer', 'Model', 'Vehicle_type',  'Latest_Launch']
    DateExtract = ['Latest_Launch']

    for column in tmpcolumns:
        df[column] = df[column].fillna("")

    rows = []
    floatSales = ['Sales_in_thousands']
    floatresale =['__year_resale_value']
    for i in range(len(df)):
        if df[floatSales].iloc[i] == "":
            rows.append(i)
        if df[floatresale].iloc[i] == "":
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
            date = df[DateExtract].iloc[i].split(" ")
            MonthsExtracted.append(date[0])
            YearsExtracted.append(int(date[2]))

    # turning month names into their month numbers
    for i, month in enumerate(MonthsExtracted):
        if month !=0:
            Datetime = Datetime.strptime(month, "%B")
            MonthNumber = Datetime.month
            MonthAdded = MonthNumber

    # check all months
    print(set(MonthAdded))
    print(set(YearsExtracted))
    
    
        
            



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
