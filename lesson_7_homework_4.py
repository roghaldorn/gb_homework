import os

test_path = './'


def dir_stats(dir_path):
    """
    Calculate and sort size of files in
    :param dir_path: path to directory which need a sort, STR
    :return: dict with sorted sizes of files, DICTIONARY
    """
    os_dir_path, files_size_list = os.path.abspath(dir_path), []
    directory_dict = {
        100: 0,
        1000: 0,
        10000: 0,
        100000: 0,
        1000000: 0,
        10000000: 0,
        100000000: 0,
        1000000000: 0,
        10000000000: 0
    }
    for root, _, files in os.walk(dir_path):
        if len(files):
            for file in files:
                files_size_list.append(os.stat(os.path.join(root, file)).st_size)

    for items in files_size_list:
        for dict_sizes in directory_dict.keys():
            if dict_sizes == 100:
                if items <= 100:
                    directory_dict[dict_sizes] += 1
            else:
                if items < dict_sizes and items > int(str(dict_sizes)[:-1]):
                    directory_dict[dict_sizes] += 1

    return directory_dict


print(dir_stats(test_path))
