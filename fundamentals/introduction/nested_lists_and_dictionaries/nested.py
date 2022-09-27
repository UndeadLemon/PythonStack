x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
students[0]["first_name"]="Bryant"
sports_directory["soccer"][0] = "Andres"
z[0]["y"] =30

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]






def iterateDictionary(diction):
    for each_key in diction:

        print( each_key["first_name"] + " - " + each_key["last_name"] )


iterateDictionary(students) 

def iterateDictionary2(list, key_name):
    for i in range(0, len(list)):
        print(list[i][key_name])

iterateDictionary2(students, "last_name")
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}



def printInfo(some_dict):
     
    for key in some_dict:
        length = len(some_dict[key])
        print(f"{length} {key}")
        for i in range(0,length):
            print(some_dict[key][i])
printInfo(dojo)
