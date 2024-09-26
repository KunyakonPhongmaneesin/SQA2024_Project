import configparser
import json


class INIParser:
    """Existing class to parse INI configuration files."""

    def __init__(self, filepath):
        self.filepath = filepath
        self.config = configparser.ConfigParser()
        self.config.read(self.filepath)

    def get_setting(self, section, option):
        return self.config.get(section, option)


class JSONConfigHandler:
    """Target interface: Expects configuration data in JSON format."""

    def load_config(self, json_data):
        try:
            config_dict = json.loads(json_data)
            print("Configuration loaded from JSON:")
            for key, value in config_dict.items():
                print(f"  {key}: {value}")
        except json.JSONDecodeError as e:
            print(f"Error loading JSON configuration: {e}")


class INItoJSONAdapter:
    """Adapter: Converts INI config data to JSON format."""

    def __init__(self, ini_parser):
        self.ini_parser = ini_parser

    def get_json_config(self):
        """Converts INI data to a JSON string."""
        config_dict = {}
        for section in self.ini_parser.config.sections():
            config_dict[section] = dict(self.ini_parser.config.items(section))
        return json.dumps(config_dict)


if __name__ == "__main__":
    ini_file = "config.ini"
    ini_parser = INIParser(ini_file)

    adapter = INItoJSONAdapter(ini_parser)
    json_config = adapter.get_json_config()

    json_handler = JSONConfigHandler()
    json_handler.load_config(json_config)