import sys
import os

# เพิ่ม path ไปยังไดเรกทอรีที่มี main.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Copilot_Adapter_R1 import Target, Adaptee, Adapter, client_code
