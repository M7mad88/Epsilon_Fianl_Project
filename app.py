import joblib
from flask import Flask, render_template, request
import preprocess  
import numpy as np

app=Flask(__name__,template_folder='templates')


model=joblib.load('models/model_xgb.h5')
@app.route('/') 
def index() :
    return render_template('index.html')

@app.route('/predict', methods = ['POST', 'GET']) 
def get_prediction() :
    if request.method == 'POST':
        month= request.form['month']
        evr= request.form['evr']
        contact= request.form['contact']
        duration= request.form['duration']
        house= request.form['house']
        campaign= request.form['campaign']
        marital= request.form['marital']
        poutcome= request.form['poutcome']
        previous= request.form['previous']
        education= request.form['education']
    

    data={ 'month': month, 'emp_var_rate': evr, 'contact_telephone': contact,
           'duration': duration, 'housing': house, 'campaign': campaign, 'marital': marital,
           'poutcome': poutcome, 'previous': previous, 'education': education}
    
    final_data = preprocess.preprocess_data(data)
    prediction = model.predict(np.array(final_data).reshape(1,14), validate_features=False)[0]
    
    # return str(prediction)
    return render_template('prediction.html', bank_deposit = str(prediction))
        
    
if __name__== '__main__':
    app.run(debug=True)
   