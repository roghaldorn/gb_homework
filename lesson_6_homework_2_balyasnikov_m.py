if __name__ == '__main__':
    print('Lesson 6\nHomework 2\nBalyasnikov Maksim')

import csv
with open('users.csv', 'r') as f_users:
    with open('hobby.csv', 'r') as f_hobby:
        users_row, hobby_row, user_ls, hobby_ls  = csv.reader(f_users), csv.reader(f_hobby), [], []
        for user in users_row:
            user_ls.append(' '.join(user))
        for hobby in hobby_row:
            hobby_ls.append(','.join(hobby))
        main_dict = dict(zip(user_ls, hobby_ls))


print(main_dict)