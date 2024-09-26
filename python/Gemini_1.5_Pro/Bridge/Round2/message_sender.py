from abc import ABC, abstractmethod


class Message:
    """Abstraction: Represents a message to be sent."""

    def __init__(self, content):
        self.content = content

    def get_content(self):
        return self.content


class MessageSender(ABC):
    """Implementation: Defines the interface for sending messages."""

    @abstractmethod
    def send(self, message):
        pass


class SMSSender(MessageSender):
    """Concrete Implementation: Sends messages using SMS."""

    def send(self, message):
        print(f"Sending SMS: {message.get_content()}")


class EmailSender(MessageSender):
    """Concrete Implementation: Sends messages using Email."""

    def send(self, message):
        print(f"Sending Email: {message.get_content()}")


class EncryptedMessage:
    """Refined Abstraction: Adds encryption to the message."""

    def __init__(self, message):
        self.message = message

    def get_content(self):
        content = self.message.get_content()
        return f"Encrypted: {content}"  # Simulate encryption


if __name__ == "__main__":
    sms_sender = SMSSender()
    email_sender = EmailSender()

    message = Message("Hello, world!")

    # Send plain message
    sms_sender.send(message)

    # Send encrypted message
    encrypted_message = EncryptedMessage(message)
    email_sender.send(encrypted_message)