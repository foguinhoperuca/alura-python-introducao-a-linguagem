from collections import defaultdict, Counter


def class_01():
    users_ds = [15, 23, 43, 56]
    users_ml = [13, 23, 56, 42]

    watched_ext = []
    watched_ext.extend(users_ds)
    print(watched_ext)

    watched_cp = users_ds.copy()
    print(watched_cp)

    watched = users_ds.copy()
    watched.extend(users_ml)
    print(f"{watched = } {len(watched) = }")
    for user in watched:
        print(user)

    print("-------------------------------------------")

    # w = set(watched)
    # print(f"{w = } {len(w) = }")
    # st = {4, 8, 1, 0, 9, 6, 11, 13, 15, 11, 7, 8, 7, 9, 4, 3}
    # print(f"{st = } {len(st) = }")
    # print(f"{st = } {len(st) = }")
    # print(f"{st = } {len(st) = }")
    # print(f"{st = } {len(st) = }")
    # print(f"{st = } {len(st) = }")

    users_ds_set = {15, 23, 43, 56}
    users_ml_set = {13, 23, 56, 42}
    watched_set = users_ds_set.union(users_ml_set)
    for user in watched_set:
        print(user)

    print(type(watched_set))
    print("-------------------------------------------")

    another_set = users_ml_set | users_ds_set
    for user in another_set:
        print(user)

    print("-------------------------------------------")
    intersection_set = users_ml_set & users_ds_set
    print(users_ml_set)
    print(users_ds_set)
    for user in intersection_set:
        print(user)

    inter = users_ml_set.intersection(users_ds_set)
    for user in inter:
        print(user)

    print("-------------------------------------------")
    diff_set = users_ds_set - users_ml_set
    for user in diff_set:
        print(user)

    diff = users_ds_set.difference(users_ml_set)
    for user in diff:
        print(user)

    print(f"{(15 in diff_set) = }")
    print(f"{(23 in diff_set) = }")

    print("-------------------------------------------")
    print(users_ml_set)
    print(users_ds_set)
    exclusive_set = users_ds_set ^ users_ml_set
    for user in exclusive_set:
        print(user)

    print("-------------------------------------------")
    excl = users_ml_set.symmetric_difference(users_ds_set)
    print(f"{len(excl) = }")
    for user in excl:
        print(user)

def class_02():
    users = {1, 5, 76, 34, 52, 13, 17}
    print(f"{len(users) = } {users = }")

    users.add(13)
    print(f"{len(users) = } {users = }")

    users.add(765)
    print(f"{len(users) = } {users = }")

    u = frozenset(users)
    print(f"{len(u) = } {u = } {type(u) = }")

    my_text = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
    print(my_text)
    my_set = set(my_text.split())
    print(f"{my_set = } {type(my_set) = }")


def class_03_1():
    appearances = {
        "Guilherme": 1,
        "cachorro": 2,
        "nome": 2,
        "vindo": 1
    }
    print(f"{type(appearances) = } {appearances}")
    print(f"{appearances['Guilherme'] = } {appearances['cachorro'] = }")
    try:
        print(f"{appearances['xpto'] = }")
    except Exception as e:
        print(f"Error was: {e = }")

    print(f"{appearances.get('xpto', 0) = } {appearances}")
    print(f"{appearances.get('cachorro', 0) = } {appearances}")

    appea_dict = dict(Guilherme=2, cachorro=1)
    print(f"{appea_dict = }")


def class_03_2():
    appearances = {
        "Guilherme": 1,
        "cachorro": 2,
        "nome": 2,
        "vindo": 1
    }

    appearances["Carlos"] = 66
    print(f"{appearances = }")

    appearances["Carlos"] = 33
    print(f"{appearances = }")

    del appearances["Carlos"]
    print(f"{appearances = }")

    print(f"{('cachorro' in appearances) = } {('Carlos' in appearances) = }")

    for el in appearances:
        print(el)

    try:
        for el in appearances.iterkeys():
            print(el)
    except Exception as e:
        print(f"dict.iterkeys do not exist anymore in python 3 see"
              f" [PEP 469 - Migration of dict iteration code to Python 3](https://peps.python.org/pep-0469/): {e = }")

    print("----------------------------------------")
    for el in appearances.keys():
        print(el)

    for el in appearances.values():
        print(el)

    print("----------------------------------------")
    print(f"{1 in appearances.values() = }")

    for el in appearances.keys():
        print(el, appearances[el])

    for el in appearances.items():
        print(f"{type(el) = } {el}")

    for key, value in appearances.items():
        print(f"{key = } {value = }")


def class_04_1():
    my_t3xt = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito muito de cachorro"
    print(my_t3xt)
    my_t3xt = my_t3xt.lower()
    print(my_t3xt)

    appearances = {}
    print(f"{type(appearances) = }")
    for txt in my_t3xt.split():
        appearances[txt] = appearances.get(txt, 0) + 1

    print(appearances)

    print("----------------------------------------------------------")

    appearances_default = defaultdict(int)
    print(f"{type(appearances_default) = }")
    for txt in my_t3xt.split():
        appearances_default[txt] = appearances_default[txt] + 1

    print(appearances_default)

    print("----------------------------------------------------------")
    print(appearances_default['bozo'])
    print(appearances_default['mafalda'])
    appearances_default['bozo'] = 15
    print(appearances_default['bozo'])

def class_04_02():
    my_t3xt = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito muito de cachorro"
    appearances = defaultdict(int)
    print(f"{type(appearances) = }")
    for txt in my_t3xt.split():
        appearances[txt] += 1

    print(appearances)
    print("***************************************************************************")
    accounts = defaultdict(Account)
    accounts[15]

    print("++++++++++++")
    print(accounts[17])
    print("++++++++++++")

    print("***************************************************************************")
    appea = Counter(my_t3xt.split())
    print(appea)


def class_05(txt_analysis):
    ct = Counter(txt_analysis.lower())
    total = sum(ct.values())
    print(ct)
    print(len(ct.values()))
    print(f"{ct.values() = } {total = }")

    for letter, freq in ct.items():
        # print(letter, freq)
        print(f"{letter = } {ct[letter] = :02} {total = } {((ct[letter] / total) * 100) = :019} %")

    print("+++++++++++++++++++++++++++++++++++++")
    proportions = [(letter, (freq / total) * 100) for letter, freq in ct.items()]
    print(len(proportions))
    print(proportions)
    print(dict(proportions))
    proportions = Counter(dict(proportions))
    m_com = proportions.most_common(10)
    print("************************")
    for ch, prop in m_com:
        # print((ch, prop))
        print("{} => {:.2f} %".format(ch, prop))

class Account:
    def __init__(self):
        print("Creating a new account...")
