from flask import Flask, redirect, url_for, render_template, request, session
import json
import sys
import os
import features_module as fm


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_route():
    dict={}
    if request.method == 'GET':
        dict['question']=''
        dict['refans']=''
        dict['studans']=''
        dict['result']=''
        dict['display']='none'
    elif request.method == 'POST':
        dict['question']=request.form['question']
        dict['refans']=request.form['refans']
        dict['studans']=request.form['studans']
        dict['display']='block'
        f=fm.get_features([request.form['studans']],request.form['refans'],request.form['question'])
        x=fm.get_prob(f)[0]
        print(x)
        p=""
        c=''
        if x[1]>0.55:
            p='correct'
            c='ag'
        elif x[1]>0.3:
            p='partially correct'
            c='ap'
        else:
            p='wrong'
            c='ar'
        dict['result']=p
        dict['scoreclass']=c
        dict['score']=round(x[1]*10,1)+1
        columns = ['prompt_overlap','av_word_len','sent_length','Cosine w2v','Cosine d2v','FSTS','Cosine Elmo','LSA 1','LSA 2','LSA 3','TTR','JC Sim','SP Sim','Cosine USE']
        # explainer = shap.TreeExplainer(fm.clf)
        # shap_values = explainer.shap_values(f)
        # shap.initjs()
        # dict['explain']=shap.force_plot(explainer.expected_value[1], shap_values[1], columns)
    return render_template('home.html',data=dict)


if __name__ == "__main__":
    app.secret_key = os.urandom(12)  # Generic key for dev purposes only
    app.run(debug=True, use_reloader=True)
