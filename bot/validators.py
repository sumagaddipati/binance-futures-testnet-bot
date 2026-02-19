def validate_inputs(order_type, quantity, price):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    if order_type == "LIMIT" and price is None:
        raise ValueError("Price is required for LIMIT orders")

    if price is not None and price <= 0:
        raise ValueError("Price must be greater than 0")
