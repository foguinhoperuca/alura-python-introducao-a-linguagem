import logging
import re
from datetime import datetime, timedelta
from time import sleep

from util import Util
from pybr.document import Document, DocCpf, DocCnpj
from pybr.phone import Landline, Mobile, GenericPhone
from pybr.dates_br import DateBr
from pybr.cep import SearchAddress



def cpf_validation():
    cpf_input = str(15316264754)
    cpf_doc = DocCpf(cpf_number=cpf_input)
    print(f"{cpf_doc = }")
    print(Util.info(cpf_doc))
    print(Util.warning(cpf_doc.manual_mask()))
    print(Util.debug(cpf_doc.mask()))

    try:
        cpf_another_input = str(2568947534)
        cpf_doc_another = DocCpf(cpf_number=cpf_another_input)
        print(f"{cpf_doc_another.validate(cpf_another_input) = }")
    except Exception as e:
        print(f"Got some error as indicate in: {Util.critical(e)}")

    try:
        cpf_incorrect = str(11111111112)
        doc_cpf_incorrect = DocCpf(cpf_number=cpf_incorrect)
        print(doc_cpf_incorrect)
    except Exception as e:
        print(f"INCORRECT CPF: {Util.critical(e)}")


def cnpj_validation():
    cnpj_input = '35379838000112'
    cnpj_doc = DocCnpj(cnpj_number=cnpj_input)
    print(cnpj_input)
    print(f"{cnpj_doc = }")
    print(Util.warning(cnpj_doc.manual_mask()))
    print(Util.info(cnpj_doc))

    try:
        cpf_doc_minor = DocCnpj(cnpj_number=str(3537983800011))
        print(f"{cpf_doc_minor.validate(cpf_doc_minor) = }")
    except Exception as e:
        print(f"Got some error as indicate in: {Util.critical(e)}")

    try:
        doc_cnpj_incorrect = DocCnpj(cnpj_number=str(11111111111111))
        print(doc_cnpj_incorrect)
    except Exception as e:
        print(f"INCORRECT CNPJ: {Util.critical(e)}")


def doc_factory_test():
    doc_factory_cnpj = Document.factory(document_number='35379838000112')
    print(type(doc_factory_cnpj))
    doc_factory_cpf = Document.factory(document_number='15316264754')
    print(type(doc_factory_cpf))

    try:
        doc_factory_error = Document.factory(document_number='353798380001')
        print(doc_factory_error)
    except Exception as e:
        print(f"Got some error as indicate in: {Util.critical(e)}")

    try:
        doc_factory_error = Document.factory(document_number='11122233344')
        print(doc_factory_error)
    except Exception as e:
        print(f"Got some error as indicate in: {Util.critical(e)}")


def email_pattern():
    print("************************************************")
    pattern = '[0-9][a-z][0-9]'
    text = '123 1a2 1cc aa1'
    response = re.search(pattern, text)
    print(response)
    print(response.group())
    print("---------")
    pattern = '[0-9][a-z]{2}[0-9]'
    text = '123 1ac2 1cc aa1'
    response = re.search(pattern, text)
    print(response)
    print(response.group())
    print("---------")
    pattern_email = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
    email = 'aaabbbcc rodrigo123@gmail.com.br'
    response_email = re.search(pattern_email, email)
    print(response_email)
    print(response_email.group())
    print("---------")
    pattern_email_br = "\w{5,50}@[a-z]{3,10}.com.br"
    email_br = "aaabbbcc rodrigo123@gmail.com.br ccbbbaaa"
    response_email_br = re.search(pattern_email_br, email_br)
    print(response_email_br)
    print(response_email_br.group())
    print("---------")


def phone_local_validation():
    phone_mask = "(99)99999-9999"
    pattern = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
    phone = "I would like to call 15998453714 some day soon. May I will call 1136332175."
    response = re.search(pattern, phone)
    print(Util.warning(phone))
    print(Util.warning(phone_mask))
    print("................................................................................")
    print(Util.debug(response))
    print(Util.info(response.group()))
    print("................................................................................")
    response_all = re.findall(pattern, phone)
    print(Util.debug(response_all))
    print(Util.info(response_all))


