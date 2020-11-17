def count_items_in_list(list_variable, quiet_or_loud):
    total_terms_to_search = 0
    if str(quiet_or_loud).lower() == 'quiet':
        for each_string in list_variable:
            total_terms_to_search += 1
        return total_terms_to_search
    elif str(quiet_or_loud).lower() == 'loud':
        for each_string in list_variable:
            total_terms_to_search += 1
            print(f'Number {total_terms_to_search}: {each_string}')
        return total_terms_to_search
    else:
        print("Quiet or loudly?")


def bash_command(input):
    _ = system(input)
