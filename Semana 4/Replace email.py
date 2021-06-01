def replace_domanin(email, old_domain, new_domain ):
    if "@" + old_domain in email:
        index = email.index("@"+old_domain)
        return email[:index] + "@" + new_domain
    return email
