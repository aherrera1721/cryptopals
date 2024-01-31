"""
Convert hex to base64
"""
import base64

def hex_to_base64(hex_string: str) -> str:
    raw_bytes = bytes.fromhex(hex_string)
    return base64.b64encode(raw_bytes).decode()

if __name__ == '__main__':
    hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    base64_string = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

    output = hex_to_base64(hex_string)
    print(f'{output=}')
    assert output == base64_string