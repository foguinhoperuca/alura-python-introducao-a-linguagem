from typing import Dict

from domain import Auction, Auctioneer, Bid, Bidder


monalisa: Auction = Auction("Selling Da Vinci's painting Monalisa")
joe: Bidder = Bidder('Joe Doe')
yuri: Bidder = Bidder('Yuri')

print(f"Today's {monalisa}")
print('Participants:')
print(f'- participant 01: {joe}')
print(f'- participant 02: {yuri}')
print('')

monalisa.receive_bid(Bid(joe, 17.23))
monalisa.receive_bid(Bid(yuri, 65.80))

print('')
print('--------------------------------------')
print('RESULT:>')
print('')

auctioneer: Auctioneer = Auctioneer()
result: Dict[str, Bid] = auctioneer.declare_winner(auction=monalisa)
print(f"highest..: {str(result['highest'])}")
print(f"lowest...: {str(result['lowest'])}")
print('--------------------------------------')
