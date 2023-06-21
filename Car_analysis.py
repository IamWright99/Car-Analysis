import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

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
    print("Most cars sold in this month: ",tmpDF.index[0:2])
     

    #///////////////////////////////////////////////////////////////////////////////////
    plt.style.use("seaborn-darkgrid")

    y = total_AVG_DF
    x = ["Honda","Toyota","Nissan","Mercedes","BMW"]
    plt.bar(x,y)
    plt.show()

    columns = list(SedansDf.Months_Added)
    Jan = 0
    feb = 0
    mar = 0
    apr = 0
    may = 0
    jun = 0
    jul = 0
    aug = 0
    sep = 0
    oct = 0
    nov = 0
    dec = 0
    for i  in columns:
        if i == 1:
            Jan += 1
        if i == 2:
            feb += 1
        if i == 3:
            mar += 1
        if i == 4:
            apr += 1
        if i == 5:
            may += 1
        if i == 6:
            jun += 1
        if i == 7:
            jul += 1
        if i == 8:
            aug += 1
        if i == 9:
            sep += 1
        if i == 10:
            oct += 1
        if i == 11:
            nov += 1
        if i == 12:
            dec += 1
        
    month_count = [Jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec]
    yy = month_count
    xx = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]

    plt.bar(xx,yy)
    plt.savefig("fig.pdf")
    plt.show()
    

            
    y2 = Total_Sold
    plt.bar(x,y2)
    plt.savefig("fig2.pdf")
    plt.show()

    SedansDf2= SedansDf[['Manufacturer','Model','Year_Resale_Value']][SedansDf['Year_Resale_Value'] >= 50.4]
    print(SedansDf2)

    plt.figure(figsize = (10,10))
    x_coords = list(ToyotaDF["Latest_Launch"])
    y_coords = list(ToyotaDF["Sales_in_thousands"])
    model = list(ToyotaDF['Model'])

    for i,model in enumerate(model):
        x = x_coords[i]
        y = y_coords[i]
        plt.scatter(x,y, marker='x', color='red')
        plt.text(x, y+0.3, model, fontsize=9)
        plt.savefig("fig3.pdf")
        plt.xticks(np.arange(0,len(ToyotaDF),1), fontsize = 8)
        plt.yticks(fontsize = 8)
    plt.show()
    #///////////////////////////////////////////////////////////////////////////////////





if __name__ == '__main__':
    main()