.PHONY: check-source

check-source:
	clear
	flake8 best_practices_pep8/main.py best_practices_pep8/queue.py best_practices_pep8/stats.py best_practices_pep8/util.py
	mypy best_practices_pep8/main.py best_practices_pep8/queue.py best_practices_pep8/stats.py best_practices_pep8/util.py

run-pep8: check-source
	clear
	python best_practices_pep8/main.py
