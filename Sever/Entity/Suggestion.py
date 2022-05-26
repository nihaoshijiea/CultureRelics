class Suggestion:
    def __init__(self):
        self.Id = ""
        self.letter_headline = ""
        self.letter_information = ""
        self.letter_type = ""
        self.occupation = ""
        self.subdistrict = ""
        self.telephone = ""
        self.user_id = ""
        self.user_name = ""
        self.user_sex = ""
        self.param_list = ['Id',
                           'letter_headline',
                           'letter_information',
                           'letter_type',
                           'occupation',
                           'subdistrict',
                           'telephone',
                           'user_id',
                           'user_name',
                           'user_sex']
        self.param_dict = {'Id': "",
                           'letter_headline': "",
                           'letter_information': "",
                           'letter_type': "",
                           'occupation': "",
                           'subdistrict': "",
                           'telephone': "",
                           'user_id': "",
                           'user_name': "",
                           'user_sex': ""}
        self.table_name = "suggestion"


    def set_param_dict(self):
        self.param_dict['Id'] = self.Id
        self.param_dict['letter_headline'] = self.letter_headline
        self.param_dict['letter_information'] = self.letter_information
        self.param_dict['letter_type'] = self.letter_type
        self.param_dict['occupation'] = self.occupation
        self.param_dict['subdistrict'] = self.subdistrict
        self.param_dict['telephone'] = self.telephone                                                                     
        self.param_dict['user_id'] = self.user_id
        self.param_dict['user_name'] = self.user_name
        self.param_dict['user_sex'] = self.user_sex






