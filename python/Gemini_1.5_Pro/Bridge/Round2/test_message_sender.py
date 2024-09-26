from message_sender import Message, SMSSender, EmailSender, EncryptedMessage

def test_sms_send_plain_message(capsys):
    # Arrange
    message = Message("Hello, SMS!")
    sender = SMSSender()

    # Act
    sender.send(message)

    # Assert
    captured = capsys.readouterr()
    assert "Sending SMS: Hello, SMS!" in captured.out

def test_email_send_plain_message(capsys):
    # Arrange
    message = Message("Hello, Email!")
    sender = EmailSender()

    # Act
    sender.send(message)

    # Assert
    captured = capsys.readouterr()
    assert "Sending Email: Hello, Email!" in captured.out

def test_email_send_encrypted_message(capsys):
    # Arrange
    message = Message("Secret Email!")
    encrypted_message = EncryptedMessage(message)
    sender = EmailSender()

    # Act
    sender.send(encrypted_message)

    # Assert
    captured = capsys.readouterr()
    assert "Sending Email: Encrypted: Secret Email!" in captured.out