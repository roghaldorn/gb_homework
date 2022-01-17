def thesaurus_adv(*args, s_name_d={}, space=' '):
    """Sort strings by full name, takes an strings, output a sorted dictionary."""
    for full_name in args:
        s_name_b = full_name.index(space) + 1
        if full_name[s_name_b] in s_name_d:
            if full_name[0] in s_name_d[full_name[s_name_b]]:
                s_name_d[full_name[s_name_b]][full_name[0]] += [full_name]
            else:
                s_name_d[full_name[s_name_b]][full_name[0]] = [full_name]

        else:
            s_name_d[full_name[s_name_b]] = {full_name[0]: [full_name]}

    f_name_d = dict(sorted(s_name_d.items(), key=lambda x: x[0]))

    return f_name_d


# print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
# print(thesaurus_adv.__doc__)
