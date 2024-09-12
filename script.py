import codecademylib3
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
print(visits)
print(cart)
print(checkout)
print(purchase)

visits_cart_left = pd.merge(visits,cart,how='left')
num_visitors = len(visits_cart_left)
print(num_visitors)
num_cart_time_null = len(visits_cart_left[visits_cart_left.cart_time.isnull()])
print(num_cart_time_null)
print("Percent of users visted website but did not buy = "+ str(100*(float(num_cart_time_null))/num_visitors)+"%")

cart_checkout_left = pd.merge(cart,checkout,how='left')
print(cart_checkout_left)
num_to_cart = len(cart_checkout_left)
print(num_to_cart)
num_checkout_time_null = len(cart_checkout_left[cart_checkout_left.checkout_time.isnull()])
print(num_checkout_time_null)
print("Percent of users added to cart and didnot go to checkout = "+ str(100*(float(num_checkout_time_null))/num_to_cart)+"%")

all_data = visits.merge(cart,how='left').merge(checkout,how='left').merge(purchase,how='left')
#print(all_data.head())

checkout_purchase_left = pd.merge(checkout,purchase,how='left')
#print(checkout_purchase_left)
num_to_checkout = len(checkout_purchase_left)
print(num_to_checkout)
num_purchase_time_null = len(checkout_purchase_left[checkout_purchase_left.purchase_time.isnull()])
print(num_purchase_time_null)
print("Percent of users proceeded to checkout and didnot buy = "+ str(100*(float(num_purchase_time_null))/num_to_checkout)+"%")

all_data['time_to_purchase']=all_data.purchase_time - all_data.visit_time
print(all_data.time_to_purchase)
print(all_data.time_to_purchase.mean())