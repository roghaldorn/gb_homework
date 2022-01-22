def gen_tuple(*args, cl=None, name=None, num=0):
    counter = len(args[1])
    if args[0]:
        name = args[0].pop()
    if args[1]:
        cl = args[1].pop()
    num+=1
    while num != counter:
        num+=1
        yield (name, cl)


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

print(gen_tuple(tutors, klasses).__next__())
print(gen_tuple(tutors, klasses).__next__())
print(gen_tuple(tutors, klasses).__next__())
print(gen_tuple(tutors, klasses).__next__())
print(gen_tuple(tutors, klasses).__next__())
print(gen_tuple(tutors, klasses).__next__())
print(gen_tuple(tutors, klasses).__next__())
print(gen_tuple(tutors, klasses).__next__())
