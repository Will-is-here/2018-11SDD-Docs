
print("Welcome to the Dominoes Pizza Website! I'm the Pizzabot, I will be helping you with your order.");
print()
print("This is the most efficient way of ordering your Pizza's.");
print()
process = input('What would you like to do?: ');
commands = ["i want food", "i want to order food!"];

while process not in commands:
  print("I'm sorry, I don't quite understand")
  process = input('What would you like to do?: ');


name = input('Before we begin, may I please have your name?: ');

while 'my name is' not in name:
  print("I'm sorry, I don't quite understand.");
  name = input("May I please have your name?: ");

else:
  name = name.replace('my name is', '');




confirm = input('So your name is' + name + '? ');
nameshort = name[11:]

while confirm == 'no':
  print('Sorry!');
  name = input('Please enter your correct name: ');
  name = name.replace('my name is', '');
  confirm = input('So your name is ' + nameshort + '? ');




else:
  name = name.replace('my name is', '');
  print('Ok.' + ' ' + name + ' ,that name is satisfactory. Lets move on.');
       
file = open("orders.txt","r+")
filea = file.read()
print (filea)
                
print()
print()
menu = {
    "meatlovers" : 3.00,
    "ham and cheese" : 5.00,
    "pineapple" : 60.00
}  
menulist = ['meatlovers','ham and cheese','pineapple']  
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
    order = input("Anything you want to eat? ").lower().strip()
    if order =="":
        break    
    if order in menu:
        cost = menu[order]
        totalcost = cost + totalcost
        print(f"Thank you for ordering - {order}, that will cost {cost}, and your total is now {totalcost}")
        cart.append(order)
    else:
        print(f"What!! {order} is not in the Menu!!")
        

if totalcost > 0:
    print(f"Ok. Your order comes to ${totalcost}")   
    print(str(cart))
    
    input("press enter")             
                
                
             
               