def main():
    legacy_system = LegacySystem()
    adapter = NewSystemAdapter(legacy_system)

    result = adapter.new_operation("data")
    print(result)