"""
Fixed XOR
"""

def fixed_xor(buffer_1: str, buffer_2: str) -> str:
    hex_1 = bytes.fromhex(buffer_1)
    hex_2 = bytes.fromhex(buffer_2)
    int_xor = int.from_bytes(hex_1) ^ int.from_bytes(hex_2)
    bytes_xor = int_xor.to_bytes((int_xor.bit_length() + 7) // 8)
    return bytes_xor.hex()

if __name__ == '__main__':
    buffer_1 = '1c0111001f010100061a024b53535009181c'
    buffer_2 = '686974207468652062756c6c277320657965'
    xor = '746865206b696420646f6e277420706c6179'

    output = fixed_xor(buffer_1, buffer_2)
    print(f"{output=}")
    assert output == xor