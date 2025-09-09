from pyscript import display

# String
restaurant_name = "Pastee Co."
owner_name = "Shia Cruz"
bestseller = "Pasteeccino"

# Integer
year_established = 2024

# Tuple
business_hours = ("9:00 AM", "8:00 PM")

# Boolean
has_delivery = True

# Floating Point
popular_item_price = 115.00
tax_rate = 0.08 # just extra information

# List
product_names = ["Pasteeccino","Shiloh Coffee","Pasteemisu","Pastee Cookies n' Cream Frappe","Skibs Croissant"]
menu_prices = [115.00, 95.00, 60.00, 160.00, 75.00] # these are already final with tax
common_allergens = ["dairy", "nuts", "gluten"]

allergens_text = f"Common Allergens: {common_allergens[0]}, {common_allergens[1]}, {common_allergens[2]}" # added f so it supports the expressions

# Display Restaurant Info
display(restaurant_name, target="restaurantName")
display(f"Owner: {owner_name}", target="ownerName")
display(f"Since {year_established}", target="yearEstablished")

# Display Menu
display(product_names[0], target="product1")
display(product_names[1], target="product2")
display(product_names[2], target="product3")
display(product_names[3], target="product4")
display(product_names[4], target="product5")
display(menu_prices[0], target="price1")
display(menu_prices[1], target="price2")
display(menu_prices[2], target="price3")
display(menu_prices[3], target="price4")
display(menu_prices[4], target="price5")
display(f"Bestseller: {bestseller} (₱{popular_item_price:.2f})", target="bestseller") 
# wanted to use the popular item price variable so I just did this

# Display Business Hours
display(f"Open: {business_hours[0]} - {business_hours[1]}", target="businessHours")  

# Display Delivery
if has_delivery:
    delivery_text = "🚚 Delivery Available"
else:
    delivery_text = "❌ Delivery Not Available"

display(f"{delivery_text}", target="deliveryButton")

# apparently if else works in python like it does in javascript
# so if has_delivery is true, it will say available. vice versia, unavailable.
# also i made delivery text a string because it showed {''} around it for some reason

# Display Common Allergens
display(allergens_text, target="allergens")