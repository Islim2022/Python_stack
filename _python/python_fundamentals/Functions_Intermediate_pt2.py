# 1.1 Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x = [ [5,2,3], [10,8,9] ] 
for i in x:
    for v in range(len(i)):
        if i[v] == 10:
            i[v] = 15           
print(x)

# 1.2 Change the last_name of the first student from 'Jordan' to 'Bryant'
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

students[0]['last_name'] = 'Bryant'
print(students) 

# 1.3 In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']}
sports_directory['soccer'][0]= 'Andres'
print(sports_directory)

# 1.4 Change the value 20 in z to 30
z = [ {'x': 10, 'y': 20} ]
# for i in z:
#     if ['y'] == 20:
#         ['y'] = 30
z[0]['y']= 30
print(z)

# 2. Iterate Through a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    string = ''
    for i in students:
        string += f"first_name - {i['first_name']}, last_name - {i['last_name']}\n"
    return string
print(iterateDictionary(students))
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# 3. Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    string = ''
    for i in some_list:
        string += f"{i[key_name]}\n"
    return string
print(iterateDictionary2('first_name', students))
# Michael
# John
# Mark
# KB
print(iterateDictionary2('last_name', students))
# Jordan
# Rosales
# Guillen
# Tonel


# # 4. NEED TO REDO THIS ONE. 
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printDictonaryInfo(my_dictonary):
    for key in my_dictonary:
        print(f"{len(my_dictonary[key])} {key.upper()}")
        for val in my_dictonary[key]:
            print(val)
        print("")
printDictonaryInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank


# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon