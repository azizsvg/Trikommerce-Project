def restock_inventory(available_items, inventory_records, current_day):
    #Ensuring that it ONLY restock every weeks
    if current_day % 7 == 0:
        #restocking amount set to 2000 items
        available_items = 2000
        #Adding the details such as the current day, sold item, available items, and available units
        inventory_records.append((current_day, 0, available_items, available_items))

    return available_items
