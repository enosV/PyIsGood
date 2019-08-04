money_in_wallet = 40
sandwich_price = 7.50
sales_tax = 0.08 * sandwich_price

sandwich_price += sales_tax
print ("this is total cost of sandwich:"), sandwich_price

money_in_wallet -= sandwich_price
print ("this is what you have left after paying for the sandwich:"), money_in_wallet

