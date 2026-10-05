# 1. Hello World
name = input("Enter your name: ")
print("Hello World by", name)


# 2. Profit or Loss
cost_price = float(input("\nEnter cost price: "))
selling_price = float(input("Enter selling price: "))

if selling_price > cost_price:
    print("Profit =", selling_price - cost_price)
elif selling_price < cost_price:
    print("Loss =", cost_price - selling_price)
else:
    print("No Profit, No Loss")


# 3. Odd or Even
num = int(input("\nEnter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 4. Voting Eligibility
age = int(input("Enter your age: "))

if age < 0 or age > 120:
    print("Invalid age")
elif age >= 18:
    print("Eligible for voting")
else:
    print("Not eligible for voting")

# 5. Anagram
word1 = input("\nEnter first word: ")
word2 = input("Enter second word: ")

if sorted(word1.lower()) == sorted(word2.lower()):
    print("Anagram")
else:
    print("Not an Anagram")