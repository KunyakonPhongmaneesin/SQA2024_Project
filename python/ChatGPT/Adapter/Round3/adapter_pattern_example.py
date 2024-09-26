# Legacy EmailSender class
class EmailSender:
    def send_email(self, message: str) -> str:
        return f"Email sent: {message}"

# New SMSSender class
class SMSSender:
    def send_sms(self, message: str) -> str:
        return f"SMS sent: {message}"

# Adapter class to adapt SMSSender to EmailSender's interface
class SMSSenderAdapter(EmailSender):
    def __init__(self, sms_sender: SMSSender):
        self.sms_sender = sms_sender

    def send_email(self, message: str) -> str:
        # Adapting send_sms to the send_email method
        return self.sms_sender.send_sms(message)

# Example usage
def main():
    email_sender = EmailSender()
    sms_sender = SMSSender()
    sms_adapter = SMSSenderAdapter(sms_sender)

    # Both can now use the send_email method
    print(email_sender.send_email("Hello via Email"))
    print(sms_adapter.send_email("Hello via SMS Adapter"))

if __name__ == "__main__":
    main()
