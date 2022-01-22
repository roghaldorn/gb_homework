# yield
def odd_nums(max_numb):
    for num in range(1, max_numb):
        if num % 2:
            yield num


odd_to_15 = odd_nums(15)
print('With yield:', next(odd_to_15), next(odd_to_15), next(odd_to_15))

# there's no yield

odd_nums = lambda max_num: (numb for numb in range(1, max_num) if numb % 2)
odd_to_20 = odd_nums(20)

print('Without yield:', next(odd_to_20), next(odd_to_20), next(odd_to_20))
