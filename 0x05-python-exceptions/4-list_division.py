#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    division = []
    darth_result = 0
    for j in range(0, list_length):
        try:
            darth_result = my_list_1[j] / my_list_2[j]
        except TypeError:
            darth_result = 0
            print("wrong type")
        except ZeroDivisionError:
            darth_result = 0
            print("division by 0")
        except IndexError:
            darth_result = 0
            print("out of range")
        finally:
            pass
        division.append(darth_result)
    return division
