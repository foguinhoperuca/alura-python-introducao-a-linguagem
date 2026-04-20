from abc import ABC, abstractmethod
from typing import Self


class Generator(ABC):
    @abstractmethod
    def generate(self: Self, content: str) -> None:
        ...


class PDFGenerator(Generator):
    def generate(self: Self, content: str) -> None:
        print(f'Generating PDF with content: {content}')


class HTMLGenerator(Generator):
    def generate(self: Self, content: str) -> None:
        print(f'Generating HTML with content: {content}')


class ExcelGenerator(Generator):
    def generate(self: Self, content: str) -> None:
        print(f'Generating EXCEL with content: {content}')


class ODSGenerator(Generator):
    def generate(self: Self, content: str) -> None:
        print(f'Generating ODS with content: {content}')


class FileConvert:
    def __init__(self: Self, generator: Generator) -> None:
        self._generator: Generator = generator

    def convert(self: Self, content: str) -> None:
        self._generator.generate(content=content)


if __name__ == '__main__':
    CONTENT: str = 'Testing file convert...'

    pdf_convert: FileConvert = FileConvert(generator=PDFGenerator())
    pdf_convert.convert(content=CONTENT)

    html_convert: FileConvert = FileConvert(generator=HTMLGenerator())
    html_convert.convert(content=CONTENT)

    excel_convert: FileConvert = FileConvert(generator=ExcelGenerator())
    excel_convert.convert(content=CONTENT)

    ods_convert: FileConvert = FileConvert(generator=ODSGenerator())
    ods_convert.convert(content=CONTENT)
