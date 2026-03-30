
#This is the very most basic prototype version where I manually implement the computation of the net value
#Using fake datas 

amount = float(input("Enter amount of money to transfer: "))

Provider = {
    "Name" : ["Moncash", "Cam", "Tap Tap send"],
    "Fee" : [5, 4, 8],
    "Rate" : [132, 131, 135]
} 

results = []


for i in range(len(Provider["Name"])):
    name = Provider["Name"][i]
    fee = Provider["Fee"][i]
    rate = Provider["Rate"][i]
    net_amount = (amount - fee) * rate
    results.append((name, net_amount))

results.sort(key = lambda x: x[1], reverse=True)

for name, net in results:
    best = "(best)" if net == results[0][1] else ""
    print(f"{name}: {net} HTG {best}")


        