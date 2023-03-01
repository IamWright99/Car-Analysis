import pandas as pd

def main():

    pd.options.display.max_rows = 160
    df = pd.read_csv('Car_sales.csv')
    print(df)

    print(df.info())

    carDF = pd.DataFrame(df)

    carDF.rename(columns= {'__year_resale_value':'resale'}, inplace= True)

    carDF.rename(columns= {'Sales_in_thousands':'sales(thousands)'}, inplace= True)

    carDF.rename(columns= {'Price_in_thousands':'price(thousands)'}, inplace= True)

    AcuraDF = pd.DataFrame(df)
    newAcuraDF= AcuraDF[(df["Manufacturer"] == 'Acura')]

    print(newAcuraDF)

    print(carDF)
    



if __name__ == '__main__':
    main()
