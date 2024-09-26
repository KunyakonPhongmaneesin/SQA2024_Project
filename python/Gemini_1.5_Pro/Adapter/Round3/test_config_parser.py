import pytest
from config_parser import INIParser, JSONConfigHandler, INItoJSONAdapter

@pytest.fixture
def sample_ini_content():
    return """
    [DATABASE]
    host = localhost
    port = 5432

    [API]
    key = your_api_key
    """

def test_ini_to_json_conversion(sample_ini_content, tmp_path):
    # Arrange
    ini_file = tmp_path / "config.ini"
    ini_file.write_text(sample_ini_content)
    ini_parser = INIParser(str(ini_file))
    adapter = INItoJSONAdapter(ini_parser)

    # Act
    json_config = adapter.get_json_config()

    # Assert
    assert json_config == '{"DATABASE": {"host": "localhost", "port": "5432"}, "API": {"key": "your_api_key"}}'

def test_json_config_load(capsys):
    # Arrange
    json_data = '{"section1": {"key1": "value1"}, "section2": {"key2": "value2"}}'
    json_handler = JSONConfigHandler()

    # Act
    json_handler.load_config(json_data)

    # Assert
    captured = capsys.readouterr()
    assert "Configuration loaded from JSON:" in captured.out
    assert "  section1:" in captured.out
    assert "  section2:" in captured.out

def test_json_config_load_error(capsys):
    # Arrange
    invalid_json_data = '{"section1": {"key1": "value1", "section2": {"key2": "value2"'  # Invalid JSON
    json_handler = JSONConfigHandler()

    # Act
    json_handler.load_config(invalid_json_data)

    # Assert
    captured = capsys.readouterr()
    assert "Error loading JSON configuration:" in captured.out