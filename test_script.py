
import restocking.supplier as supplier
from api.models import Product

for product in Product.objects.all():
    product.amount = 11
    product.save()
print("done")


