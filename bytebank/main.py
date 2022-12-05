from bytebank.model import Employee


if __name__ == "__main__":
    print("***********************************")
    print("|| Python Unit Tests - Byte Bank ||")
    print("***********************************")

    lucas = Employee('Lucas Carvalho', '2000-04-01', 1000.00)
    print(lucas)
    print(lucas.birthday)

    carlos = Employee('Ana', '12/03/1997', 100000000)
    print(carlos)
    print(f"{carlos.name}'s bonus is: ${carlos.bonus()}")

    carlos = Employee('Carlos', '12/03/1997', 987.55)
    print(carlos)
    print(f"{carlos.name}'s bonus is: ${carlos.bonus()}")