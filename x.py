text = "http://127.0.0.1:5000/static/images.jpeg"
text = text.split('/')
print(text)
text = text[3:]
print(text)
print('/'.join(text))