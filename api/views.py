from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer, OrderSerializer
from restocking import restock
from .models import Order, OrderItem, Product

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/products/',
            'method': 'GET',
            'body': None,
            'description': 'Returns all products'
        },
        {
            'Endpoint': '/products/id/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single products'
        },
        {
            'Endpoints': '/orders/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates a new empty cart from id'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    # serializer = ProductSerializer(products, many=True)
    # products = supplier.getProductsList()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request, pk):
    # Needs implementing
    product = Product.objects.get(EAN_13 = pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getOrders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

def createOrderItem(data: dict, order: Order):
    for key in data.keys():
        order_item = OrderItem.objects.create(
            order_id=order,
            item_id=Product.objects.get(EAN_13=data[key]['item_id']),
            amount=data[key]['amount']
        )
        restock.update_stock(order_item)
        


@api_view(['POST'])
def createOrder(request):
    data = request.data
    print(data)
    order_dict = data['Order']
    order = Order.objects.create(
        price=order_dict['price']
    )
    createOrderItem(data['Items'], order)
    serializer = OrderSerializer(order, many=False)
    return Response(serializer.data)
