import re
from time import sleep
import logging
from util import Util
from model import ExtractorUrl, ExtractorCEP


def simple_test():
    text = 'abcde'
    print(text[0])
    print(text[1])
    print(text[2])
    print(text[3])
    print(text[4])
    print(text[-1])
    print("----------------\n")

    print(text[0:1])
    print(text[0:0])
    print(text[0:])
    print(text[0:2])
    print(text[0:5])
    print(text[0:3])
    print(text[:5])
    print("----------------\n")

    word = "abc"
    print(f"{word=} {id(word)=}")
    word = "def"
    print(f"{word=} {id(word)=}")
    try:
        word[0] = "x"
    except Exception as e:
        logging.error(e)

    sleep(1)

    list_mut = ['a', 'b', 'c']
    print(list_mut)
    list_mut[0] = 'x'
    print(list_mut)

    wordlx = "abc"
    wordly = "abc"
    print(f"{id(wordlx)=} == {id(wordly)=}? {id(wordlx) == id(wordly)=}")

    x = ['a', 'b', 'c']
    y = ['a', 'b', 'c']
    print(f"{id(x)=} == {id(y)=}? {id(x) == id(y)=}")
    print("===================================================\n")

    print(f"{text.find('c')=}")

    text02 = "I study at Alura"
    print(f"{text02.find('I')=} {text02.find('s')=} {text02.find('study')=} {text02.find('Alura')=} {len(text02)=}")


def test_exclamation_mark():
    index_exclamation = simple_url.find("!")
    if index_exclamation == -1:
        print("No exclamation mark found!")
    else:
        print(f"Found at least one exclamation mark in position {index_exclamation}")


def simple_url_slicer():
    # url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
    # print(url)

    print(f"{simple_url=} {id(simple_url)=}")
    print(f"{simple_url[0:19]=}")
    print(f"{simple_url_param=} {simple_url[20:]=}")
    print(f"{simple_url=} {id(simple_url)=}")

    index_interrogation = simple_url.find("?")
    if index_interrogation == -1:
        print("No ? found!")
    else:
        print(f"Found at least one ? in position {index_interrogation}")

    url_base = simple_url[:index_interrogation]
    url_parameter = simple_url[(index_interrogation + 1):]
    print(f"{index_interrogation=} --> { url_base=} { url_parameter=}")
    print("===================================================\n")


def alura():
    print("ALURA ------------------------------------")
    # separa base do parametro
    # url = "bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"
    url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"  # Another example
    indice_interrogacao = url.find('?')
    url_base = url[:indice_interrogacao]
    url_parametros = url[indice_interrogacao + 1:]

    # busca valor do parametro
    # parametro_busca = 'moedaDestino'
    # parametro_busca = 'moedaOrigem'
    parametro_busca = 'quantidade'

    indice_parametro = url_parametros.find(parametro_busca)
    indice_valor = indice_parametro + len(parametro_busca) + 1
    indice_e_comercial = url_parametros.find('&', indice_valor)
    if indice_e_comercial == -1:
        valor = url_parametros[indice_valor:]
    else:
        valor = url_parametros[indice_valor:indice_e_comercial]

    print(f"{url_parametros=}")
    print(f"{indice_parametro=} {indice_valor=} {indice_e_comercial=}")
    print(f"{parametro_busca=} {(len(parametro_busca))=}")
    print(f"{valor=}")


def slicer_procedural():
    simple_url = "bytebank.com/cambio?moedaOrigem=real"
    simple_url_param = simple_url[20:36]
    # simple_url_slicer()

    url_better_ordered = "bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
    url_double = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
    url_triple = "bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"
    url_empty = ""
    url_spaces = "        bytebank.com/cambio ?        moedaDestino=dolar&    quantidade=100&moedaOrigem=real                  "

    url = url_spaces
    print(f"{url=}")
    print(f"{url.strip()=}")
    url = url.strip()
    url = url.replace(" ", "")
    if url == "":
        raise ValueError("Your URL is empty.")

    url_base = url[:url.find('?')]
    params = url[(url.find("?") + 1):]
    search_param = 'moedaOrigem'
    # search_param = 'moedaDestino'
    # search_param = 'quantidade'
    param_position = params.find(search_param)
    ampersand_position = params.find('&', param_position)
    print(f"{params=} {search_param=} {params.find(search_param)=} {ampersand_position=}")

    if ampersand_position == -1:
        value = params[param_position + (len(search_param) + 1):]
    else:
        value = params[param_position + (len(search_param) + 1):ampersand_position]

    print(f"value is: {value} {len(value)=}")


def test_cep(address="Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"):
    # cep = "18090380"
    ExtractorCEP.parse(address)


