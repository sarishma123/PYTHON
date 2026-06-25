price = 5000

promo = input("Enter promo code: ").upper()
member = input("Frequent Flyer Club member (yes/no): ").lower()
baggage = float(input("Enter baggage weight (kg): "))

# Apply promo code discount
if promo == "FIRSTFLIGHT":
    price = price - (price * 0.20)

# Apply frequent flyer discount
if member == "yes":
    price = price - (price * 0.20)

# Extra baggage charge
if baggage > 20:
    extra_weight = baggage - 20
    price = price + (extra_weight * 100)

print("Total Airfare Price = ₹", price)