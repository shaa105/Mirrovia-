import datetime
from typing import List, Dict

# Sample product dataset (simulating live e-commerce data)
product_database = [
    {
        "id": 1,
        "name": "Summer Floral Dress",
        "price": 120,
        "size": "M",
        "color_tone": "warm",
        "location": "Dubai",
        "stock": True,
        "delivery_days": 3
    },
    {
        "id": 2,
        "name": "Cool Grey Blazer",
        "price": 350,
        "size": "L",
        "color_tone": "cool",
        "location": "Dubai",
        "stock": True,
        "delivery_days": 5
    },
    {
        "id": 3,
        "name": "Neutral Toned Scarf",
        "price": 50,
        "size": "Free",
        "color_tone": "neutral",
        "location": "Abu Dhabi",
        "stock": True,
        "delivery_days": 2
    }
]

def get_user_input():
    return {
        "budget": 200,
        "figure_size": "M",
        "color_tone": "warm",
        "location": "Dubai",
        "delivery_deadline": datetime.datetime.now() + datetime.timedelta(days=4)
    }

def match_products(user_input: Dict, products: List[Dict]) -> List[Dict]:
    matched = []
    for product in products:
        delivery_date = datetime.datetime.now() + datetime.timedelta(days=product["delivery_days"])
        if (
            product["stock"] and
            product["price"] <= user_input["budget"] and
            (product["size"] == user_input["figure_size"] or product["size"] == "Free") and
            product["color_tone"] == user_input["color_tone"] and
            product["location"] == user_input["location"] and
            delivery_date <= user_input["delivery_deadline"]
        ):
            matched.append(product)
    return matched

def display_matches(matches: List[Dict]):
    if not matches:
        print("No products match your preferences.")
    else:
        print("Matched Products:")
        for product in matches:
            print(f"- {product['name']} (AED {product['price']}) - Deliver in {product['delivery_days']} days")

if __name__ == "__main__":
    user_input = get_user_input()
    matched_products = match_products(user_input, product_database)
    display_matches(matched_products)
