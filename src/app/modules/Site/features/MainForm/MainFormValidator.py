from app.abstracts.Validator import Validator
from validate_email import validate_email

class MainFormValidator(Validator):
    def __init__(self):
        self._is_valid = True
        self._error_message = []
    
    @property
    def is_valid(self):
        return self._is_valid
    
    @is_valid.setter
    def is_valid(self, value):
        self._is_valid = value
    
    @property
    def error_message(self):
        return ', '.join(self._error_message)

    @error_message.setter
    def error_message(self, value):
        self._error_message.append(value)

    def validate(self, data):
        # Validate required fields
        required_fields = ['username', 'email', 'url']
        for field_name in required_fields:
            self.validate_required_field(field_name, data)
        # Validate email
        if 'email' in data:
            self.validate_email_field(data['email'])
    

    def validate_required_field(self, field_name, data):
        if not field_name in data or not data[field_name]:
            self.is_valid = False
            self.error_message = f'{field_name} is required'
    
    def validate_email_field(self, email):
        is_valid = validate_email(email)
        if not is_valid:
            self.is_valid = False
            self.error_message = f'email: {email} is not valid'

