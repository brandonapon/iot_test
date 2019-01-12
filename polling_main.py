from bird import bird_watch

b = bird_watch()
# b.update_login_info()
# print(b.email, b.guid)
b.login()
print(b.token)
