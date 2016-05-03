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

# for category in users:
#     print category
#     i = 0
#     for vals in users[category]:
#         i += 1
#         print "{} - {} {} - {}".format(i, vals['first_name'], vals['last_name'], len(vals['first_name']) + len(vals['last_name']))

for category in users:
    print category
    for idx, vals in enumerate(users[category]):
        print "{} - {} {} - {}".format((idx + 1), vals['first_name'], vals['last_name'], len(vals['first_name']) + len(vals['last_name']))
