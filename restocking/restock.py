from api.models import OrderItem, Product
from . import supplier

def update_stock(order: OrderItem):
    product = order.item_id
    amount_bought = order.amount
    product.amount -= amount_bought
    product.save()

def check_stocks():
    print("Checking stocks...")
    products = Product.objects.all()
    order_count = 1
    for product in products:
        if product.amount <= product.threshold:
            order_dict = {"product_id": product.order_id, "order_id": order_count, "nr_of_products": 100}
            supplier.add_to_orderline(order_dict)
            order_count += 1
    supplier.place_orders(order_count)
    supplier.handle_deliveries()
    print("Stocks checked!")
