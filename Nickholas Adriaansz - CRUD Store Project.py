# ======================================
# Inventory Data
# ======================================

listItem = [['Pen', 20, 13000],
            ['Pencil', 15, 10000],
            ['Notebook', 25, 15000],
            ['Eraser', 30, 12000]
            ]


# ======================================
# Misc. Functions
# ======================================
def crosscheck(name):
     for item in listItem:
          if name.lower() == item[0].lower():
               return item
     return None


# ======================================
# Menu Functions
# ======================================

#Menu 1: View Items in Store
def menu1():
     print(f"{'Menu':<15} | {'Stock':<15} | {'Harga':<15}")
     for i in range(len(listItem)):
          print(f'{listItem[i][0]:<15} | {listItem[i][1]:<15} | {listItem[i][2]:<15}')

#Menu 2: Add New Item(s)
def menu2():
     while True:
          menu1()

          inputItem = input('What item would you like to add?\n')

          if crosscheck(inputItem):
               print('Data already exists!\n')
               continue
               
          else:
               inputAmount = int(input(f'How many {inputItem.title()} would you like to stock?\n'))
               inputPrice = int(input(f'How much does each {inputItem.title()} cost (in IDR)?\n'))
               
               addItem = [inputItem.title(), inputAmount, inputPrice]
               listItem.append(addItem)
               
               menu1()
               print('Data Successfully saved!\n')
               break

#Menu 3: Update an Item
def menu3():
     while True:
          menu1()

          updateItem = input('What item would you like to update?\n')
          item = crosscheck(updateItem)

          if item:
               inputAmount = int(input(f'How many {updateItem.title()} would you like to stock??\n'))
               item[1] = inputAmount + item[1]

               priceChecker = input(f"Do you also want to update the price of {updateItem.title()}? (y/n)\n")
               if priceChecker.lower() == 'y':
                    updatePrice = int(input(f'How much does each {updateItem.title()} cost (in IDR)?\n'))
                    item[2] = updatePrice

               menu1()
               print('Data Successfully saved!')
               break
               
          else:
               print("Try something else, the data you're looking for does not exist!\n")

          promptChecker = input('Would you like to update another item? (y/n)\n')
          if promptChecker.lower() == 'n':
               break

#Menu 4: Remove an Item
def menu4():
     while True:
          menu1()

          delItem = input('What item would you like to delete?:\n')
          item = crosscheck(delItem)

          if item:
               delConfirm = input(f'Are you sure you want to delete {delItem.title()} (y/n)?\n')
               if delConfirm.lower() == 'y':
                    listItem.remove(item)

                    menu1()
                    print(f'{delItem.title()} has been successfully deleted!\n')
               else:
                    print('Deletion cancelled.\n')
               break
               
          else:
               print("The data you're looking for does not exist!\n")
               
          delChecker = input('Would you like to delete another item? (y/n)\n')
          if delChecker.lower() == 'n':
               break


#Menu 5: Shop Items
def menu5():
     cart = []
     while True:
          menu1()
          
          chosenItem = (input('Which item would you like to buy today?\n'))
          item = crosscheck(chosenItem)

          if not item:
               print("The item you're looking for does not exist!\n")
               continue

          inputQty = int(input('How many would you like to buy?\n'))

          if inputQty > item[1]:
               print(f'''Apologies, requested quantity exceeds stock.
                     Only {item[1]} left.''')
          
          else:
               cart.append([item[0], inputQty, item[2]])
               item[1] -= inputQty
               print(f'{inputQty} {item[0]} added to cart.')
          
          checker = input('Would you like to buy another item? (y/n)\n')
          if checker.lower() == 'n':
               break

     print('Your Cart :')
     print('Name\t| Qty\t| Price\t| Total Price')
     totalPrice = 0

     for item in cart:
          subtotal = item[1] * item[2]
          if item[1] > 10:
               print(f'Promo Applied: 10% Off on {item[0]} (Qty: {item[1]})')
               subtotal *= 0.9
          print(f'{item[0]}\t| {item[1]}\t| IDR {item[2]}\t| IDR {subtotal}')
          totalPrice += subtotal

     while True:
          print(f'Total amount to pay: IDR {totalPrice}')
          inputMoney = int(input('Enter the amount of money you have:\n'))

          if inputMoney < totalPrice:
               shortage = totalPrice - inputMoney
               print(f'''
                    Amount paid: IDR {inputMoney}
                    Insufficient funds. You are short by: IDR {shortage}
                    Please re-enter the correct amount.
                    ''')
          elif inputMoney == totalPrice:
               print(f'''
                    Amount paid: IDR {inputMoney}
                    Thank you for your purchase
                    ''')
               break
          else:
               print(f'''
                    Amount paid: IDR {inputMoney}
                    Thank you for your purchase
                    Your change: IDR {inputMoney - totalPrice}
                    ''')
               break


#Menu 6: Current Deals!
def menu6():

     print('$$$ CURRENT DEALS $$$')
     print('-' * 60)
     print("GET 10% OFF on every product if you buy MORE THAN 10 UNITS!")
     print("Valid only for today's purchases!")
     print('-' * 60)


# ======================================
# Role-Based Menus
# ======================================

def buyermenu():
    while True:
          print('''
          Welcome to the CRUD Store
                                   
          What would you like to do today?
          1. View Items in Store
          2. Shop Items
          3. $$$ Current Deals $$$!

          0. Exit Program
          ''')
          
          inputMenu = int(input('Please input your choice (0-3): '))           

          if inputMenu == 1:
               menu1()

          elif inputMenu == 2 :
               menu5()

          elif inputMenu == 3 :
               menu6()

          elif inputMenu == 0 :
               print("Thank you for shopping with us! See you next time!")
               exit()

          else:
               print('\nThe option you entered is not valid!')

def sellermenu():
    while True:
          print('''
          Welcome to the CRUD Store
                                   
          What would you like to do today?
          1. View Items in Store
          2. Add New Item(s)
          3. Update an Item
          4. Remove an Item
          5. Shop Items
          6. $$$ Current Deals $$$!

          0. Return to Main Menu
          ''')
          
          inputMenu = int(input('Please input your choice (0-6): '))           

          if inputMenu == 1:
               menu1()

          elif inputMenu == 2 :
               menu2()

          elif inputMenu == 3 :
               menu3()

          elif inputMenu == 4 :
               menu4()

          elif inputMenu == 5 :
               menu5()

          elif inputMenu == 6 :
               menu6()

          elif inputMenu == 0 :
               print("Thank you for choosing us! See you next time!")
               return

          else:
               print('\nThe option you entered is not valid!')

# ======================================
# Main Menu
# ======================================

def mainmenu():
    while True:
          print('''
          Welcome to the CRUD Store
                                   
          Are you a:
          1. Buyer
          2. Seller (with inventory access)

          0. Exit Program
          ''')
          
          inputRole = int(input('Please input your choice (0-2): '))           

          if inputRole == 1:
               buyermenu()

          elif inputRole == 2 :
               password = input('Enter password:\n')
               if password == 'admin':
                    sellermenu()
               
               else:
                    print("Oops! That's not the right password. Returning to the main menu...\n")

          elif inputRole == 0 :
               print("Thank you for choosing us! See you next time!")
               exit()

          else:
               print('\nThe option you entered is not valid!')


# ======================================
# Run Program
# ======================================
mainmenu()