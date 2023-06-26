#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            item_1 = my_list_1[i]
            item_2 = my_list_2[i]
            try:
                div_result = item_1 / item_2
            except ZeroDivisionError:
                print("division by 0")
                div_result = 0
            except (TypeError, ValueError):
                print("wrong type")
                div_result = 0
            finally:
                result.append(div_result)
        except IndexError:
            print("out of range")
            result.append(0)
    return result
