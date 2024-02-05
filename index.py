import hug

@hug.get('/hello')
def hello():
    return "Hello, World!"

print("https://localhost:8000")