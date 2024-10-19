from flask import Flask
import os
from datetime import datetime
import subprocess
import pytz
import getpass

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system username
    username = getpass.getuser()
    
    # Get current server time in IST
    ist_tz = pytz.timezone('Asia/Kolkata')
    ist_time = datetime.now(ist_tz).strftime('%Y-%m-%d %H:%M:%S')

    # Get top output (for demonstration, we'll limit it to the first 10 lines)
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8').splitlines()[:10]
    except Exception as e:
        top_output = [f"Error retrieving top output: {str(e)}"]

    return f"""
    <h1>System Information</h1>
    <p>Name: Your Full Name</p>
    <p>Username: {username}</p>
    <p>Server Time (IST): {ist_time}</p>
    <h2>Top Output:</h2>
    <pre>{'\n'.join(top_output)}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
