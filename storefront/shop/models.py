from django.db import models
from django.utils import timezone
from register.models import Customer
from warehouse.models import Product
# Create your models here.

# Purchase's status
PREPARING = 'PR'
SHIPPED = 'SH'
DELIVERED = 'DL'
SELL_ON_STORE = 'SO'

PURCHASE_STATUS = (
    (PREPARING, 'Preparing'),
    (SHIPPED, 'Shipped'),
    (DELIVERED, 'Delivered'),
    (SELL_ON_STORE, 'Sell on store'),
)

# Payment types
CASH = 'CS'
CREDIT_CARD = 'TC'
CLIP = 'CL'
ONLINE = 'OL'

PAYMENT_TYPES = (
    (CASH, 'Cash'),
    (CREDIT_CARD, 'Credit card'),
    (CLIP, 'Clip'),
    (ONLINE, 'Online'),
)

COMMISSIONS = {
    CASH: 0,
    CREDIT_CARD: 0.029,
    CLIP: 0.04,
    ONLINE: 0.029,
}

DEFAULT_TAX = 0.16


class Address(models.Model):
    name = models.CharField(max_length=100, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address_line_one = models.CharField(max_length=200)
    address_line_two = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_full_address(self):
        return ' '.join([
            self.address_line_one,
            self.address_line_two,
            self.city,
            self.zip_code,
            self.state,
            self.country
        ])


class Purchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Product)
    is_friend = models.BooleanField(default=False)
    payment_method = models.CharField(
        max_length=2,
        choices=PAYMENT_TYPES,
        default=CASH
    )
    ship_to = models.ForeignKey(Address, null=True)
    status = models.CharField(
        max_length=2,
        choices=PURCHASE_STATUS,
        default=SELL_ON_STORE
    )
    subtotal = models.DecimalField(max_digits=6, decimal_places=2)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    is_payed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=timezone.now)

    def get_subtotal(self):
        subtotal = 0
        for product in self.products:
            subtotal += product.sale_cost
        self.subtotal = subtotal
        return self.subtotal

    def get_commission(self):
        if self.payment_method == 'CS':
            pass

    def get_total(self):
        if self.payment_method == 'CS':
            pass
