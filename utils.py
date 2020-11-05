
def get_integer_in_range(min_bound,max_bound,prompt_string=None):
    n_int = 0
    while(n_int < min_bound or n_int > max_bound):
        n = input(prompt_string)
        try:
            n_int = int(n)
        except ValueError:
            print("Not an integer, enter an integer...")
    return n_int

def choose_string_in_list(str_list):
    typed_str = []
    flag = True
    print(str_list)
    while(flag):
        typed_str = input("Type exactly one of the proposed elements:\n")
        if(str_list.count(typed_str) == 1):
            flag = False
    return typed_str