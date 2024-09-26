import pytest
from adapter_pattern_example import EmailSender, SMSSender, SMSSenderAdapter

# Test using the AAA pattern (Arrange, Act, Assert)

def test_email_sender_send_email():
    # Arrange
    email_sender = EmailSender()

    # Act
    result = email_sender.send_email("Hello via Email")

    # Assert
    assert result == "Email sent: Hello via Email"

def test_sms_adapter_send_email():
    # Arrange
    sms_sender = SMSSender()
    sms_adapter = SMSSenderAdapter(sms_sender)

    # Act
    result = sms_adapter.send_email("Hello via SMS Adapter")

    # Assert
    assert result == "SMS sent: Hello via SMS Adapter"

# 100% Branch Coverage Test:
def test_adapter_branch_coverage():
    # Arrange
    email_sender = EmailSender()
    sms_sender = SMSSender()
    sms_adapter = SMSSenderAdapter(sms_sender)

    # Act & Assert
    assert email_sender.send_email("Branch Coverage Test for EmailSender") == "Email sent: Branch Coverage Test for EmailSender"
    assert sms_adapter.send_email("Branch Coverage Test for SMSSenderAdapter") == "SMS sent: Branch Coverage Test for SMSSenderAdapter"
