from django.shortcuts import render
from django.db.models import Q, F, Func, Count, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.db.models.aggregates import Max, Min, Avg, Sum
from django.db.models import Value
from django.contrib.contenttypes.models import ContentType
from tags.models import TaggedItem
from django.db import transaction, connection

from store.models import Product, OrderItem, Order, Customer, Collection


def say_hello(request):
    # queryset = Product.objects.filter(Q(inventory__lt=10) | ~Q(unit_price__lt=20))
    # queryset = Product.objects.filter(inventory=F('unit_price'))
    # queryset = Product.objects.order_by('unit_price', '-title').reverse()
    # product = Product.objects.order_by('unit_price')[0]
    # product = Product.objects.earliest('unit_price')
    # queryset = Product.objects.all()[5:10]
    # queryset = Product.objects.values_list('id', 'title', 'collection__title')
    # queryset = Product.objects.filter(
    #     id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    # queryset = Product.objects.only('id', 'title')
    # queryset = Product.objects.defer('description')
    # queryset = Product.objects.prefetch_related('promotions').select_related('collection').all()
    # queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

    # result = Product.objects.filter(collection_id=1).aggregate(count=Count('id'), min_price=Min('unit_price'))
    # queryset = Customer.objects.annotate(new_id=F('id') + 1)
    # queryset = Customer.objects.annotate(
    #     fullname=Func(F('first_name'), Value(
    #         ''), F('last_name'), function='CONCAT')
    # )

    # queryset = Customer.objects.annotate(
    #     fullname=Concat('first_name', Value(' '), 'last_name')
    # )
    # number of orders each customers had placed
    # queryset = Customer.objects.annotate(
    #     order_count=Count('order')
    # )
    # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    # queryset = Product.objects.annotate(
    #     discounted_price=discounted_price
    # )

    # content_type = ContentType.objects.get_for_model(Product)

    # queryset = TaggedItem.objects \
    #     .select_related('tag') \
    #     .filter(
    #         content_type=content_type,
    #         object_id=1
    #     )

    # queryset = TaggedItem.objects.get_tags_for(Product, 1)

    # collection = Collection.objects.get(pk=11)
    # collection.title = "Games"
    # collection.featured_product = None
    # collection.save()

    # collection = Collection.objects.create(title="jjj", featured_product_id=1)
    # Collection.objects.filter(pk=11).update(featured_product=None)

    # collection = Collection(pk=11)
    # collection.delete()

    # Collection.objects.filter(id__gt=5).delete()
    # queryset = Product.objects.raw('SELECT * FROM store_product')
    
    # cursor = connection.cursor()
    # cursor.execute('SELECT * FROM store_product')
    # cursor.close()
    
    # with connection.cursor() as cursor:
    #     cursor.callproc('get_customers', [1, 2,'a'])

    return render(request, 'hello.html', {'name': 'Mosh', 'results': list(queryset)})
