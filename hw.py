__author__ = 'will'


# database = [
#     ['wilzhang', '1111'],
#     ['ziyzhang', '1111'],
#     ['ziyue', '111111']
# ]
#
# id = input('Enter your name : ')
# Pass1 = input ('Enter your pass: ')
#
# if [id, Pass1] in database:
#     print('valid')
# else:
#     print('not valid')
#



# words = input('Please enter a string: ')
# # if words(n)
#
# print(words.count('a'))
#
# print(['to','be','or','not','to','be'].count('to'))
#
# words = input('Please enter a string: ')
# long=len(words)
# new=[None]*len(words)
# for n in range (0,long):
#     new[n] = words[long-n-1]
# print(''.join(new))


# words = input('Please enter a string: ')
#
# print(''.join(words))


#hello this is a change test

# update test

#this is another test

people = {
    'Alice': {
        'phone': '2341',
        'addr': 'Foo drive 23'
    },
    'Beth': {
        'phone': '9102',
        'addr': 'Bar street 42'
    },
    'Cecil': {
        'phone': '3158',
        'addr': 'Baz avenue 90'
    }
}

labels = {
    'phone': 'phone number',
    'addr': 'address'
}

name = input('name: ')
request = input("Phone number (p) or address (a)? ")
if request == 'p':
    key = 'phone'
if request == 'a':
    key = 'addr'

if name in people: print("%s's %s is %s." % (name, labels[key], people[name][key]))