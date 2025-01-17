import  json

def get_stored_username():
    """获取存储的用户名"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """输入用户名"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """问候用户，指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, "+username+'!')
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + '!')

greet_user()