def calc_offer(offers, n, product_qty):
    if product_qty <= 0 or n <= 0:
        return {}

    current_offer = offers[n-1]
    item = current_offer["item"]    
    if product_qty >= current_offer["min_qty"]:
        # Calculate how many times we can apply the current offer
        offer_count = product_qty // current_offer["min_qty"]
        
        # Calculate the offer amount for the current offer
        current_offer_amount = offer_count * current_offer["f_qty"]
        
        # Calculate the remaining quantity after applying the current offer
        remaining_qty = product_qty - (offer_count * current_offer["min_qty"])
        
        # Recursively calculate for the remaining quantity and other offers
        result = calc_offer(offers, n-1, remaining_qty)
        
        # Merge the current offer result with the recursive result
        result[item] = result.get(item, 0) + current_offer_amount
        return result
    else:
        # If we can't apply the current offer, move to the next one
        return calc_offer(offers, n-1, product_qty)

# Sort the offers by min_qty in descending order
offers = sorted([
    {"f_qty": 7, "min_qty": 50, "item": 1},
    {"f_qty": 15, "min_qty": 120, "item": 2},
    {"f_qty": 8, "min_qty": 60, "item": 2},
    {"f_qty": 13, "min_qty": 100, "item": 1},
    {"f_qty": 1, "min_qty": 10, "item": 1}
], key=lambda x: x["min_qty"])

n = len(offers)
product_qty = 200

result = calc_offer(offers, n, product_qty)
print(f"Free items: {result}")