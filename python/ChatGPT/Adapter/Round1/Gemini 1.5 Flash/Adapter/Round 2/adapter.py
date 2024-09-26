class NewSystemAdapter:
    def __init__(self, legacy_system):
        self.legacy_system = legacy_system

    def new_operation(self, data):
        # Adapt the old operation to the new interface
        return self.legacy_system.old_operation(data)