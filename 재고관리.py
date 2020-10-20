Buy = [int(i) for i in input().split()]
Sell = [int(i) for i in input().split()]
Stock=[]
tot = 0

Stock.append(Buy[0]-Sell[0])
for i in range(1, len(Buy)):
    Stock.append(Stock[i-1]+Buy[i]-Sell[i])

if len(Sell) < 4:
    for i in Sell:
        tot += i
    avr = tot / len(Sell)

else:
    for i in range(-4, 0, 1):
        tot += Sell[i]
    avr = tot / 4

sell_Max = max(Sell)
avr_Lead = 1
max_Lead = 2
safety_Stock = (sell_Max * max_Lead) - (avr * avr_Lead)
stock_Cycle = safety_Stock / avr

buy_Recommend=round(stock_Cycle*avr - Stock[-1] + Sell[-1])
if buy_Recommend<0:
    buy_Recommend=0

print("구매량:", Buy)
print("판매량:", Sell)
print("평균 판매량:", avr)
print("재고:", Stock)
print("재고주기:", Stock[-1]/avr)
print("안전 재고:", safety_Stock)
print("안전 재고 주기:", stock_Cycle)
print("추천 구매량:", buy_Recommend)