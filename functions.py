import base64
import urllib.parse
import re
import requests
import jwt
import hashlib

def has_role(user, role_id):
    if isinstance(user, discord.Member):
        role = discord.utils.get(user.roles, id=role_id)
        return role is not None
    return False

def hash_text(text: str):
    hasher = hashlib.sha256()
    hasher.update(text.encode())
    return hasher.hexdigest()

def jwtdec(jwtstr, key):
    try:
        decoded_token = jwt.decode(jwtstr, key, algorithms=['HS256'])
        return f"Decoded Token: {decoded_token}"
    except jwt.ExpiredSignatureError:
        return "Token has expired"
    except jwt.InvalidTokenError:
        return "Invalid token"

def b85enc(text):
    try:
        encoded_text = f"**{base64.b85encode(text.encode('utf-8')).decode('utf-8')}**"
    except:
        encoded_text = "**Invalid Input**"

    return encoded_text

def b85dec(text):
    try:
        decoded_text = f"**{base64.b85decode(text.encode('utf-8')).decode('utf-8')}**"

    except:
        decoded_text = "**Invalid Input**"

    return decoded_text

def b64dec(text):
    try:
        decoded_text = f"**{base64.b64decode(text.encode('utf-8')).decode('utf-8')}**"
    except:
        decoded_text = "**Invalid Input**"

    return decoded_text

def b64enc(text):
    try:
        encoded_text = f"**{base64.b64encode(text.encode('utf-8')).decode('utf-8')}**"
    except:
        encoded_text = "**Invalid Input**"

    return encoded_text


def b64dec(text):
    try:
        decoded_text = f"**{base64.b64decode(text.encode('utf-8')).decode('utf-8')}**"
    except:
        decoded_text = "**Invalid Input**"

    return decoded_text


def b32enc(text):
    try:
        encoded_text = f"**{base64.b32encode(text.encode('utf-8')).decode('utf-8')}**"
    except:
        encoded_text = "**Invalid Input**"

    return encoded_text


def b32dec(text):
    try:
        decoded_text = f"**{base64.b32decode(text.encode('utf-8')).decode('utf-8')}**"
    except:
        decoded_text = "**Invalid Input**"
    return decoded_text


def bin_to_hex(binary_str):
    try:
        return hex(int(binary_str, 2))[2:]
    except:
        return "**Invalid Input**"

def hex_to_bin(hex_str):
    if not all(c in '0123456789ABCDEFabcdef' for c in hex_str):
        raise ValueError('Invalid hexadecimal string')
    return bin(int(hex_str, 16))[2:]


def hex_to_dec(hex_str):
    return int(hex_str, 16)


def dec_to_hex(dec_str):
    return hex(int(dec_str)).split('x')[-1].upper()


def bin_to_str(bins):
    return ''.join(chr(int(bins[i:i+8], 2)) for i in range(0, len(bins), 8))


def str_to_bin(string):
    return ''.join(bin(ord(c))[2:].zfill(8) for c in string)


def cyclic(num):
    text = ""
    alphabeta = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    buffer = "aaa"
    counter = 0
    for i in range(num):
        if int(i / 26) > counter:
            counter += 1
            buffer = buffer.replace(buffer[-(len(buffer) - (int(counter / 26)))],
                                    chr(ord(buffer[-(int(counter / 26))]) + 1))
        text += alphabeta[i % 26]
        text += buffer
    return text


def locate_cyclic(cyc, subs):
    index = cyc.find(subs)
    if index == -1:
        return "Not found"
    return index


def encode_url(url):
    return urllib.parse.quote(url)


def decode_url(url):
    return re.compile('%([0-9a-fA-F]{2})', re.M).sub(lambda m: chr(int(m.group(1), 16)), url)

def get_ctf_events():
    url = 'https://ctftime.org/api/v1/events/'
    params = {'limit': 100}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error: {response.status_code}')
        return None


def team_info():
    url = 'https://ctftime.org/api/v1/teams/266864/'
    params = {'limit': 100}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error: {response.status_code}')
        return None
