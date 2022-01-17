# to run the reset script run 
# - python manage.py shell
# (Inside the shell) - exec(open(reset_script.py).read())

import restocking.supplier as supplier
from api.models import Product, Order, OrderItem

Product.objects.all().delete()
Order.objects.all().delete()
OrderItem.objects.all().delete()

my_dict = supplier.getProductsList()
for item in my_dict:
    p = Product(EAN_13=item['EAN_13'],
                order_id=item['id'],
                name=item['name'],
                vat_rate=item['vat_rate'],
                price_in_cents=item['price_in_cents'],
                amount=100,
                threshold=10)
    p.save()
    

