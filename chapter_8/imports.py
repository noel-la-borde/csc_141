# Imports

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('Noel', 'La Borde',
                            weight='192 pounds',
                            height='5,11',
                            occupation= 'Student'
                            )
print(user_profile)
