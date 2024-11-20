def restock_inventory(available_items, inventory_records, current_day):
    if current_day % 7 == 0:
        available_items = 2000
        inventory_records.append((current_day, 0, available_items, available_items))

    return available_items
