


import pandas as pd 

amount = float(input("Enter amount you want to send: "))

df = pd.DataFrame({
                   'Provider': ['Moncash', 'WesternUnion', 'CAM', 'Remitly', 'WorldRemit'],
                   'Fee': [2.99, 4.99, 3.50, 5.50, 6.00],
                   'Rate': [129, 133, 132, 134, 135]
                   })



df['net_amount'] = (amount - df['Fee']) * df['Rate'] 
df = df.sort_values(by = "net_amount", ascending=False).reset_index(drop = True)
df.index = df.index + 1
print("Ranking Best Provider ")
print(df[['Provider', 'Fee', 'Rate', 'net_amount']])




df.to_csv("remmittance_data.csv", index=False)
print(df)
print("Fees under $5")

df[df["Fee"] < 5]

df.sort_values(by="Amount", ascending=False)

best = df.loc[df["Amount"].idxmax()]
print(f"The best provider is {best['Provider']} giving {best['Amount']}")