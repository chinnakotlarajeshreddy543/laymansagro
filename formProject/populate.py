import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'formProject.settings')
import django
django.setup()
from faker import Faker
from formApp.models import Products
import random

def populate(n):
    f=Faker()
    for i in range(n):
        pname=f.name()
        no=random.randint(100,1000)
        details=f.name()
        addr=f.address()
        product_details=Products.objects.get_or_create(pname=pname,pno=no,pdetails=details,paddr=addr)
populate(10)