def test_simple_class_extractor_url():
    extractor_url = ExtractorUrl()
    print(f"{Util.info('Extracted value is')}: {Util.info(extractor_url.get_param_value('moedaOrigem'))}")
    print(f"{Util.error('Extracted value is')}: {Util.info(extractor_url.get_param_value('moedaDestino'))}")
    print(f"{Util.warning('Extracted value is')}: {Util.info(extractor_url.get_param_value('quantidade'))}")
    print("---------------------- ERRORS ----------------------")

    # Errors
    try:
        extractor_url_none = ExtractorUrl(None)
        print(f"{Util.error('Extracted value is')}: {Util.info(extractor_url_none.get_param_value('moedaDestino'))}")
    except ValueError as e:
        print(f"Error None: {Util.warning(e)}")

    try:
        protocol = ExtractorUrl("bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100")
        print(f"{Util.info('Extracted value is')}: {Util.info(protocol.get_param_value('moedaOrigem'))}")
    except ValueError as e:
        print(f"Error protocol: {Util.warning(e)}")

    try:
        route = ExtractorUrl("http://bytebank.com/?moedaOrigem=real&moedaDestino=dolar&quantidade=100")
        print(f"{Util.info('Extracted value is')}: {Util.info(route.get_param_value('moedaOrigem'))}")
    except ValueError as e:
        print(f"route: {Util.warning(e)}")

    better_validated = ExtractorUrl("http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100")
    print(
        f"Better Validated: {better_validated.get_param_value('quantidade')} --> {ExtractorUrl.get_url_base(better_validated.url)}")


def test_url(urls_test):
    total_correct = 0
    for url_test in urls_test:
        try:
            valid_extract_url = ExtractorUrl(url=url_test)
            total_correct += 1
            print(f"{Util.error('Extracted value (for moedaOrigem) is...')}: {Util.info(valid_extract_url.get_param_value('moedaOrigem'))} --> from {Util.warning(valid_extract_url.url)}")
            print(f"{Util.error('Extracted value (for moedaDestino) is..')}: {Util.info(valid_extract_url.get_param_value('moedaDestino'))} --> from {Util.warning(valid_extract_url.url)}")
            print(f"{Util.error('Extracted value (for quantidade) is....')}: {Util.info(valid_extract_url.get_param_value('quantidade'))} --> from {Util.warning(valid_extract_url.url)}")
            print("........................")
        except ValueError as e:
            # breakpoint()
            print(f"{url_test=} {e=}")
            print("........................")

    print("****************************************************************************")
    print(f"Stats: {total_correct} corrects; {len(urls_test) - total_correct}: incorrect")
    print("****************************************************************************")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format=Util.LOG_FORMAT_SIMPLE)
    print("****************************")
    print("|| Extractor URL project! ||")
    print("****************************\n")

    # test_cep()
    # test_simple_class_extractor_url()
    # print("+++++++++++++++++++++++++++++++++++++++++++\n")

    # valids = [
    #     "bytebank.com/cambio",
    #     "bytebank.com.br/cambio",
    #     "www.bytebank.com/cambio",
    #     "www.bytebank.com.br/cambio",
    #     "http://www.bytebank.com/cambio",
    #     "http://www.bytebank.com.br/cambio",
    #     "https://www.bytebank.com/cambio",
    #     "https://www.bytebank.com.br/cambio"
    # ]
    # test_url(valids)
    #
    # invalids = [
    #     "https: // bytebank / cambio",
    #     "https: // bytebank.naoexiste / cambio",
    #     "ht: // bytebank.naoexiste / cambio"
    # ]
    # test_url(invalids)
    #
    # print("------------------\n")
    # url_full_ok = "https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"
    # url_full_nok = "//bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"
    # extractor_url_full_ok = ExtractorUrl(url=url_full_ok)
    # repetead_extractor_url_full_ok = ExtractorUrl(url=url_full_ok)
    # # extractor_url_full_nok = ExtractorUrl(url=url_full_nok)
    # print(f"{len(url_full_ok)=} == {len(extractor_url_full_ok)=} ? {(len(valids[0]) == len(extractor_url_full_ok))}")
    # print(extractor_url_full_ok)
    # print(f"{extractor_url_full_ok == repetead_extractor_url_full_ok} --> "
    #       f"{id(extractor_url_full_ok)} {id(repetead_extractor_url_full_ok)} --> "
    #       f"{extractor_url_full_ok is repetead_extractor_url_full_ok}")
    #
    # print(f"test __equal__: {repetead_extractor_url_full_ok.__eq__(extractor_url_full_ok)}")
    # print("////////////////////////////////////////////////")
    # print(f'{0 == False}')
    # print(f'{1 == True}')
    # print(f'{bool("") == False}')
    # print(f'{None == False}')
    # print(f'{"" == False}')

    conversion_test = ExtractorUrl(url="https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real")
    print(f"conversion to real: {conversion_test.convert('real')}")
    print(f"conversion to dolar: {conversion_test.convert('dolar')}")

