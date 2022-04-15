def preprocess_month(month) :
    if month.lower() == 'mar' :
        return [1,0,0,0,0]
    elif month.lower() == 'may' :
        return [0,1,0,0,0]
    elif month.lower() == 'sep' :
        return [0,0,1,0,0]
    elif month.lower() == 'oct' :
        return [0,0,0,1,0]
    elif month.lower() == 'dec' :
        return [0,0,0,0,1]
    else :
        return [0,0,0,0,0]
    
def preprocess_contact(contact) :
    if contact.lower() == 'telephone' : 
        return [1]
    else :
        return [0]
    
    
def preprocess_housing(housing) :
    if housing.lower() == 'yes' : 
        return [1]
    else :
        return [0]   



def preprocess_marital(marital) :
    if marital.lower() == 'married' : 
        return [1]
    else :
        return [0]

def preprocess_poutcome(poutcome) :
    if  poutcome.lower() == 'success' : 
        return [1]
    else :
        return [0]   
    
def preprocess_education(education) :
    if education.lower() == 'university_degree' :
        return [1]
    else :
        return [0]
    
   
    
## data is du=ictionary contains all input from the user
def preprocess_data(data) :
   
    month = preprocess_month(data['month'])
    
    emp_var_rate= data['emp_var_rate']
    
    contact_telephone= preprocess_contact(data['contact_telephone'])
    
    duration= data['duration']
    
    housing= preprocess_housing(data['housing'])
    
    campaign = data['campaign']
    
    marital = preprocess_marital(data['marital'])
    
    poutcome=preprocess_poutcome(data['poutcome'])
    
    previous = data['previous']
    
    education = preprocess_education(data['education'])
    
    final_data = month+ [emp_var_rate] + contact_telephone +[duration]+ housing+ [campaign]+ marital+poutcome+[previous] +education
    return final_data