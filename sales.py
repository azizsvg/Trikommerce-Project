import random

def daily_sales(available_items, inventory_records, current_day):
#If current_day is NOT a multiple of 7
    if current_day % 7 != 0:
#Picks a number between 0 and 200
        sold_unit = random.randint(0, 200)
#Basically works as available_item = available_item - sold_unit
        available_items -= sold_unit

        inventory_records.append((current_day, sold_unit, 0, available_items))

    return available_items