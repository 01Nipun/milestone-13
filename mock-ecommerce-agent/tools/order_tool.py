import json

def get_order_status(order_id):
    with open("data/orders.json") as f:
        orders = json.load(f)

    for order in orders:
        if str(order["id"]) == str(order_id):
            return f"Order {order_id} is {order['status']}"

    return "Order not found"