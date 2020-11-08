class NameTooShortError(Exception):
    """ Raised when the username is less than or equal to 4 """
    pass


class MustContainAtSymbolError(Exception):
    """ Raised when there is no "@" in the email"""
    pass


class InvalidDomainError(Exception):
    """ Raised when the domain of the email is invalid """
    pass


def validate_name(email):
    username = email.split("@")[0]
    if len(username) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")


def validate_at_symbol(email):
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")


def validate_domain(email):
    domain = email.split(".")[-1]
    if domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")


valid_domains = ("com", "bg", "org", "net")

while True:
    email = input()
    if email == "End":
        break
    else:
        validate_name(email)
        validate_at_symbol(email)
        validate_domain(email)

    print("Email is valid")