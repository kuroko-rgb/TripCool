from django.test import TestCase
from shop.models import Contact,Orders 
# Create your tests here.

class TestPruebas(TestCase):
    def setUp(self):
        Contact.objects.create(msg_id=1,name='Pablo',email='123@test.com',phone='123123',desc='Testiando 1')
        Contact.objects.create(msg_id=2,name='Juan',email='123@test.com',phone='123123',desc='Testiando 2')

    def test_contactomsg_creado(self):
        exists=Contact.objects.filter(name='Pablo').exists()
        exists2=Contact.objects.filter(msg_id=2).exists()
        self.assertEqual(exists, True)
        self.assertEqual(exists2, True)

class TestPruebas2(TestCase):
    def setUp(self):
        Orders.objects.create(order_id=1,items_json='1',name='Felipe',email='algo@test.cl',address='Las Torres',city='Viña',state='valparaiso',zip_code='2580000',phone='5241611')
        Orders.objects.create(order_id=2,items_json='2',name='jose',email='siempre@test.cl',address='Los alamos',city='Peru',state='Santiago',zip_code='2530000',phone='5487457')

    def test_contacto_creado(self):
        exists=Orders.objects.filter(name='Felipe').exists()
        exists2=Orders.objects.filter(order_id=2).exists()
        self.assertEqual(exists, True)
        self.assertEqual(exists2, True)
