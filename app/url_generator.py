
import hashlib

class URLGenerator:
    @staticmethod
    def generate_short_code(url):
        # Generate a short code using MD5 hash of the URL
        hash_object = hashlib.md5(url.encode())
        return hash_object.hexdigest()[:8]  # Return first 8 characters of the hash
