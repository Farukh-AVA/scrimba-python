sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []

w2_day7 = input('Please input number of lemonade sold: ')

sales_w2.append(int(w2_day7)); 

sales_w1.extend(sales_w2)

sales = list(sales_w1)

max_earned = max(sales)
min_earned = min(sales)
total_earned = sum(sales)
print(max_earned)
print(min_earned)
print(total_earned) 

