print("Name :", "Madhesh Gupta ,", "Enrollment_No. :", "0863CS231095")

def create_csv(filename, total: int):

    with open(filename, 'w+') as f:

        f.write('Name, gender, department, salary \n')

        for data in range(total):

            n = input('enter name : ')
            g = input('gender m/f/o : ')
            dept = input('enter department : ')
            sal = float(input('enter salary : '))

            f.write(f'{n}, {g}, {dept}, {sal} \n')

    print('created data.....')
    print('--' * 20)


def read_csv(filename):

    with open(filename, 'r') as f:

        for text in f:
            print(text)

    print('--' * 20)


create_csv('learn.csv', 3)

read_csv('learn.csv')
