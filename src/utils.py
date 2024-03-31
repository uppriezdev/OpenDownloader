import math
import mimetypes
import typer
import requests

def get_file_type(filename):
    file_type, _ = mimetypes.guess_type(filename)
    if file_type:
        return file_type.split('/')[1].upper()
    else:
        return "Unknown"

def bytes_to_size(bytes: int) -> str:
    sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB', "PB", "EB", "ZB", "YB"]

    try:
        bytes = int(bytes)
    except ValueError:
        return 'Invalid input'
    if bytes < 0:
        return 'Invalid input'
    i = int(math.floor(math.log(bytes) / math.log(1024)))
    return f"{(bytes / (1024 ** i)):.1f} {sizes[i]}"

def get_file_size(url):
    response = requests.head(url)
    if response.status_code == 200:
        size = int(response.headers.get('content-length', 0))
        return size
    else:
        return 0
