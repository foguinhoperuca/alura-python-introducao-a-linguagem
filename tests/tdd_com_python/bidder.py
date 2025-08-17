import logging
import pytest

from tdd_com_python.domain import Auction, Bid, Bidder, WalletWithoutFundsException


class TestBidder:
    @pytest.fixture
    def oro_jackson(self) -> Auction:
        return Auction(description="Gol D. Roger's ship. The one to cross the end of Grand Line.")

    @pytest.fixture
    def luffy(self) -> Bidder:
        return Bidder(name='Luffy', wallet=19.99)

    def test_receive_bidder_cant_be_more_than_bidder_have_in_wallet(self, luffy: Bidder, oro_jackson: Auction) -> None:
        with pytest.raises(WalletWithoutFundsException):
            luffy.bid(auction=oro_jackson, value=1000000.00)

        bid: Bid = luffy.bid(auction=oro_jackson, value=1.99)
        assert bid.is_valid()


class TestBid:
    @pytest.fixture
    def nami(self) -> Bid:
        initial_wallet_nami: float = 7856.42
        return Bidder(name='Nami', wallet=initial_wallet_nami)

    def test_bidder_should_generate_valid_bids(self, nami) -> None:
        initial_wallet_nami: float = 7856.42

        invalid_bid: Bid = Bid(bidder=nami, value=10000.85, logging_level=logging.DEBUG)
        assert not invalid_bid.is_valid()

        valid_bid: Bid = Bid(bidder=nami, value=initial_wallet_nami, logging_level=logging.DEBUG)
        assert valid_bid.is_valid()

        also_valid_bid: Bid = Bid(bidder=nami, value=346.92, logging_level=logging.DEBUG)
        assert also_valid_bid.is_valid()
