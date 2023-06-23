#ask user for weight of package
#weight = int(input("How much does your package weigh? "))

# Set weight
weight = 5

#Calculate prices based on weight
#Ground shipping
if weight <= 2:
  ground_price = 20 + 1.5*weight
elif weight <= 6:
  ground_price = 20 + 3*weight
elif weight <= 10:
  ground_price = 20 + 4*weight
else:
  ground_price = 20 + 4.75*weight

print(f"Ground Shipping Price: ${ground_price}")

#Ground Premium Shipping
ground_premium = 125
print(f"Ground Premium Shipping Price: ${ground_premium}")

#Drone Shipping
if weight <= 2:
  drone_price = 4.50*weight
elif weight <= 6:
  drone_price = 9*weight
elif weight <= 10:
  drone_price = 12*weight
else:
  drone_price = 14.25*weight
print(f"Drone Shipping Price: ${drone_price}")

print("")
print("")

#Tell user which shipping method is least expensive
if ground_price < ground_premium and ground_price < drone_price:
  print(f"You should use Ground Shipping. It will cost ${ground_price}.")
elif ground_premium < ground_price and ground_premium < drone_price:
  print(f"You should use Ground Shipping Premium. It will cost ${ground_premium}.")
else:
  print(f"You should use Drone Shipping. It will cost ${drone_price}.")
