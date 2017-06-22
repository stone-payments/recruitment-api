class Candidate:

    def __init__(self, name=None, email=None, mobile_phone=None,
                 cultural_fit=None, logic_test=None, college=None,
                 graduation=None, is_present = False, event=None):
        super().__init__()
        self.event = event
        self.is_present = is_present
        self.name = name
        self.email = email
        self.mobile_phone = mobile_phone
        self.cultural_fit = cultural_fit
        self.logic_test = logic_test
        self.college = college
        self.graduation = graduation
