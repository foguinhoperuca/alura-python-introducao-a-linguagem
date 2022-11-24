from collections import defaultdict, Counter
from operator import attrgetter
from decimal import Decimal
import list_ops
import py_collection_part_2
from py_collection_part_2 import Account
from tuples_examples import CheckingAccount, SavingAccount, InvestmentAccount
import array as arr
import numpy as np
from another_bank import SalaryAccount, MultipleSalaries


def course_01():
    list_ops.first_class()
    print("/////////////////////////////////////////////////////")
    print("")

    list_ops.second_class()
    print("/////////////////////////////////////////////////////")
    print("")

    list_ops.third_class()
    print("/////////////////////////////////////////////////////")
    print("")

    list_ops.until_class_04()
    print("/////////////////////////////////////////////////////")
    print("")

    list_ops.until_class_06()
    print("/////////////////////////////////////////////////////")
    print("")

    list_ops.final_class_course_01()
    print("/////////////////////////////////////////////////////")
    print("")


def course_02():
    py_collection_part_2.class_01()
    print("**************************************************************")
    print("")
    py_collection_part_2.class_02()
    print("**************************************************************")
    print("")
    py_collection_part_2.class_03_1()
    print("**************************************************************")
    print("")
    py_collection_part_2.class_03_2()
    print("**************************************************************")
    print("")
    py_collection_part_2.class_04_1()
    print("**************************************************************")
    print("")
    py_collection_part_2.class_04_2()
    print("**************************************************************")
    print("")
    pydoc_list_pop = """
    Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)    
    """
    pydoc_list_queues = """
    It is also possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”); however, lists are not efficient for this purpose. While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).
    """
    py_collection_part_2.class_05(pydoc_list_pop)
    py_collection_part_2.class_05(pydoc_list_queues)


if __name__ == "__main__":
    print("")
    print("*******************************************")
    print("|| Python Collection 01: List and Tuples ||")
    print("*******************************************")
    print("")

    # course_01()
    # course_02()
    pydoc_list_pop = """
        Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)    
        """
    pydoc_list_queues = """
        It is also possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”); however, lists are not efficient for this purpose. While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).
        """
    py_collection_part_2.class_05(pydoc_list_pop)
    print("============================================")
    print("============================================")
    print("============================================")
    py_collection_part_2.class_05(pydoc_list_queues)


#     STOPPED AT 07:55 - convert list to dict


