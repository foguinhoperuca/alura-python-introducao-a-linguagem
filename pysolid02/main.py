import argparse
from decimal import Decimal
import sys

from util import init_logger
from domain.entities import Client, Order, Product, ProductType
from domain.service import EmailService, InvoiceService, ISS, ICMS, IVA


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='[ALURA] py solid 02')
    parser.add_argument('--run', choices=['main', 'chap01'], help='View availiable: [main | chap01]')
    args = parser.parse_args()

    logger = init_logger(log_type='normal')

    if args.run == 'main':
        print('Then run main system...')
    elif args.run == 'chap01':
        mariah: Client = Client(name='Mariah Jhonnes', email='mary.jhonnes@alura.com.br')
        book: Product = Product(sku='102030', name='How to Program in Python by Alura', price=round(Decimal('39.99'), 2), quantity=5, prod_type=ProductType.DIGITAL)
        notebook: Product = Product(sku='405060', name='Simple notebook to annotate everything', price=round(Decimal('19.99'), 2), quantity=10, prod_type=ProductType.PHYSICAL)
        order: Order = Order(client=mariah)
        order.add(book)
        order.add(notebook)
        invoice_service: InvoiceService = InvoiceService(order=order, taxes=[ISS(), ICMS(), IVA()])
        EmailService.send(recipient=mariah.email, subject='Your Invoice.', message=invoice_service.generate_document())
    else:
        print('No run...')
        sys.exit(1)

    sys.exit(0)
