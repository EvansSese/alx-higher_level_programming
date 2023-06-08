#!/usr/bin/python3
if __name__ == "__main__":
    import variable_load_5
    variable_list = dir(variable_load_5)
    for variable in variable_list:
        if variable == 'a':
            print(variable_load_5.a)
            break
