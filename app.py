# save this as app.py
from flask import Flask, request, render_template
from markupsafe import escape
import pickle

vector = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("finalized_model.pkl", "rb"))

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        news = str(request.form['news'])
        predict = model.predict(vector.transform([news]))[0]
        print(predict)
        return render_template("index.html",prediction_text = "News is ->{}".format(predict))
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run()
