class Candidate:
    name = None
    email = None
    mobile_phone = None
    cultural_fit = None
    logic_test = None
    college = None
    # birthday = None
    graduation = None

    def __init__(self, name=None, email=None, mobile_phone=None, cultural_fit=None, logic_test=None, college=None,
                 birthday=None, graduation=None):
        super().__init__()
        self.name = name
        self.email = email
        self.mobile_phone = mobile_phone
        self.cultural_fit = cultural_fit
        self.logic_test = logic_test
        self.college = college
        # self.birthday = birthday
        self.graduation = graduation
