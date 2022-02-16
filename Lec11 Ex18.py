# The Contact class holds contact information.

class Contact:
    # The _ _init_ _ method initializes the attributes.
    def _ _init_ _(self, name, phone, email):
        self._ _name = name
        self._ _phone = phone
        self._ _email = email

    # The set_name method sets the name attribute.
    def set_name(self, name):
       self._ _name = name

    # The set_phone method sets the phone attribute.
    def set_phone(self, phone):
        self._ _phone = phone

    # The set_email method sets the email attribute.
    def set_email(self, email):
        self._ _email = email

    # The get_name method returns the name attribute.
    def get_name(self):
       return self._ _name

    # The get_phone method returns the phone attribute.
    def get_phone(self):
        return self._ _phone

    # The get_email method returns the email attribute.
    def get_email(self):
        return self._ _email

    # The _ _str_ _ method returns the object's state
    # as a string.
    def _ _str_ _(self):
        return "Name: " + self._ _name + \
        "\nPhone: " + self._ _phone + \
        "\nEmail: " + self._ _email

