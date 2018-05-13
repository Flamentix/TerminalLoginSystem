import string

login_values = {
    'Flamentix' : 'someRandomValue',
    'exampleUser' : 'guest12345',
    'tempuser_12:16' : '_tempuser16:12'
}

login_values_m = dict((i.lower(), v) for i, v in login_values.items())
login_values_u = dict(zip(login_values_m.keys(), login_values.keys()))

def AppendLogin(username, password):
    for punctuation in string.punctuation:
        punctuation = str(punctuation)
        if (punctuation != '_' and punctuation != '.') and (punctuation in username):
            return 1
        if (punctuation == '}' and punctuation in password):
            return 2
        if username.lower() in login_values_m:
            return 3
        if len(username) > 12 or len(username) < 6:
            return 4
        if len(password) > 20 or len(password) < 8:
            return 5
    copy = open('database/login.py', 'r')
    reader = copy.read()
    for line in reader:
        first_replace = reader.replace('tempuser_12:16', username, 1)
        other_replace = first_replace.replace("'_tempuser16:12'","'" +  password + "'" +  ',', 1)
        final_replace = other_replace.replace('}', "    'tempuser_12:16' : '_tempuser16:12'\n}",1)
    writer = open('database/login.py', 'w')
    writer.write(final_replace)
    return None

def CheckLogin(username, password):
    try:
        if password == login_values_m[username.lower().strip()]:
            pureUsername = login_values_u[username.lower().strip()]
            return True, pureUsername
        return False
    except (KeyError):
        return False

#Make yourself sound Smart
