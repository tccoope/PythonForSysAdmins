users = [{ 'admin': True, 'active': True, 'name': 'Travis'},
{ 'admin': True, 'active': False, 'name': 'Pete'},
{ 'admin': False, 'active': True, 'name': 'Ben'},
{ 'admin': False, 'active': False, 'name': 'Evan'}]

line = 0

for user in users:
    line += 1
    if user['admin'] and user['active']:
        print "%i Active - (ADMIN)%s" % (line, user['name'])
    elif user['admin']:
        print "%i (ADMIN)%s" % (line, user['name'])
    elif user['active']:
        print "%i Active - %s" % (line, user['name'])
    else:
        print "%i %s" % (line, user['name'])
