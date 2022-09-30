def even_number_of_evens(numbers):
    if isinstance(numbers, list):
        evens = sum([1 for n in numbers if n % 2 == 0])
        # refactoring 1
        # for n in numbers:
        #     if n % 2 == 0:
        #         evens += 1
        return True if evens and evens % 2 == 0 else False
        # refactoring 2
        # if evens:
        #     return evens % 2 == 0
        # else:
        #     return False
    else:
        raise TypeError("A list was not passed")
        

if __name__ == '__main__':
    print(even_number_of_evens([2, 1, 4]))