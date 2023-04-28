class ByteBankReader:
    def __init__(self, file_reader):
        self._file_reader = file_reader

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        print("Closing file in dunder method __exit__")

    def read_next_line(self):
        print('Reading the next line...')
        raise IOError()

        return 'NEXT LINE AS IS'

    def close(self):
        print("Closing file")
