
import hashlib

class URLGenerator:
    
    def md5_hash_generator(self, url):
        # Generate a short code using MD5 hash of the URL
        hash_object = hashlib.md5(url.encode())
        return hash_object.hexdigest()[:7]  # Return first 8 characters of the hash
    
    @staticmethod
    def generate_short_code(self, url, method):
        if method == 'md5':
            return self.md5_hash_generator(url)
        else:
            return {'success':False, 'message':f'No hashing method matching :: {method}'}



