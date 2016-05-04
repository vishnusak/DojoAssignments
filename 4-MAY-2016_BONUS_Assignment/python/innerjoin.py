# Write a function  innerJoin  that uses the three provided arrays to return a new array, where each element is also an array containing three objects, one each pulled from  users ,  books  and  usersHaveBooks . Here's the catch: The user object's  id  property must match the  user_id  property of the  usersHaveBooks  object, and the book object's  id  property must match the  book_id  property of the  usersHaveBooks  object.

# steps:
# 1. traverse thru the user array
# 2. for every user-id, find the entry in usersHaveBooks. This will give us a pair (user1, userhavebook1), (user1, userhavebook2), (user2, userhavebook1) etc
# 3. for each of these pairs, match book-id in userhavebook with the book id in books array. This will give us the required triplet
def inner_join(arr_u, arr_b, arr_ub):
    result = []
    cell = []

    for user in (arr_u):
        for userbook in (arr_ub):
            if (user['id'] == userbook['user_id']):
                cell.append(user)
                cell.append(userbook)
                for book in (arr_b):
                    if (userbook['book_id'] == book['id']):
                        cell.append(book)
                        result.append(cell)
                        cell = []

    return result

users = [
  {
  'id': 1,
  'first_name': 'Johnny',
  'last_name': 'Rotten',
  'created_at':'2012-12-31 23:59:59',
  'updated_at':'2012-12-31 23:59:59'
  },
  {
  'id': 2,
  'first_name': 'Amy',
  'last_name': 'Brown',
  'created_at':'2012-12-31 23:59:59',
  'updated_at':'2012-12-31 23:59:59'
  },
  {
  'id': 3,
  'first_name': 'Alice',
  'last_name': 'Roh',
  'created_at':'2012-12-31 23:59:59',
  'updated_at':'2012-12-31 23:59:59'
  },

]

usersHaveBooks = [
  {
    'id':1,
    'user_id':1,
    'book_id':1,
    'created_at':'2012-12-31 23:59:59',
    'updated_at':'2012-12-31 23:59:59'
  },
  {
    'id':1,
    'user_id':1,
    'book_id':2,
    'created_at':'2012-12-31 23:59:59',
    'updated_at':'2012-12-31 23:59:59'
  },
  {
    'id':1,
    'user_id':1,
    'book_id':3,
    'created_at':'2012-12-31 23:59:59',
    'updated_at':'2012-12-31 23:59:59'
  },
  {
    'id':1,
    'user_id':2,
    'book_id':2,
    'created_at':'2012-12-31 23:59:59',
    'updated_at':'2012-12-31 23:59:59'
  },

]

books = [
  {
  'id': 1,
  'book_title': 'Grapes of Wrath',
  'book_subject': 'The hard life during the depression',
  'created_at':'2012-12-31 23:59:59',
  'updated_at':'2012-12-31 23:59:59'
  },
  {
  'id': 2,
  'book_title': 'Metamorphosis',
  'book_subject': 'The degradation of humanity, reflected in a single man',
  'created_at':'2015-01-12 23:59:59',
  'updated_at':'2015-01-12 23:59:59'
  },
  {
  'id': 3,
  'book_title': 'The Coming Plague',
  'book_subject': 'Infectious diseases',
  'created_at':'2015-01-12 23:59:59',
  'updated_at':'2015-01-12 23:59:59'
  },
]

joined_arr = inner_join(users, books, usersHaveBooks)

print("\nThe joined array has the following\n")
for details in joined_arr:
    print("{}").format(details[0])
    print("{}").format(details[1])
    print("{}\n\n").format(details[2])
