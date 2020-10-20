import csv
import matplotlib.pyplot as plt

sale_data = []
optimal_weight = 0
optimal_xaxis = []
optimal_yaxis = []

with open('csv/sample_data.csv', encoding='utf-8-sig') as data:
    sum_x = 0
    sum_y = 0
    reader = csv.DictReader(data)
    for row in reader:
        price = int(row['price'])
        sale_qty = int(row['sale_qty'])
        sale_data.append({
            'price': price,
            'qty': sale_qty,
        })
        sum_x += price
        sum_y += sale_qty
        plt.scatter(price, sale_qty)

    avg_x = sum_x / len(sale_data)
    avg_y = sum_y / len(sale_data)

    divider = 0
    diviend = 0
    for data in sale_data:
        divider += (data.get('price') - avg_x) ** 2
        diviend += (data.get('price') - avg_y) * (data.get('qty') - avg_y)

    optimal_weight = diviend / divider
    b = avg_y - (avg_x * optimal_weight)

    for price in range(10000, 100000, 1000):
        estimate_qty = optimal_weight * price + b
        optimal_xaxis.append(price)
        optimal_yaxis.append(estimate_qty)

    plt.plot(optimal_xaxis, optimal_yaxis)
    plt.show()
