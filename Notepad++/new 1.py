menu = {
	"pizza" : 3.40,
	"tacos" : 5.60,
	"curry chocken" : 13.00
}	
print("menu")
count = 1
for item in menu:
	price = menu[item]
	print(f"> {item} - ${price}")
	count +=1

totalcount = 0
while True:
	order = input("What do you want to eat?").lower().strip()
	if order =="":
		break	
	if order in menu:
		cost = menu[order]
		totalcost += cost
		print(f"Thank you for ordering - {order}, that will cost {cost}, and your total is now {totalcost}")
	else:
		print(f"What!! {order} is not in the Menu!!)
		

if totalcost > 0:
	print(f"Thanks...you owe me ${totalcost}