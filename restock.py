def restock_inventory(available_items, inventory_records, current_day):
    
    if current_day == 0:
        #Ensuring both available items and restocked items are set to 2000, due to it being the first day and restocking day.
        available_items = 2000
        restocked_units =  2000
        inventory_records.append((current_day, 0, restocked_units, available_items))


    #The If statement checks if the current_day is a multiple of 7
    if current_day % 7 == 0:
        #This equation shows the amount of items used to replenish the available_items to 2000
        restocked_units = 2000 - available_items

        #Available_item is set to 2000
        available_items = 2000
        #The data's output on restocking day, will be: the restocked units and the available items.
        inventory_records.append((current_day, 0, restocked_units, available_items))
        
    return available_items

