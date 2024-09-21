import hashlib
import time


def generate_custom_pk():
    current_time = str(time.time()).encode('utf-8')
    return hashlib.sha256(current_time).hexdigest()
