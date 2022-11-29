from validate_docbr import CPF, CNPJ
from abc import abstractmethod, ABC


class Document(ABC):
    @staticmethod
    def factory(document_number):
        if len(document_number) == DocCpf.DOCUMENT_SIZE:
            return DocCpf(cpf_number=document_number)
        elif len(document_number) == DocCnpj.DOCUMENT_SIZE:
            return DocCnpj(cnpj_number=document_number)
        else:
            raise ValueError(f"Failed with number of digits: 11 - CPF or 14 - CNPJ."
                             f" {document_number = } {len(document_number) = }")

    def __init__(self, document_size, document_helper, document_number):
        self._document_size = document_size
        self._document_helper = document_helper
        if self.validate(document_number):
            self._document_number = document_number
        else:
            raise ValueError(f"Invalid document number: {document_number} with len of {len(document_number)}")

    def __str__(self):
        return f"{self.mask()}"

    def __repr__(self):
        return f">> Type: {type(self)} -- doc number: {self.document_number} <<"

    @property
    def document_size(self):
        return self._document_size

    @property
    def document_helper(self):
        return self._document_helper

    @property
    def document_number(self):
        return self._document_number

    @abstractmethod
    def manual_mask(self):
        pass

    def validate(self, document_number):
        if len(document_number) == self._document_size:
            valid = self.document_helper.validate(document_number)
        else:
            raise ValueError(f"Length of document is incorrect!! {len(document_number) = } "
                             f"for {document_number = }")

        return valid

    def mask(self):
        return self._document_helper.mask(self.document_number)


class DocCpf(Document):
    DOCUMENT_SIZE = 11

    def __init__(self, cpf_number):
        super(DocCpf, self).__init__(document_number=cpf_number, document_size=DocCpf.DOCUMENT_SIZE, document_helper=CPF())

    def manual_mask(self):
        return f"{self.document_number[:3]}.{self.document_number[3:6]}.{self.document_number[6:9]}-{self.document_number[9:]}"


class DocCnpj(Document):
    DOCUMENT_SIZE = 14

    def __init__(self, cnpj_number):
        super(DocCnpj, self).__init__(document_number=cnpj_number, document_size=DocCnpj.DOCUMENT_SIZE, document_helper=CNPJ())

    def manual_mask(self):
        return f"{self.document_number[:3]}.{self.document_number[3:6]}.{self.document_number[6:9]}/{self.document_number[9:13]}-{self.document_number[13:]}"
