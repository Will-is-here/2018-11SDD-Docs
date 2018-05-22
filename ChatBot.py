import json
import sys

def retrieveFile():
 try:
     with open('orderfile.txt', 'r') as f:
         orderfile = json.load(f)
 except FileNotFoundError:
     orderfile = {}
 return orderfile        
         




print("Welcome to the Dominoes Pizza Website! I'm the Pizzabot, I will be helping you with your order.");
print()
print("This is the most efficient way of ordering your Pizza's.");
print()
process = input('What would you like to do?: ');
commands = ["i want food", "i want to order food!","I want food","Iwantfood"];

while process not in commands:
  print("I'm sorry, I don't quite understand")
  process = input('What would you like to do?: ');


name = input('Before we begin, may I please have your name?: ');

while 'my name is' not in name:
  print("Sorry, I don't understand.");
  name = input("Can I have your name please?: ");

else:
  name = name.replace('my name is', '');




confirm = input('So your name is' + name + '? ');
nameshort = name[11:]

while confirm == 'no':
  print('Sorry!');
  name = input('Please enter your correct name: ');
  name = name.replace('my name is', '');
  confirm = input('So your name is ' + nameshort + '? ');

orderfile = retrieveFile()
if nameshort in orderfile:
    prevOrderList = orderfile[nameshort]
    print('Hold on a moment ' + nameshort +', you have ordered here before')
    print('You ordered: ' + str(prevOrderList))
    option = input('Would you like to CoNtInUe OrdErIng?: ')
    if option == 'no':
      exit();

else:
  name = name.replace('my name is', '');
  print('Ok.' + ' ' + name + ' ,that name is exemplemary. Lets move on.');
       
                
print()
print()
menu = {
    "meatlovers" : 5.00,
          "ham and cheese" : 5.00,
             "pepperoni" : 5.00,
             "peri peri chicken" : 5.00,
             "cheese" : 5.00,
             "three cheese" : 5.00,
             "random topping" : 7.00,
             "neapolitan" : 12.00,
             "hawaiian" : 60.00
}  
menulist = ['meatlovers','ham and cheese','hawaiian','pepperoni','peri peri chicken','cheese','three cheese','random topping','dessert','neapolitan','hawaiian']  
cart = []
print("menu")
count = 1
for item in menu:
    price = menu[item]
    print(f"> {item} - ${price}")
    count +=1


totalcost = 0
totalcount = 0
while True:
    order = input("What do you want to eat? ").lower().strip()
    if order =="":
        break    
    if order in menu:
        cost = menu[order]
        totalcost = cost + totalcost
        print(f"Thank you for ordering - {order}, that will cost {cost}, and your total is now {totalcost}")
        cart.append(order)
    else:
        print(f"What!! {order} is not in the Menu!!");
        

if nameshort in orderfile:
    previousOrderList = orderfile[nameshort];
else:
    previousOrderList = [];
    
previousOrderList.append(cart)
orderfile[name] = previousOrderList

with open ('orderfile.txt', 'w') as f:
    json.dump(orderlist, f)

if totalcost > 0:
    print(f"Ok. Your order comes to ${totalcost}")   
    print(str(cart))
    
    input("press enter")             
                
                
             
               