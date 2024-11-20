def restock_inventory(available_items, inventory_records, current_day):
    restocked_units = 0
    #Ensuring that it ONLY restock every weeks
    if current_day % 7 == 0:
        #Displays how much units will be used to replenish the stock, at the start of each week.
        restocked_units = 2000 - available_items
        #restocking amount set to 2000 items
        available_items += restocked_units
        #Adding the details such as the current day, sold item, available items, and available units
        inventory_records.append((current_day, 0, restocked_units, available_items))
        
    return available_items

