import pandas as pd
import matplotlib.pyplot as plt

def main():
    pd.options.display.max_columns = 160
    df = pd.read_csv('FinalUCDF.csv')
    print(df.head())

    corr_df = df[["X","Sales_in_thousands","Year_Resale_Value","Price_in_thousands","Engine_size","Horsepower","Wheelbase","Width"]]
    print(corr_df.head())
    print(corr_df.corr())

    #From a general look at the correlation of the dataframe. Resale valuse seems dependent on Price, horsepower and Pwer and performance

    SedansDf = df[(df.Vehicle_type == "Passenger")]
    print(SedansDf.head())

    print(SedansDf.max())
    #tmpSedandf = SedansDf[["Price_in_thousands","Model","Manufacturer"]]
    print(SedansDf[SedansDf['Price_in_thousands'] == SedansDf['Price_in_thousands'].max()])
        
    TrucksDF = df[(df.Vehicle_type == "Car")]
    print(TrucksDF.head())

if __name__ == '__main__':
    main()