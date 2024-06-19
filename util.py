import geopandas as gpd
import matplotlib.pyplot as plt  # type: ignore
from termcolor import colored


def account_factory(number, owner, balance, limit):
    return {
        "number": number,
        "owner": owner,
        "balance": balance,
        "limit": limit
    }


def deposit(account, value):
    orig_balance = account['balance']
    account["balance"] += value
    print(f"You original balance is ${orig_balance}. You will deposit ${value}. The final balance is ${account['balance']}")


def withdraw(account, value):
    orig_balance = account['balance']
    account["balance"] -= value
    print(f"You original balance is ${orig_balance}. You will withdrawn ${value}. The final balance is ${account['balance']}")


def balance(account):
    print(f"The account's balance is ${account['balance']}")


# generate_figure_from_shape(in_file='geo/data/map_rj/33MUE250GC_SIR.shp', out='geo/data/output/rj_original', plot_original=True)  # noqa: E501
# generate_figure_from_shape(in_file='geo/data/map_rj/33MUE250GC_SIR.shp', out='geo/data/output/rj_black-white', plot_original=False)  # noqa: E501
def generate_figure_from_shape(in_file: str, out: str, plot_original: bool = True) -> None:
    shp: gpd.geodataframe.GeoDataFrame = gpd.read_file(in_file)  # type: ignore[attr-defined, name-defined]
    if plot_original:
        shp.plot()
    else:
        shp.plot(color='white', edgecolor='black', figsize=(15, 8))

    plt.savefig(out)
    print(f'Columns is: {shp.columns}')
    print(shp)
    # logging.debug(Util.warning(shp))


class Util:
    """Helper class used to provide configuration, defaults and so on."""
    LOG_FORMAT_FULL = colored('[%(asctime)s][%(process)d:%(processName)s]', 'green', attrs=['bold', 'dark']) + colored('[%(filename)s#%(funcName)s:%(lineno)d]', 'white', attrs=['bold', 'dark']) + colored('[%(levelname)s]', 'magenta', attrs=['bold', 'dark']) + ' %(message)s'
    LOG_FORMAT_DEBUG = colored('[%(filename)s#%(funcName)s:%(lineno)d]', 'white', attrs=['bold', 'dark']) + colored('[%(levelname)s]', 'magenta', attrs=['bold', 'dark']) + ' %(message)s'  # noqa: E501
    LOG_FORMAT_SIMPLE = colored('[%(levelname)s]', 'magenta', attrs=['bold', 'dark']) + ' %(message)s'  # noqa: E501
    GEO_02_NEW_OUTPUT: str = 'geo/data/geo02_new/output'
    GEO_02_NEW_INPUT: str = 'geo/data/geo02_new/input'
    GEO_02_NEW_DATA: str = 'alura_curso_geopandas_02/dados'

    # # FIXME Why I need instantiate Util class?!?! Make all methods statics wouldn't be enough?!?  # noqa: E501
    # def __init__(self):

    def info(msg):
        """This function standardize the message and simplified the use to standard output."""  # noqa: E501
        return colored(msg, 'cyan')

    def warning(msg):
        """This function standardize the message and simplified the use to standard output."""  # noqa: E501
        return colored(msg, 'yellow', attrs=['bold'])

    def error(msg):
        """This function standardize the message and simplified the use to standard output."""  # noqa: E501
        return colored(msg, 'red', attrs=['bold', 'underline'])

    def debug(msg):
        """This function standardize the message and simplified the use to standard output."""  # noqa: E501
        return colored(msg, 'green', attrs=['reverse', 'bold', 'underline'])

    def critical(msg):
        """This function standardize the message and simplified the use to standard output."""  # noqa: E501
        return colored(msg, 'red', attrs=['bold', 'underline', 'blink'])
