prices=[100,200,300,400,500]
final_prices=[]
for price in prices:
    final_price=price-price*0.1
    final_prices.append(final_price)
    
print(final_prices)
