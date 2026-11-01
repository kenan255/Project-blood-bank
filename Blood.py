print("welcome")
x = input("Enter username: ")
with open("c.txt", "a") as f:
  f.write(x + "\n")
k = int(input("Enter your age: "))
if k < 18:
    print("sorry, you are too young.")
else: n = input("Do you want to donate blood? (y/n): ")
if n.lower() == "y":
  blood = input("Enter your blood group (A+ , AB+ , etc.):")
  print("Thank you")
else:
  print("Thank you")
