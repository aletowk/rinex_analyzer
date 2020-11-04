
def get_integer_in_range(min_bound,max_bound,prompt_string=None):
    n_int = 0
    while(n_int < min_bound or n_int > max_bound):
        n = input(prompt_string)
        try:
            n_int = int(n)
        except ValueError:
            print("Not an integer, enter an integer...")
    return n_int