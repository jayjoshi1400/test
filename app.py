from flask import Flask, request
from sts import find_sim
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        data = request.get_json()
        if data:
            if 'text1' in data:
                text1 = data['text1']
            if 'text2' in data:
                text2 = data['text2']
            sim = find_sim(text1, text2)
        return sim
    else:
        return '<h1>Please pass the texts in the format provided</h1>'

if __name__ == "__main__":
    app.run(debug=True)