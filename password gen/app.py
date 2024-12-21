from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length, use_lower, use_upper, use_special, use_numbers):
    characters = ''
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        return "Error: No character sets selected!"
    
    characters=shuffle_more(characters)
    password = ''.join(random.sample(characters, length))
    random_password = shuffle_more(password)
    return random_password\
    
@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        length = int(request.form.get('length', 8))
        use_lower = 'lowercase' in request.form
        use_upper = 'uppercase' in request.form
        use_special = 'special' in request.form
        use_numbers = 'numbers' in request.form

        password = generate_password(length, use_lower, use_upper, use_special, use_numbers)
        return render_template('index.html', password=password)
    return render_template('index.html', password=None)

def shuffle_more(password):

    password_list=list(password)

    for _ in range(200): random.shuffle(password_list)

    return ''.join(password_list)

if __name__ == '__main__':
    app.run(debug=True)
