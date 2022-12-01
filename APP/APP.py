#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Импортируем необходимые библиотеки для нашего приложения
import numpy as np
import tensorflow as tf
from tensorflow import keras
from flask import Flask, request, render_template


# In[8]:


app = Flask(__name__)


# In[3]:


# Загружаем модель и определяем параметры функции  -  будущие входы для модели (всего 12 параметров)

def set_params(IW, IF, VW, FP):

    model = keras.models.load_model(r"C:\Users\Avona\Desktop\Итоговая работа\APP\models\model_1")
    prediction = model.predict([IW, IF, VW, FP])

    return prediction[0][0]


# In[ ]:


@app.route('/', methods=['post', 'get'])

def app_calculation():
    param_lst = []
    message = ''
    if request.method == 'POST':
        
       # получим данные из наших форм и кладем их в список, который затем передадим функции set_params
        for i in range(1,13,1):
            param = request.form.get(f'param{i}')
            param_lst.append(float(param))
            
        message = set_params(*param_lst)

    # указываем шаблон и прототип сайта для вывода    
    return render_template("C:/Users/Avona/Desktop/Итоговая работа/APP/templates/index.html", message = message) 

# Запускаем приложение  
app.run(debug=True)


# In[ ]:




