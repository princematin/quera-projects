# user, password verify func

def check_registration_rules(**kwargs: str) -> list[str]:
    verified_users = []
    for key, value in kwargs.items():
        if len(key) >= 4:
            if key == 'quera' or key == 'codecup':
                continue
            else:
                if len(value) >= 6:
                    if value.isnumeric() == False:
                        verified_users.append(key)
    return verified_users
