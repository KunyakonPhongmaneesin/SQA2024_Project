import pytest
import requests_mock
from emoji_translator import EnglishText, EmojiProcessor, EmojiAPIAdapter

def test_process_with_successful_api_call(monkeypatch):
    # Arrange
    english_text = EnglishText("Hello world!")
    adapter = EmojiAPIAdapter(english_text)

    # Mock API response
    with requests_mock.Mocker() as m:
        m.post('https://api.example.com/translate', 
               json={'emoji_text': '👋 🌍!'})
        emoji_text = adapter.get_emoji_text()

    processor = EmojiProcessor()

    # Act
    processor.process_text(emoji_text)

    # Assert (would usually check output)
    # Check if the output contains emojis

def test_process_with_failed_api_call(monkeypatch):
    # Arrange
    english_text = EnglishText("Hello world!")
    adapter = EmojiAPIAdapter(english_text)

    # Mock API failure
    with requests_mock.Mocker() as m:
        m.post('https://api.example.com/translate', status_code=500)
        emoji_text = adapter.get_emoji_text()

    processor = EmojiProcessor()

    # Act
    processor.process_text(emoji_text)

    # Assert (would usually check output)
    # Check if the output contains original text 