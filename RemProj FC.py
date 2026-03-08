import pandas as pd 
df = pd.DataFrame({
                   'Provider': ['Moncash', 'WesternUnion', 'CAM', 'Remitly', 'WorldRemit'],
                   'Fee': [2.99, 4.99, 3.50, 5.50, 6.00],
                   'Amount': [12887, 12519, 12801, 12440, 12300]
                   })


df.to_csv("remmittance_data.csv", index=False)
print(df)
print("Fees under $5")

df[df["Fee"] < 5]

df.sort_values(by="Amount", ascending=False)

best = df.loc[df["Amount"].idxmax()]
print(f"The best provider is {best['Provider']} giving {best['Amount']}")


#Today I successfully create a data frame, a fake one, next time I will make some basic analysis 


#provider,fee,amount_received
#MonCash,2.99,12887
#Western Union,4.99,125193

#CAM,3.50,12801
#Remitly,5.50,12440
#WorldRemit,6.00,12300