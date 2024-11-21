from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey' 

@app.route('/')
def home():
    return render_template('register.html')

users = []  

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    if username: 
        users.append(username)  
        flash(f'Bienvenido, {username}!', 'success')  
        return redirect(url_for('welcome', username=username))
    else:
        flash('El nombre de usuario es obligatorio.', 'error')
        return redirect(url_for('home'))

@app.route('/welcome/<username>')
def welcome(username):
    return render_template('welcome.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
