import base64

with open('111.jpg', 'rb') as icon:
    icon_str = base64.b64encode(icon.read())
    icon_bytes = str(icon_str)
with open('img.py', 'w+') as icon_py:
    icon_py.write(icon_bytes)