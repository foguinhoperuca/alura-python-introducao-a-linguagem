from document import add_attendants, reset_attendants, update_attendants, get_attendants


def test_add_attendant():
    reset_attendants()
    assert add_attendants("Jonh") == "OK"
    assert add_attendants('') != "OK"
    assert add_attendants('Jonh') != "OK"


def test_update():
    reset_attendants()
    add_attendants("Jonh")
    assert get_attendants()[0]['sales'] == 0
    update_attendants(index=0)
    assert get_attendants()[0]['sales'] == 1


if __name__ == "__main__":
    test_add_attendant()
    test_update()

    print('Test was sucessfully!!!')
