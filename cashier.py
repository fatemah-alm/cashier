def get_invoice_items(items):
    # Items is a dictionary with a quantity and price key, and a name key
    # Return a list of all the invoice line items in the following format:
    # quantity name subtotal currency
    # For example, if we had the following:
    # [
    #   {'name': 'Apple', 'quantity': 1, price: 0.2 },
    #   {'name': 'Orange', 'quantity': 4, price: 0.3 },
    # ]
    # We should return the following:
    # ['1 Apple 0.200KD', '4 Orange 1.200KD']
    # ---
    # Write your code here
    invoice_items = []
    for i in items:
       name = i['name']
       quantity = i['quantity']
       totalPrice = int(quantity)*float(i['price'])
       invoice_items.append(str(quantity) + ' ' + name + ' ' + str(totalPrice) + 'KD')

    return invoice_items

    ...


def get_total(items):
    # Items is a dictionary with a quantity and price key
    # Calculate the total of all items in the cart
    # Write your code here
    total = 0
    for i in items:
        total = total + float(i['price'])*int(i['quantity'])
    
    return total

    ...


def print_receipt(invoice_items, total):
    # invoice_items will be the list of formatted items received from
    # `get_invoice_items`, and total will be a float. Print out a nice receipt
    # displaying a title, all the invoice items on separate lines, and the
    # total at the end.
    # ---
    # Write your code here
    print('------------------\nreceipt: \n------------------')
    for i in invoice_items:
     print(i)

    print('Total Price: ' + str(total) + 'KD')
    ...


def main():
    # Write your main logic here
    items = []

    while True:
        item_name = input('Item (enter "done" when finished): ')
        if (item_name == 'done'):
            break  
        price = input('Price: ')
        quantity = input('Quantity: ')
        
        item = {}
        item['name'] = item_name
        item['price'] = price
        item['quantity'] = quantity
        items.append(item)
        

    total = get_total(items)
    invoice_items = get_invoice_items(items)
    print_receipt(invoice_items, total)


    ...


if __name__ == "__main__":
    main()