def phone_custom_test_regex():
    # telefone = "05521926481234"
    telefone = "05521926481234 lalalala 04470997856411"
    padrao = "([0-9]{2,3})([0-9]{2})([0-9]{4,5})([0-9]{4})"
    resposta = re.findall(padrao, telefone)
    print(resposta)
    print(resposta[1][0])
    print("++++++++++++++++++")
    telefone = "0552126481234"
    padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
    resposta = re.search(padrao, telefone)
    print(resposta.group(0))
    print(resposta.group(1))
    print(resposta.group(2))
    print(resposta.group(3))
    print(resposta.group(4))
    print("++++++++++++++++++")


def phone_validation():
    try:
        print(Landline(phone_number="1136332175"))
    except Exception as e:
        print(f"Got some error as indicate in: {Util.critical(e)}")
    try:
        print(Mobile(phone_number="15998453714"))
    except Exception as e:
        print(f"Got some error as indicate in: {Util.critical(e)}")
    try:
        phone_error = Landline(phone_number='153232358e')
        print(phone_error)
    except Exception as e:
        print(f"Got some error as indicate in: {Util.critical(e)}")
    print(Landline(phone_number="0551136332175"))
    print(Mobile(phone_number="10915998453714"))
    print(GenericPhone(phone_number="05511536332175"))
    print(GenericPhone(phone_number="15932323023"))
    print(GenericPhone(phone_number="0551932323023"))


def datebr_test(sleeptime=1):
    dt = DateBr()
    print(dt)
    print(dt.month())
    print(dt.weekday())
    print("---------------------")
    print(dt.register_datetime)
    print(type(dt.register_datetime))
    print("---------------------")
    print(dt.format())
    print(dt.format(fmt_type="BR"))
    print("---------------------")
    today = datetime.today()
    tomorrow = datetime.today() + timedelta(days=1, hours=3)
    print(today)
    print(tomorrow)
    print(tomorrow - today)
    print(today - tomorrow)
    print(f"--------------------- sleeping by {sleeptime} ---------------------")
    sleep(sleeptime)
    print(dt.since())


if __name__ == "__main__":
    print("**********************************")
    print("|| Python Brazil - Brasilidades ||")
    print("**********************************")
    logging.basicConfig(level=logging.DEBUG, format=Util.LOG_FORMAT_DEBUG)
    # logging.basicConfig(level=logging.INFO, format=Util.LOG_FORMAT_SIMPLE)

    # cpf_validation()
    # print("************************************************")
    # cnpj_validation()
    # print("************************************************")
    # doc_factory_test()
    # email_pattern()
    # print("************************************************")
    # phone_local_validation()
    # print("************************************************")
    # phone_validation()
    # print("++++++++++++++++++")
    # phone_custom_test_regex()
    # print("************************************************")
    # datebr_test(sleeptime=3)
    # print("************************************************")

    try:
        print(SearchAddress(cep="1809074A"))
    except Exception as e:
        print(f"Got some error as in {Util.debug(e)}")
    print("+++++++++++++++++++++++++")

    # addr_do_not_exist_00 = SearchAddress(cep="25800320")
    # print(Util.info(addr_do_not_exist_00))
    # print(addr_do_not_exist_00.webservice())
    # print("+++++++++++++++++++++++++")

    # addr_do_not_exist_01 = SearchAddress(cep="25870145")
    # print(Util.info(addr_do_not_exist_01))
    # print(addr_do_not_exist_01.webservice())
    # print("+++++++++++++++++++++++++")

    msr = SearchAddress(cep="18080745")
    print(Util.info(msr))
    viacep_msr = msr.webservice()
    print(viacep_msr)
    print(viacep_msr["logradouro"])
    print(viacep_msr["bairro"])
    print(viacep_msr["localidade"])
    print(viacep_msr["uf"])
    print("+++++++++++++++++++++++++")

    baltazar = SearchAddress(cep="18090380")
    print(Util.info(baltazar))
    viacep_baltazar = baltazar.webservice()
    print(baltazar.webservice())
    print(viacep_baltazar["logradouro"])
    print(viacep_baltazar["bairro"])
    print(viacep_baltazar["localidade"])
    print(viacep_baltazar["uf"])
