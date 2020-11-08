def age_assignment(*args, **kwargs):
    persons_name = {}
    for name in args:
        persons_name[name] = kwargs[name[0]]
    return persons_name


#persons = {name: kwargs[name[0]] for name in args}


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
