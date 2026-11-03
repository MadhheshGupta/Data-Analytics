print("Name :","Madhesh Gupta ,","Enrollment_No. :","0863CS231095")
def read_csv(filename):
    with open(filename,'r') as f:
        next(f)
        for line in f:
            yield line.strip().split(', ')
            #~! this is complete row data
def filter_data(data):
    for row in data:
        #~# avi  m  IT  28000
        n,g,dept,sal = row
        
        #~^ n = avi   g = m   dept = IT   sal = 28000
        if float(sal) > 28000:
            yield row

def update_data(data):
    for row in data:
        #~# avi  m  IT  28000
        n,g,dept,sal = row
        
        #~# these are unpacked, not in form of list or tuple
        #~# so you need to pack them again
        
        new_sal = float(sal) + float(sal) * 1.10
        yield [n, g, dept, new_sal]

def display(data):
    print('__' * 20)
    
    for row in data:
        print(row)

pipeline = display(filter_data(read_csv('learn.csv')))
d = display(read_csv('learn.csv'))
p2 = display(update_data(read_csv('learn.csv')))
