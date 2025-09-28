from flask import Flask, render_template_string, request
import time
import os

app = Flask(__name__)
start_time = time.time()

@app.route('/')
def home():
    uptime = time.time() - start_time
    hours = int(uptime // 3600)
    minutes = int((uptime % 3600) // 60)
    
    html_template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>BANDUM CYBERSECURITY</title>
        <style>
            body { 
                background: #000;
                color: #0f0;
                font-family: 'Courier New', monospace;
                margin: 0;
                padding: 20px;
            }
            .container {
                max-width: 800px;
                margin: 50px auto;
                border: 2px solid #0f0;
                padding: 30px;
                border-radius: 15px;
                text-align: center;
            }
            h1 {
                color: #ff0;
                text-shadow: 0 0 10px #0f0;
            }
            .btn {
                display: inline-block;
                padding: 12px 24px;
                background: #0f0;
                color: #000;
                text-decoration: none;
                border-radius: 5px;
                font-weight: bold;
                margin: 10px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🛡️ BANDUM CYBERSECURITY</h1>
            <p>Server Online dan Stabil</p>
            <p>Uptime: ''' + f'{hours} jam {minutes} menit' + '''</p>
            <a href="/login" class="btn">🔐 LOGIN</a>
        </div>
    </body>
    </html>
    '''
    return html_template

@app.route('/login')
def login():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Login - BANDUM</title>
        <style>
            body { 
                background: #000; 
                color: #0f0; 
                font-family: monospace; 
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .login-box { 
                width: 90%;
                max-width: 400px; 
                padding: 30px; 
                border: 2px solid #0f0; 
                border-radius: 10px;
                text-align: center;
            }
            input { 
                width: 100%; 
                padding: 12px; 
                margin: 10px 0; 
                background: #111; 
                color: #0f0; 
                border: 1px solid #0f0; 
                border-radius: 5px;
            }
            button { 
                padding: 12px 24px; 
                background: #0f0; 
                color: #000; 
                border: none; 
                border-radius: 5px;
                cursor: pointer; 
                font-weight: bold;
                width: 100%;
            }
        </style>
    </head>
    <body>
        <div class="login-box">
            <h2>🔐 LOGIN BANDUM</h2>
            <form>
                <input type="text" placeholder="Username" required>
                <input type="password" placeholder="Password" required>
                <button type="submit">LOGIN</button>
            </form>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
  
