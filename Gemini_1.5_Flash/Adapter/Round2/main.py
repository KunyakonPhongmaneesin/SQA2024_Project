# main.py
class LegacySystem:
    def calculate_area(self, length, width):
        """คำนวณพื้นที่ของรูปสี่เหลี่ยมผืนผ้า"""
        return length * width


class NewSystemAdapter:
    def __init__(self, legacy_system):
        self.legacy_system = legacy_system

    def calculate_area(self, length, width):
        if length < 0 or width < 0:
            return 0  # คืนค่า 0 หากมีค่าลบ
        return self.legacy_system.calculate_area(length, width)


def main():
    legacy_system = LegacySystem()
    adapter = NewSystemAdapter(legacy_system)

    # ทดสอบการคำนวณพื้นที่
    area1 = adapter.calculate_area(5, 3)
    print(f"Area: {area1}")  # ควรแสดงผลเป็น 15

    area2 = adapter.calculate_area(-1, 3)
    print(f"Area: {area2}")  # ควรแสดงผลเป็น 0


if __name__ == "__main__":
    main()
