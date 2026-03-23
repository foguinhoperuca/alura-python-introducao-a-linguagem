class EmailService:
    @staticmethod
    def send(recipient: str, subject: str, message: str) -> None:
        print(f'[EMAIL] Sending e-mail for {recipient}')
        print(f'[EMAIL] With subject: {subject}')
        print(f'[EMAIL] Message: {message}')
