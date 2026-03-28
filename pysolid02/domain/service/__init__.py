from domain.service.email import EmailService                                                                 # noqa: F401
from domain.service.invoice import InvoiceService, ISS, ICMS, IVA                                             # noqa: F401
from domain.service.discount import BirthdayDiscountStrategy, LoyaltyDiscountStrategy, ApplyDiscountStrategy  # noqa: F401
from domain.service.shipping import NormalShippingStrategy, ExpressShippingStrategy, EconomyShippingStrategy  # noqa: F401
