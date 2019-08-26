def create_slack_message(
        username: str,
        email: str,
        url: str,
        phone: str,
        message: str,
        productName: str,
        price: str,
    ):

    message_dict = {
        'От': username,
        'Email': email,
        'Страница': url,
        'Телефон': phone,
        'Сообщение': message,
        'Продукт': productName,
        'Цена на сайте': price,
    }

    return '\n'.join(['%s: %s' % (key, value) for (key, value) in message_dict.items()])