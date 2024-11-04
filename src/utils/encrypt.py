from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

def encode(key,text):
    cipher = AES.new(key, AES.MODE_CBC)
    text_bytes = cipher.encrypt(pad(text.encode(), AES.block_size))
    vi = base64.b64encode(cipher.iv).decode("utf-8")
    texto_cifrado = base64.b64encode(text_bytes).decode("utf-8")
    return vi, texto_cifrado

def generate_key():
    return get_random_bytes(32)

def decode(key, vi,texto_cifrado):
    iv = base64.b64decode(vi)
    texto_cifrado = base64.b64decode(texto_cifrado)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(texto_cifrado), AES.block_size)
    return pt.decode("utf-8")
