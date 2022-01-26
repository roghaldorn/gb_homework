if __name__ == '__main__':
    print('Lesson 6\nHomework 1\nBalyasnikov Maksim')

from requests import get
import json

# errors = getattr(__builtins__,'FileExistsError', IOError)#


response, spam_dict, spam_dict_2 = get(
    'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'), {}, {}
with open('data_1_response.dat', 'w+', encoding='utf-8') as f1:
    with open('data_2_result.dat', 'w+', encoding='utf-8') as f2:
        with open('data_3_spam.json', 'w+', encoding='utf-8') as f3:
            for chunk in response.content.decode(encoding=response.encoding).split('\n'):
                f1.write(f'{chunk}\n')
            f1.seek(0)
            for count, rows in enumerate(f1):
                adr_list = []
                adr_list.append(ip := rows[0:rows.find(" ")])  # ip
                adr_list.append(rows[rows.find('"') + 1:rows.find('"') + 4])  # request type
                adr_list.append(rows[rows.find('prod'):rows.find('HT') - 1])  # product type
                if ip in spam_dict:
                    spam_dict[ip] += 1
                else:
                    spam_dict[ip] = 1
                f2.write(str(f'{tuple(adr_list)}\n'))
            for key, value in spam_dict.items():
                spam_dict_2[value] = key

            print(
                f'Наибольшее количество запросов ({max(spam_dict.values())}) с ip {spam_dict_2[max(spam_dict.values())]}'
            )

            json.dump(spam_dict, f3, indent=4)
