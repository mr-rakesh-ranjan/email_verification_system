from db_config import get_data
import json as js

def generate_otp():
    import random, math
    digits = "0123456789"
    OTP = ""
    
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]

    return OTP
