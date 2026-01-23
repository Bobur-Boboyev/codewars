class Converter():
    @staticmethod
    def to_ascii(h):
        bytes_object = bytes.fromhex(h)
        decoded_string = bytes_object.decode('utf-8')
        return decoded_string
    
    @staticmethod
    def to_hex(s):
        encoded_s = s.encode("utf-8")
        hex_string = encoded_s.hex()
        return hex_string