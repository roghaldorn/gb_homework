# homework_1_1 - преобразование секунд к минутам/часам/дням
def homework_1_1(time_duration):
    sec_in_mins, sec_in_hours, sec_in_days = 60, 3600, 86400

    if (time_duration < sec_in_mins):  # seconds
        print('{seconds} сек'.format(seconds=time_duration))

    elif (time_duration < sec_in_hours):  # mins
        print('{minutes} мин {seconds} сек'.format(minutes=time_duration // sec_in_mins,
                                                   seconds=time_duration % sec_in_mins))

    elif (time_duration < sec_in_days):  # hours
        print('{hours} час {minutes} мин {seconds} сек'.format(hours=time_duration // sec_in_hours,
                                                               minutes=time_duration // sec_in_mins - time_duration // sec_in_hours * sec_in_mins,
                                                               seconds=time_duration % sec_in_mins))
    elif (time_duration >= sec_in_days):  # days
        print('{days} дн {hours} час {minutes} мин {seconds} сек'.format(days=time_duration // sec_in_days,
                                                                         hours=time_duration // sec_in_hours - time_duration // sec_in_days * 24,
                                                                         minutes=time_duration // sec_in_mins - time_duration // sec_in_hours * sec_in_mins,
                                                                         seconds=time_duration % sec_in_mins))  #


# homework_1_2 - кубический список(?)
def homework_1_2():
    main_sum_a, main_sum_b, cube_list = 0, 0, [cube ** 3 for cube in range(1, 1001)]
    for number in cube_list:
        number_sum_a, number_sum_b = 0, 0
        for digit in str(number):  # часть a
            number_sum_a += int(digit)
        for digit in str(number + 17):  # часть b
            number_sum_b += int(digit)

        if (number_sum_a % 7 == 0):
            main_sum_a += number_sum_a
        if (number_sum_b % 7 == 0):
            main_sum_b += number_sum_b

    print(
        'Сумма чисел, сумма которых делится нацело на 7: {sum_a}.\nСумма чисел после прибавления 17-ти к элементам списка: {sum_b}.'.format(
            sum_a=main_sum_a, sum_b=main_sum_b))


# homework_1_3 - проценты
def homework_1_3():
    for percent in range(1, 101):
        # print(percent)
        if (percent in range(11, 15) or (int(str(percent)[-1]) == 0) or (
                int(str(percent)[-1]) in range(5, 10))):  # +исключения
            print('{perc} процентов'.format(perc=percent))
        elif (int(str(percent)[-1]) in range(2, 5)):
            print('{perc} процента'.format(perc=percent))
        else:
            print('{perc} процент'.format(perc=percent))

## раскомментить для проверки:

## homework_1_1 output test
#for some_time in range(99999):
#    homework_1_1(some_time)

## homework_1_2 output test
# homework_1_2()

## homework_1_3 output test
# homework_1_3()
