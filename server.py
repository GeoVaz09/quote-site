from flask import Flask, render_template
import random
import os

app = Flask(__name__)


quotes_file = 'quotes.txt'
quote = ""

def pick_one_quote():
    if not os.path.exists(quotes_file):
        return "No quotes available."
    with open(quotes_file, 'r') as f:
        lines = f.readlines()
        text = lines[random.randint(0, len(lines))]
        return text
    return "No quotes available."

@app.route('/')
def index():
    quote = pick_one_quote()
    return render_template('index.html', quote=quote)

if __name__=='__main__': 
   app.run(debug=True, host="0.0.0.0") 