from enum import auto, StrEnum
import logging
import sys
from typing import Dict, List

from termcolor import colored    # type: ignore

sys.path.append('.')
from util import Util           # noqa: E402


class WalletWithoutFundsException(Exception):
    pass


class Bidder:
    """Will participate in auction. Made bids.
    Vulgo: licitante/interessados (pt-br).
    """
    def __init__(self, name: str, wallet: float = 0.00) -> None:
        self.__name: str = name
        self.__wallet: float = wallet
        self.__participations: Dict[Auction, float] = dict()

    @property
    def name(self) -> str:
        return self.__name

    @property
    def wallet(self) -> float:
        return self.__wallet

    @wallet.setter
    def wallet(self, vl: float) -> None:
        self.__wallet = vl

    @property
    def participations(self) -> float:
        return self.__participations

    def __str__(self) -> str:
        name_formatted: str = f'{self.__name:<10}'
        return f'Bidder identification is {colored(name_formatted, "yellow")}'

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, another) -> bool:
        return self.__name == another.name

    def bid(self, auction: 'Auction', value: float) -> 'Bid':
        bid: Bid = Bid(bidder=self, value=value)
        if not bid.is_valid():
            error_msg: str = f'This bidder: {str(self)} could not do a valid bid with value: ${value} :: wallet: {self.__wallet}'
            raise WalletWithoutFundsException(error_msg)

        self.__participations[auction] = value

        return bid


class Bid:
    def __init__(self, bidder: Bidder, value: float, logging_level=logging.INFO) -> None:
        self.__bidder: Bidder = bidder
        self.__value: float = value
        logging.basicConfig(level=logging_level, format=Util.LOG_FORMAT_FULL)  # alternative: LOG_FORMAT_DEBUG

    @property
    def bidder(self) -> Bidder:
        return self.__bidder

    @property
    def value(self) -> float:
        return self.__value

    def __str__(self) -> str:
        return f'{str(self.__bidder)} with value: {colored(f"${self.__value}", "red")}'

    def __repr__(self) -> str:
        return self.__str__()

    def is_valid(self) -> bool:
        is_valid: bool = True

        if self.__value > self.__bidder.wallet:
            is_valid = False

        logging.debug(f'****************************** {self.__value=} :: {self.__bidder.wallet=} :: {is_valid=}')

        return is_valid


class Auction:
    class AuctionType(StrEnum):
        LOWER = auto()
        HIGHEST = auto()

    def __init__(self, description: str, minimum_bid: float = 0.01, auction_type: AuctionType = AuctionType.HIGHEST, logging_level=logging.INFO) -> None:
        self._description: str = description
        self._minimum_bid: float = minimum_bid
        self._auction_type: Auction.AuctionType = auction_type
        self.__bids: List[Bid] = []
        logging.basicConfig(level=logging_level, format=Util.LOG_FORMAT_FULL)  # alternative: LOG_FORMAT_DEBUG

    @property
    def description(self) -> str:
        return self._description

    @property
    def minimum_bid(self) -> float:
        return self._minimum_bid

    @property
    def auction_type(self) -> AuctionType:
        return self._auction_type

    @property
    def bids(self) -> List[Bid]:
        return self.__bids[:]

    def __str__(self) -> str:
        return f'[{colored(self._auction_type.upper(), "white")}] Auction: {colored(self._description, "cyan")}'

    def __repr__(self) -> str:
        return self.__str__()

    def receive_bid(self, bid: Bid) -> None:
        """ Rules to a valid bid:
        0. A bid should be greather than 0;
        1. Minimum (lowest) acceptance value;
        2. The same bidder can't bid twice in a row;
        3. The bid must be greather than the last one;
        """
        logging.debug(f'Received bid -> {bid}')

        if bid.value <= 0:
            logging.error(f'Invalid bid value: {bid.value} -> it should be positve greater than zero.')
            return None

        if bid.value < self._minimum_bid:
            logging.error(f'Invalid bid: {bid.value} -> it should be a grather than the minimum bid: ${self._minimum_bid} !!')
            return None

        if len(self.__bids) > 0 and bid.bidder == self.__bids[-1].bidder:
            logging.error(f'Invalid bid: {bid.bidder} (last bidder: {self.__bids[-1].bidder})-> it should be a different bidder from the last one!!')
            return None

        if len(self.__bids) > 0 and bid.value <= self.__bids[-1].value:
            error_msg: str = f'Invalid bid: {bid.value} (last value: {self.__bids[-1].value})-> it should be a grather than last one value!!'
            logging.error(error_msg)
            raise ValueError(error_msg)

        self.__bids.append(bid)

    # TODO implement a strategy design pattern using: A - AuctioneerSimpleMinMax; B - AuctioneerMinMaxShouldRespectCeilFloor
    def sell(self) -> Bid:
        pass


class Auctioneer:
    """Responsible for define the best bid and declare the winner.
    Vulgo: Leiloeiro (pt-br)
    """
    def __init__(self, logging_level=logging.INFO) -> None:
        logging.basicConfig(level=logging_level, format=Util.LOG_FORMAT_FULL)  # alternative: LOG_FORMAT_DEBUG

    def declare_winner(self, auction: Auction) -> Dict[str, Bid]:
        initial_bidder: Bidder = Bidder('Initial Bidder Default')
        lowest_bid: Bid = Bid(bidder=initial_bidder, value=sys.float_info.max)
        highest_bid: Bid = Bid(bidder=initial_bidder, value=sys.float_info.min)

        for bid in auction.bids:
            if bid.value > highest_bid.value:
                highest_bid = bid

            if bid.value < lowest_bid.value:
                lowest_bid = bid

        return {
            'highest': highest_bid,
            'lowest': lowest_bid
        }
