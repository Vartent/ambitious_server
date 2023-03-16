class EmailParse:
    email: str
    username: str
    domain_full: str
    domain_top: str
    domain_name: str

    @classmethod
    def get_username(cls, email: str) -> str:
        s: str = ""
        for c in email:
            if c != "@":
                s += c
            else:
                return s
        raise "Email form is invalid"

    @classmethod
    def get_domain_full(cls, email: str) -> str:
        return email[len(cls.get_username(email)) + 1:]

    @classmethod
    def get_domain_name(cls, domain_full: str) -> str:
        s: str = ""
        for c in domain_full:
            if c != ".":
                s += c
            else:
                return s
        raise "Domain name id invalid"

    @classmethod
    def get_domain_top(cls, domain_full: str):
        return domain_full[len(cls.get_domain_name(domain_full)) + 1:]

    def __init__(self, email: str):
        self.email = email
        self.username = self.get_username(email)
        self.domain_full = self.get_domain_full(email)
        self.domain_name = self.get_domain_name(self.domain_full)
        self.domain_top = self.get_domain_top(self.domain_full)
