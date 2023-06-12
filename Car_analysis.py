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

    # Qusetion 1: which Sedan is the most expensive? What about Trucks?

    print(SedansDf.max())

    print(SedansDf[SedansDf['Price_in_thousands'] == SedansDf['Price_in_thousands'].max()])
        
    TrucksDF = df[(df.Vehicle_type == "Car")]

    print(TrucksDF.max())

    print(TrucksDF[TrucksDF['Price_in_thousands'] == TrucksDF['Price_in_thousands'].max()])

    # Question 2: out of these 5 manufacturers, which manufacturer is the most expensive, Which is the cheapest?

    HondaDf = df[(df.Manufacturer == "Honda")]

    ToyotaDF = df[(df.Manufacturer == "Toyota")]

    NissanDf = df[(df.Manufacturer == "Nissan")]

    MercedesDf = df[(df.Manufacturer == "Mercedes-B")]

    BMW_DF = df[(df.Manufacturer == "BMW")]

    HondaAVG= HondaDf.Price_in_thousands.mean()
    ToyotaAVG = ToyotaDF.Price_in_thousands.mean()
    NissanAVG = NissanDf.Price_in_thousands.mean()
    MercedesAVG = MercedesDf.Price_in_thousands.mean()
    BMW_AVG = BMW_DF.Price_in_thousands.mean()

    
    total_AVG_DF = [HondaAVG,ToyotaAVG,NissanAVG,MercedesAVG,BMW_AVG]
    total_AVG_DF.sort()

    print("Honda avg price: ", HondaAVG)
    print("Toyota avg price: ", ToyotaAVG)
    print("Nissan avg price: ", NissanAVG)
    print("Mercedes avg price: ", MercedesAVG)
    print("BMW avg price: ", BMW_AVG)
    print(total_AVG_DF)
    
    # Question 3: Out of these 5 manufacturers, which manufacturer sold the most units?

    Hondasold = HondaDf.Sales_in_thousands.sum()
    Toyotasold = ToyotaDF.Sales_in_thousands.sum()
    Nissansold = NissanDf.Sales_in_thousands.sum()
    Mercedessold = MercedesDf.Sales_in_thousands.sum()
    BMWsold = BMW_DF.Sales_in_thousands.sum()

    Total_Sold = [Hondasold,Toyotasold,Nissansold,Mercedessold,BMWsold]
    Total_Sold.sort()

    print("Honda sold: ", Hondasold)
    print("Toyota sold: ", Toyotasold)
    print("Nissan sold: ", Nissansold)
    print("Mercedes sold: ", Mercedessold)
    print("BMW sold: ", BMWsold)
    print(Total_Sold)


    # Question 4: Out of all Sedans, which has the highest resale value? what about trucks?

    Sedantmp = SedansDf[['Manufacturer','Model','Year_Resale_Value']][SedansDf['Year_Resale_Value'] == SedansDf['Year_Resale_Value'].max()]
    print(Sedantmp)
    
    Trucktmp = TrucksDF[['Manufacturer','Model','Year_Resale_Value']][TrucksDF['Year_Resale_Value'] == TrucksDF['Year_Resale_Value'].max()]
    print(Trucktmp)

    # What is the peak month that the most cars were sold during 2011 and 2012?

    tmpDF = SedansDf.Months_Added.value_counts()
    print(tmpDF.index[0:2])
     



if __name__ == '__main__':
    main()