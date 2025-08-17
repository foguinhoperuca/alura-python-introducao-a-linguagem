from typing import Dict, List
from unittest import TestCase

from tdd_com_python.domain import Auction, Auctioneer, Bid, Bidder


class TestAuctioneer(TestCase):
    def setUp(self) -> None:
        self.bidders: List[Bidder] = [
            Bidder('Loki'),
            Bidder('Peter'),
            Bidder('Tux'),
            Bidder('Luigi')
        ]
        self.auctioneer: Auctioneer = Auctioneer()

    def test_declare_winner_when_descending_bids(self) -> None:
        brazil_1970: Auction = Auction("[AUTO TEST] Selling rare t-shirt from Brazil's 1970.")
        brazil_1970.receive_bid(Bid(self.bidders[0], 596.66))
        with self.assertRaises(ValueError):
            brazil_1970.receive_bid(Bid(self.bidders[1], 147.84))

        result_1970: Dict[str, Bid] = self.auctioneer.declare_winner(auction=brazil_1970)
        self.assertEqual(596.66, result_1970['highest'].value)
        self.assertEqual(596.66, result_1970['lowest'].value)

    def test_declare_winner_when_ascending_bids(self) -> None:
        brazil_1994: Auction = Auction("[AUTO TEST] Selling rare t-shirt from Brazil's 1994.")
        brazil_1994.receive_bid(Bid(self.bidders[0], 99.27))
        brazil_1994.receive_bid(Bid(self.bidders[1], 130.89))
        result_1994: Dict[str, Bid] = self.auctioneer.declare_winner(auction=brazil_1994)
        self.assertEqual(130.89, result_1994['highest'].value)
        self.assertEqual(99.27, result_1994['lowest'].value)

    def test_declare_winner_when_multiple_bids(self) -> None:
        brazil_2002: Auction = Auction("[AUTO TEST] Selling rare t-shirt from Brazil's 2002.")
        brazil_2002.receive_bid(Bid(self.bidders[0], 26.74))
        brazil_2002.receive_bid(Bid(self.bidders[1], 987.50))
        with self.assertRaises(ValueError):
            brazil_2002.receive_bid(Bid(self.bidders[2], 257.66))

        with self.assertRaises(ValueError):
            brazil_2002.receive_bid(Bid(self.bidders[3], 18.19))

        result_2002: Dict[str, Bid] = self.auctioneer.declare_winner(auction=brazil_2002)
        self.assertEqual(987.50, result_2002['highest'].value)
        self.assertEqual(26.74, result_2002['lowest'].value)

        brazil_2006: Auction = Auction("[AUTO TEST] Selling rare t-shirt from Brazil's 2006.")
        brazil_2006.receive_bid(Bid(self.bidders[2], 1.99))
        brazil_2006.receive_bid(Bid(self.bidders[3], 9.99))
        brazil_2006.receive_bid(Bid(self.bidders[1], 25.41))
        result_2006: Dict[str, Bid] = self.auctioneer.declare_winner(auction=brazil_2006)
        self.assertEqual(25.41, result_2006['highest'].value)
        self.assertEqual(1.99, result_2006['lowest'].value)

    def test_declare_winner_when_one_bids(self) -> None:
        brazil_1998: Auction = Auction("[AUTO TEST] Selling rare t-shirt from Brazil's 1998.")
        brazil_1998.receive_bid(Bid(self.bidders[0], 782.48))
        result_1998: Dict[str, Bid] = self.auctioneer.declare_winner(auction=brazil_1998)
        self.assertEqual(782.48, result_1998['highest'].value)
        self.assertEqual(782.48, result_1998['lowest'].value)


class TestAuction(TestCase):
    def setUp(self) -> None:
        self.minimum_bid: float = 0.99
        self.action_figure: Auction = Auction('Selling an rare action figure', minimum_bid=self.minimum_bid)
        self.mario: Bidder = Bidder('Mario')
        self.wario: Bidder = Bidder('Wario')
        self.valid_value: float = 4563.74
        self.valid_bid: Bid = Bid(self.mario, self.valid_value)
        self.invalid_bid_zero: Bid = Bid(self.wario, 0)
        self.invalid_negative_value: float = -754.84
        self.invalid_bid_negative: Bid = Bid(self.wario, self.invalid_negative_value)

    def test_receive_bid_when_valid(self) -> None:
        self.action_figure.receive_bid(bid=self.valid_bid)
        self.assertEqual(1, len(self.action_figure.bids))

    def test_receive_bid_when_invalid(self) -> None:
        self.action_figure.receive_bid(bid=self.invalid_bid_zero)
        self.assertEqual(0, len(self.action_figure.bids))

        self.action_figure.receive_bid(bid=self.invalid_bid_negative)
        self.assertEqual(0, len(self.action_figure.bids))

    def test_receive_bid_minimum_value(self) -> None:
        self.assertEqual(0, len(self.action_figure.bids))

        bid_less_minimum: Bid = Bid(bidder=self.mario, value=0.05)
        self.action_figure.receive_bid(bid=bid_less_minimum)
        self.assertEqual(0, len(self.action_figure.bids))

        bid_equal_minimum = Bid(bidder=self.mario, value=self.minimum_bid)
        self.action_figure.receive_bid(bid=bid_equal_minimum)
        self.assertEqual(1, len(self.action_figure.bids))

        bid_greather_minimum = Bid(bidder=self.wario, value=579.88)
        self.action_figure.receive_bid(bid=bid_greather_minimum)
        self.assertEqual(2, len(self.action_figure.bids))

    def test_receive_bid_not_same_bidder_in_a_row(self):
        self.assertEqual(0, len(self.action_figure.bids))
        self.action_figure.receive_bid(bid=self.valid_bid)
        self.assertEqual(1, len(self.action_figure.bids))
        another_attemp_mario: Bid = Bid(bidder=self.mario, value=6984.88)
        self.action_figure.receive_bid(bid=another_attemp_mario)
        self.assertEqual(1, len(self.action_figure.bids))

    def test_receive_bid_greater_than_last_one(self):
        self.assertEqual(0, len(self.action_figure.bids))
        self.action_figure.receive_bid(bid=self.valid_bid)
        self.assertEqual(1, len(self.action_figure.bids))

        with self.assertRaises(ValueError):
            another_attemp_wario_less: Bid = Bid(bidder=self.wario, value=11.22)
            self.action_figure.receive_bid(bid=another_attemp_wario_less)
        self.assertEqual(1, len(self.action_figure.bids))

        with self.assertRaises(ValueError):
            another_attemp_wario_equal: Bid = Bid(bidder=self.wario, value=self.valid_value)
            self.action_figure.receive_bid(bid=another_attemp_wario_equal)
        self.assertEqual(1, len(self.action_figure.bids))

        another_attemp_wario_greather: Bid = Bid(bidder=self.wario, value=10857.93)
        self.action_figure.receive_bid(bid=another_attemp_wario_greather)
        self.assertEqual(2, len(self.action_figure.bids))
