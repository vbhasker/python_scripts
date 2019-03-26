#!/usr/bin/env python3


users = [{'admin': True, 'active': False, 'name': 'Kevin'}, {'admin': True, 'active': True, 'name': 'Vinodh'},
         {'admin': False, 'active': False, 'name': 'Bob'}]

for user in users:
    if user['active']:
        print('ACTIVE -', end=' ')
    if user['admin']:
        print('(ADMIN)', end=' ')

    print(user['name'])
