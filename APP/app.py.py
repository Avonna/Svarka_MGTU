#!/usr/bin/env python
# coding: utf-8

# In[1]:


import flask
import pickle
from flask import render_template


# In[7]:


app = flask.Flask(__name__, template_folder = 'templates')
@app.route('/', methods = ['POST', 'GET'])
def index():
    if flask.request.method == 'GET':
        return render_template('index.html')
    if flask.request.method == 'POST':
        with open('gbr_model.pkl', 'rb') as width:
            load_width = pickle.load(width)
        with open('gbr_1_model.pkl', 'rb') as depth:
            load_depth = pickle.load(depth)
        IW = float(flask.request.form['IW'])
        IF = float(flask.request.form['IF'])
        VW = float(flask.request.form['VW'])
        FP = float(flask.request.form['FP'])
        y_width = load_width.predict([[IW, IF, VW, FP]])
        y_depth = load_depth.predict([[IW, IF, VW, FP]])

        return render_template('main.html', result = (round(y_width[0], 2), round(y_depth[0], 2)))


# In[8]:


if __name__ == '__main__':
    app.run()


# In[ ]:




