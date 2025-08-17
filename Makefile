.PHONY: check-source

check-source:
	clear
	flake8 best_practices_pep8/main.py best_practices_pep8/queue.py best_practices_pep8/stats.py best_practices_pep8/util.py
	mypy best_practices_pep8/main.py best_practices_pep8/queue.py best_practices_pep8/stats.py best_practices_pep8/util.py

run-pep8: check-source
	clear
	python best_practices_pep8/main.py

run-test-tdd:
	@clear
	@date
	python3 -m pytest tests/tdd_com_python/bidder.py::TestBid::test_bidder_should_generate_valid_bids
	python3 -m unittest tests.tdd_com_python.domain.TestAuction.test_receive_bid_greater_than_last_one
	@date

run-test-tdd-all:
	@clear
	@date
	python3 -m unittest tests.tdd_com_python.domain
	python3 -m pytest tests/tdd_com_python/bidder.py
	@date
