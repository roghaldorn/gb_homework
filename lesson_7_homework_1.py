import os

test_ls = ['my_project', 'settings', 'mainapp', 'adminapp', 'authapp',
           'C:/Users/balasick/PycharmProjects/files']


def start_project(*args):
    """
    Creating a project directory with names in
    :param args: list with names of directory, LIST
    :return: string with status, STR
    """
    try:
        dir_names = args[0]
        names_dict = {
            'main_dir': dir_names[0],
            'dir_0': dir_names[1],
            'dir_1': dir_names[2],
            'dir_2': dir_names[3],
            'dir_3': dir_names[4],
            'root_path': './' if len(dir_names) == 5 else dir_names[5]
        }
    except (NameError, IndexError):
        return None
    else:
        project_path = os.path.abspath(os.path.join(names_dict['root_path'], names_dict['main_dir']))
        if os.path.exists(project_path):
            return 'Проект с таким именем уже существует'
        else:
            os.mkdir(project_path)
            for index, dirs in enumerate(names_dict):
                if index > 0 and index < 5:
                    os.makedirs(os.path.join(project_path, names_dict[dirs]))
                    return 'Done'


print(start_project(test_ls))
