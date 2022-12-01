from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

def get_prediction(parms_float):
    pickle_model_file = './model/knn_model.pkl'
    with open(pickle_model_file, 'rb') as file:
        pickle_model = pickle.load(file)
    Ypredict_pckl = pickle_model.predict(parms_float)
    return Ypredict_pckl[0]

@app.route('/', methods=['post', 'get'])
def processing():
    depth = 0.0
    width = 0.0
    if request.method == 'POST':
        IW = request.form.get('IW')
        IF = request.form.get('IF')
        VW = request.form.get('VW')
        FP = request.form.get('FP')
        parms = [IW,IF,VW,FP]

        try:
            parms_float = np.array([[float(param) for param in parms]])
            depth, width = get_prediction(parms_float)
        except Exception as e:
            print(e)
    return render_template('index.html', depth=depth, width=width)

if __name__ == '__main__':
    app.run()
