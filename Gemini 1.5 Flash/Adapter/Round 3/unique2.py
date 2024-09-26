class OldAPI:
    def get_data(self):
        return {"key1": "value1", "key2": "value2"}

class NewAPIAdapter:
    def fetch_data(self):
        old_data = self.old_api.get_data()
        new_data = {"data": old_data}
        return new_data