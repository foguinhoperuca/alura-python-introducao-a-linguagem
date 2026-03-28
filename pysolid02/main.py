import argparse
from decimal import Decimal
import sys

from util import init_logger
from domain.entities import Client, Order, Product, ProductType, ShippingType
from domain.service import ApplyDiscountStrategy, BirthdayDiscountStrategy, LoyaltyDiscountStrategy, EmailService, InvoiceService, ISS, ICMS, IVA


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='[ALURA] py solid 02')
    parser.add_argument('--run', choices=['main', 'chap01', 'exerc_ch_02'], help='View availiable: [main | chap01]')
    args = parser.parse_args()

    logger = init_logger(log_type='normal')

    if args.run == 'main':
        print('Then run main system...')
    elif args.run == 'chap01':
        mariah: Client = Client(name='Mariah Jhonnes', email='mary.jhonnes@alura.com.br')
        book: Product = Product(sku='102030', name='How to Program in Python by Alura', price=round(Decimal('39.99'), 2), quantity=5, prod_type=ProductType.DIGITAL)
        notebook: Product = Product(sku='405060', name='Simple notebook to annotate everything', price=round(Decimal('19.99'), 2), quantity=10, prod_type=ProductType.PHYSICAL)
        order: Order = Order(client=mariah, shipping_type=ShippingType.EXPRESS)
        order.add(book)
        order.add(notebook)
        invoice_service: InvoiceService = InvoiceService(order=order, taxes=[ISS(), ICMS(), IVA()])
        EmailService.send(recipient=mariah.email, subject='Your Invoice.', message=invoice_service.generate_document())
    elif args.run == 'exerc_ch_02':
        product_price: Decimal = round(Decimal('100.00'), 2)
        print(f'[$100.00] Birthday Discount..: {ApplyDiscountStrategy(strategy=BirthdayDiscountStrategy()).apply_discount(value=product_price)}')
        print(f'[$100.00] Loyalty Discount...: {ApplyDiscountStrategy(strategy=LoyaltyDiscountStrategy()).apply_discount(value=product_price)}')
        print('----- </$100.00> -----')

        product_price = round(Decimal('300.00'), 2)
        print(f'[$300.00] Birthday Discount..: {ApplyDiscountStrategy(strategy=BirthdayDiscountStrategy()).apply_discount(value=product_price)}')
        print(f'[$300.00] Loyalty Discount...: {ApplyDiscountStrategy(strategy=LoyaltyDiscountStrategy()).apply_discount(value=product_price)}')
        print('----- </$300.00> -----')

        product_price = round(Decimal('400.00'), 2)
        print(f'[$400.00] Birthday Discount..: {ApplyDiscountStrategy(strategy=BirthdayDiscountStrategy()).apply_discount(value=product_price)}')
        print(f'[$400.00] Loyalty Discount...: {ApplyDiscountStrategy(strategy=LoyaltyDiscountStrategy()).apply_discount(value=product_price)}')
        print('----- </$400.00> -----')

        product_price = round(Decimal('500.00'), 2)
        print(f'[$500.00] Birthday Discount..: {ApplyDiscountStrategy(strategy=BirthdayDiscountStrategy()).apply_discount(value=product_price)}')
        print(f'[$500.00] Loyalty Discount...: {ApplyDiscountStrategy(strategy=LoyaltyDiscountStrategy()).apply_discount(value=product_price)}')
        print('----- </$500.00> -----')
    else:
        print('No run...')
        sys.exit(1)

    sys.exit(0)
