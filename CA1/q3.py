
'''3 input into list, list into dictionary, and count how many inputs'''


def is_valid (val):
    return val != ('done').lower()

#add values into the list
inp = ''
#create a variable which stores a list
values = []
#while entry is not equal to done function keeps looping
while is_valid (inp):
    inp = raw_input ('Enter a number or type done to exit the program:')
    if is_valid (inp):
            try:
                #input converted to float
                value = float(inp)
                if value <= 7 and value >= 1:
                #add values to the list as a float
                    values.append(float(inp))
                #if wrong input print message and don't add value into the lsit
                #input should be converted to float
                else:
                    #if value not between 1 and 7
                    print 'Bad input, pelase enter value between 1 and 7'
            except:
                print 'Bad Input, please input an int or type done to exit the program'
         
print values 


#assign name to value and count how many         
values_dic = {}
for value in values:
    if value == 1.0:
       values_dic['Very bad'] = values_dic.get('Very bad', 0) + 1
    elif value == 2.0:
        values_dic['Bad'] = values_dic.get('Bad', 0) + 1
    elif value == 3.0:
        values_dic['Midle'] = values_dic.get('Midle', 0) + 1
    elif value == 4.0:
        values_dic['Average'] = values_dic.get('Average', 0) + 1
    elif value == 5.0:
        values_dic['Not Bad'] = values_dic.get('Not Bad', 0) + 1
    elif value == 6.0:
        values_dic['Good'] = values_dic.get('Good', 0) + 1
    elif value == 7.0:
        values_dic['Very good'] = values_dic.get('Very good', 0) + 1

print values_dic


#sort from bigest to smallest
values = []
for k, v in values_dic.items():
    values.append((v, k))    
sorted_values = sorted(values, reverse = True)

for value in sorted_values:
      print value[1], ':', value[0]
#print sorted_values[0][1] , ': ', sorted_values[0][0]



'''grades to dictionary and aftrt to list'''

def is_valid(val):
    return val != ('done').lower()



students = ''
value = False
while is_valid(students) and not value:
    students = raw_input('Pelase enter for how many students you would like to record results:')
    try:
        students = int(students)
        #breaking a while loop
        value = True
    except:
        print 'Pelase enter numeric value'
        
        
result = '' 
results_list = []       
while students > 0 and is_valid(result):
    result = raw_input('Pelase enter result for each student: ')
    try:
        result = float(result)
        if result >= 0 and result <=100:
            results_list.append(result)
            students -= 1
        else:
            print 'Result must be between 0-100'
    except:
        print 'Pelase enter numeric value'
        
        
inp = ''
grades = {}
value = False
values = [] 
while is_valid(inp) and not value:
    inp = raw_input('Tyoe 1 to Display Number of Students per Grade\
                    \nType Done to Quit: ')
    if is_valid(inp):
        try:
            if inp == '1':
                for result in results_list:
                    if 70 <= result <= 100:
                        grades['A'] = grades.get('A',0) + 1
                    elif 60 <= result <= 69:
                        grades['B'] = grades.get('B',0) + 1
                    elif 50 <= result <= 59:
                        grades['C'] = grades.get('C',0) + 1
                    elif 40 <= result <= 49:
                        grades['D'] = grades.get('D',0) + 1
                    elif 0 <= result <= 39:
                        grades['E'] = grades.get('E',0) + 1    
                for k, v in grades.items():
                    values.append((k, v))
                for value in values:
                    print value[0], ':', value[1] 
                #print grades
                #value = True
            else:
                print '\nWrong input, pelase perss 1 to display number of students\
                \nor type "Done" to exit'
        except:
            print 'Bad input'
    else: 
        print 'Thank you for using my program!'
