x = [ [5,2,3], [15,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Bryant', 'James', 'Curry'],
    'soccer' : ['Andres', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 30} ]
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for i in range (0,len(some_list)):
        print((some_list[i]))

iterateDictionary(students)

def iterateDictionary2(key_name, some_list):
    for i in range (0, len(some_list)):
        print (some_list[i][key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    print (len(some_dict['locations']), "Locations")
    for i in range (0, len(some_dict['locations'])):
        print (some_dict['locations'][i])
    print ("")
    print (len(some_dict['instructors']), "Instructors")
    for i in range (0, len(some_dict['instructors'])):
        print (some_dict['instructors'][i])

printInfo(dojo)

