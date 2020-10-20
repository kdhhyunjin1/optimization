import csv
import matplotlib.pyplot as plt

grad_list = []
sale_data = []
m=0xFFFFFFFF
with open('csv/sample_data.csv', encoding='utf-8-sig') as data:
    reader = csv.DictReader(data)
    for row in reader:
        price = int(row['price'])
        sale_qty = int(row['sale_qty'])
        sale_data.append({
            'price': price,
            'qty': sale_qty,
        })
        plt.scatter(price, sale_qty)

    for deno in range(-100, 101):
        if deno==0:
            continue
        for nu in range(1,101):
            inc=nu/(deno*100000)
            sum=0
            for data in sale_data:
                estimate=data.get('price')*inc
                diff=estimate-data.get('qty')
                sum+=diff
            if m==-1 or m>sum:
                min_inc=inc
                m=sum

    x_axis=[]
    y_axis=[]
    for price in range(10000,100000,1000):
        estimate_qty=min_inc*price
        x_axis.append(price)
        y_axis.append(estimate_qty)

    plt.plot(x_axis, y_axis)
    plt.show()