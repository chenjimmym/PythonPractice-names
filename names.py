# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# for obj in students:
#     for name in obj.itervalues():
#         print name,                    #prints inline
#     print ''                           #to print a new line

#PART TWO
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

for pos, ob in users.iteritems():                   # ob is students and instructors
    print pos
    count = 1
    for data in ob:                                 # data is the dictionaries inside of ob
        print count, '-',
        nameCount = 0
        for names in data.itervalues():             # names is the values of the dictionaries (data)
            print names,
            nameCount = nameCount + len(names)
        print '-', nameCount,
        print ''
        count += 1