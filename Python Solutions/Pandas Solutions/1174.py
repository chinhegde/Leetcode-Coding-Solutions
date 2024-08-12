# https://leetcode.com/problems/immediate-food-delivery-ii/

import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:

    first_orders = delivery.loc[delivery.groupby(by='customer_id')['order_date'].idxmin()]
    first_orders['delivery'] = ['Immediate' if i['order_date'] == i['customer_pref_delivery_date'] else 'Scheduled' for ind, i in first_orders.iterrows()]

    return pd.DataFrame({'immediate_percentage': [len(first_orders[first_orders['delivery'] == 'Immediate'])*100/len(first_orders)]}).round(2)