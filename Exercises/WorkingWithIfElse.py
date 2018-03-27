user = { 'admin': False, 'active': False, 'name': 'Travis'}

admin = user.get('admin')
active = user.get('active')
username = user.get('name')

if admin and active:
    print "Active - (ADMIN)" + username
elif admin:
    print "(ADMIN)" + username
elif active:
    print "Active - " + username
else:
    print username
