from abc import ABC, abstractmethod
from typing import Self


class Printer(ABC):
    @abstractmethod
    def print_doc(self: Self, doc: str = '') -> None:
        ...


class Scanner(ABC):
    @abstractmethod
    def digitalize_doc(self: Self) -> None:
        ...


class Fax(ABC):
    @abstractmethod
    def send_doc_by_fax(self: Self) -> None:
        ...


class OldPrinter(Printer):
    def print_doc(self: Self, doc: str = '') -> None:
        print(f'PRINTING Old printer: {doc}')


class ModernPrinter(Printer, Scanner):
    def print_doc(self: Self, doc: str = '') -> None:
        print(f'PRINTING Modern printer: {doc}')

    def digitalize_doc(self: Self, doc: str = '') -> None:
        print(f'DIGITALIZE Modern printer: {doc}')


class CompletePrinter(Printer, Scanner, Fax):
    def print_doc(self: Self, doc: str = '') -> None:
        print(f'PRINTING Complete printer: {doc}')

    def digitalize_doc(self: Self, doc: str = '') -> None:
        print(f'DIGITALIZE Complete printer: {doc}')

    def send_doc_by_fax(self: Self, doc: str = '') -> None:
        print(f'SEND FAX Complete printer: {doc}')


if __name__ == '__main__':
    epson_mx80: OldPrinter = OldPrinter()
    hp_smart_tank_580: ModernPrinter = ModernPrinter()
    brother_mfc_l3780cdw: CompletePrinter = CompletePrinter()

    epson_mx80.print_doc(doc='EPSON MX-80')

    hp_smart_tank_580.print_doc(doc='HP Smart Tank 580')
    hp_smart_tank_580.digitalize_doc(doc='HP Smart Tank 580')

    brother_mfc_l3780cdw.print_doc(doc='Brother MFC L3780 CDW')
    brother_mfc_l3780cdw.digitalize_doc(doc='Brother MFC L3780 CDW')
    brother_mfc_l3780cdw.send_doc_by_fax(doc='Brother MFC L3780 CDW')
