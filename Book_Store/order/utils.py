import base64
from django.core.mail import EmailMessage


class Utils:
    @staticmethod
    def send_mail(data):
        message = EmailMessage(
            subject=data.get('subject'), body=data.get('email_body'), to=[data.get('email')])
        message.send()

    @staticmethod
    def token_short(token):
        token_string_bytes = token.encode("ascii")

        base64_bytes = base64.b64encode(token_string_bytes)
        base64_string = base64_bytes.decode("ascii")

        return base64_string

    @staticmethod
    def true_token(token_):
        base64_bytes = token_.encode("ascii")

        sample_string_bytes = base64.b64decode(base64_bytes)
        sample_string = sample_string_bytes.decode("ascii")
        return sample_string
