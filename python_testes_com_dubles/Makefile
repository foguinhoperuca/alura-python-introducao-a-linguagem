.PHONY: ptcd-test

ptcd-test-one-fn:
	@clear
	@date
	@echo "----->> ptcvd-test run pytest <<-----"
	python3 -m pytest tests/python_testes_com_dubles/test_books.py::test_consult_books_returns_format_string
	python3 -m pytest tests/python_testes_com_dubles/test_book_directory.py::test_write_file_register_error_on_create_file

ptcd-test-suite:
	@clear
	@date
	@echo "----->> ptcvd-test-suite run pytest <<-----"
	python3 -m pytest tests/python_testes_com_dubles/test_books.py::test_consult_books_returns_format_string
	python3 -m pytest tests/python_testes_com_dubles/test_books.py::test_consult_books_call_prepare_data_once_and_with_same_parameters
	python3 -m pytest tests/python_testes_com_dubles/test_books.py::test_consult_books_call_get_url_with_params_return_of_prepare_data
	python3 -m pytest tests/python_testes_com_dubles/test_books.py::test_consult_books_call_execute_requisition_with_get_url_returns

ptcd-test-directory:
	@clear
	@date
	@echo "----->> ptcvd-test-directory run pytest <<-----"
	# python3 -m pytest --no-cov tests/python_testes_com_dubles/test_book_directory.py
	# python3 -m pytest tests/python_testes_com_dubles/test_book_directory.py::test_write_file_register_error_on_create_file
	# python3 -m pytest tests/python_testes_com_dubles/test_book_directory.py::test_write_in_file_call_write_spy_fp
	python3 -m pytest tests/python_testes_com_dubles/test_book_directory.py::test_write_in_file_call_write

ptcd-test:
	@clear
	@date
	@echo "----->> ptcvd-test run pytest <<-----"
	python3 -m pytest --no-cov tests/python_testes_com_dubles/test_books.py
	@echo ""
	@echo "////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"
	@echo "////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"
	@echo ""
	python3 -m pytest --no-cov tests/python_testes_com_dubles/test_books_stub.py
	@echo ""
	@echo "////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"
	@echo "////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"
	@echo ""
	python3 -m pytest --no-cov tests/python_testes_com_dubles/test_book_directory.py

ptcd-test-email:
	@clear
	@date
	@echo "----->> ptcvd-test-email run pytest <<-----"
	python3 -m pytest --no-cov tests/python_testes_com_dubles/test_send_email.py


ptcd-class04:
	@clear
	@date
	@echo "----->> ptcvd-class04 run pytest <<-----"
	python3 -m pytest --no-cov tests/python_testes_com_dubles/test_class04.py
