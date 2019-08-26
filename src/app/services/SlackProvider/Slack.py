from ..SlackProvider import client

class SlackNotificationSender:

    @staticmethod
    def send_message(channel_id, message):
        client.chat_postMessage(
            channel=channel_id,
            text=message
        )

# "G6A8820BE"