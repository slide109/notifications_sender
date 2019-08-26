from typing import Dict

class MainFormData:

    def __init__(self, form_data: Dict[str, str]):
        self.username = form_data['username']
        self.email = form_data['email']
        self.url = form_data['url']
        self.phone = form_data['phone'] if 'phone' in form_data else ''
        self.message = form_data['message'] if 'message' in form_data else ''
        self.productName = form_data['productName'] if 'productName' in form_data else ''
        self.price = form_data['price'] if 'price' in form_data else ''
