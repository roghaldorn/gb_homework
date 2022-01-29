# насколько я понял суть задачи в корне проекта взять все файлы/директории и закинуть их в папку templates
import os
import shutil

test_dir = './lesson_7/my_project/'


def templates(pr_dir, new=False):
    """
    Function copy all dirs/files into 'templates' folder.
    :param pr_dir: path to your project, STR
    :param new: if True - if dir is already exist, func will del and re-create folder 'templates', BOOL
    :return: STR
    """
    project_dir = os.path.abspath(pr_dir)
    target_dir = os.path.abspath(os.path.join(project_dir, 'templates'))
    try:
        os.mkdir(target_dir)
    except FileExistsError:
        if not new:
            return 'Папка "templates" уже существует в корне проекта.'
        else:
            shutil.rmtree(os.path.join(project_dir, 'templates'))
            os.mkdir(target_dir)
    for dirs in os.listdir(project_dir):
        base_path = os.path.join(project_dir, dirs)
        target_path = os.path.join(target_dir, dirs)
        if dirs != 'templates':
            base_path = os.path.join(project_dir, dirs)
            target_path = os.path.join(target_dir, dirs)
            shutil.copytree(base_path, target_path)
    return 'Done'


print(templates(test_dir, new=True))
