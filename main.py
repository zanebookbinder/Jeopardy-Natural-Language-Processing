from flask import Flask, request, render_template
import string
from nltk.tokenize import word_tokenize
import pickle
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("main.html")

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    exclude = set(string.punctuation)
    text = ''.join(ch for ch in text if ch not in exclude)
    text = text.lower()
    text = word_tokenize(text)
    with open('listfile.txt', 'r') as f:
        textlist = f.readlines()
    textlist2 = []
    for element in textlist:
        textlist2.append(element.rstrip())
    data = []
    countdict = []
    for word in textlist2:
         countdict.append(text.count(word))
    data.append(countdict)
    print(textlist2)
    print(countdict)
    with open('picklemodel.pkl', 'rb') as file:
        kmeans = pickle.load(file)
    cluster = kmeans.predict(data)
    print(cluster)
    return 'Your question has been clustered into cluster number: ' + str(cluster[0])

if __name__ == "__main__":
    app.run(debug=True)