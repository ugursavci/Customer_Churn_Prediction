import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    TENURE = int(request.form['Tenure'])
    MONTHLYCHARGES= float(request.form['Monthly Charges'])

            ####### Contract #######
            ########################
    Contract = request.form['Contract']
    if Contract =='One Year':
        CONTRACT_One_year = 1
        CONTRACT_Two_year = 0
    elif Contract =='Two Years':
        CONTRACT_One_year = 0
        CONTRACT_Two_year = 1
    else:
        CONTRACT_One_year = 0
        CONTRACT_Two_year = 0


        ##########TECHSUPPORT############
        #################################

    TECHSUPPORT = request.form['TechSupport']
    if TECHSUPPORT == 'Yes':
        TECHSUPPORT_No_internet =0
        TECHSUPPORT_Yes = 1
        TECHSUPPORT_Yes = 1
    elif TECHSUPPORT == 'No Internet':
        TECHSUPPORT_No_internet = 1
        TECHSUPPORT_Yes = 0
    else:
        TECHSUPPORT_No_internet = 0
        TECHSUPPORT_Yes = 0

        #########INTERNET SERVICE ###########
        #####################################

    Internet_Service = request.form['Internet Service']

    if Internet_Service == "Fiber optic":
        INTERNETSERVICE_Fiber_optic = 1
        INTERNETSERVICE_No = 0

    elif Internet_Service == "No Internet Service":
        INTERNETSERVICE_Fiber_optic = 1
        INTERNETSERVICE_No = 0

    else:
        INTERNETSERVICE_Fiber_optic = 0
        INTERNETSERVICE_No = 0

            ##########ONLINE SECURITY###############
            ########################################

    Online_Security = request.form['Online Security']

    if Online_Security == 'Yes':
        ONLINESECURITY_No_internet =0
        ONLINESECURITY_Yes = 1
    elif Online_Security == 'No Internet Service':
        ONLINESECURITY_No_internet = 1
        ONLINESECURITY_Yes = 0
    else :
        ONLINESECURITY_No_internet = 0
        ONLINESECURITY_Yes = 0

    ############ DEVICEPROTECTION ################
##############################################

    Device_Protection = request.form['Device Protection']

    if Device_Protection == 'Yes':
        DEVICEPROTECTION_No_internet = 0
        DEVICEPROTECTION_Yes = 1
    elif Device_Protection == 'No Internet Service':
        DEVICEPROTECTION_No_internet = 1
        DEVICEPROTECTION_Yes = 0
    else:
        DEVICEPROTECTION_No_internet = 0
        DEVICEPROTECTION_Yes = 0


                    #########PAYMENTMETHOD##########
                    ################################

    Payment_Method = request.form['Payment Method']
    if Payment_Method == 'Credit card (automatic)':
        PAYMENTMETHOD_Credit_card_automatic = 1
        PAYMENTMETHOD_Electronic_check = 0
        PAYMENTMETHOD_Mailed_check = 0
    elif Payment_Method == 'Electronic check':
        PAYMENTMETHOD_Credit_card_automatic = 0
        PAYMENTMETHOD_Electronic_check = 1
        PAYMENTMETHOD_Mailed_check = 0
    elif Payment_Method == 'Mailed Check':

        PAYMENTMETHOD_Credit_card_automatic = 0
        PAYMENTMETHOD_Electronic_check = 0
        PAYMENTMETHOD_Mailed_check = 1
    else:
        PAYMENTMETHOD_Credit_card_automatic = 0
        PAYMENTMETHOD_Electronic_check = 0
        PAYMENTMETHOD_Mailed_check = 0

                        ######STREAMINGMOVIES#######
                        ############################

    Streaming_Movies = request.form['Streaming Movies']

    if Streaming_Movies == 'Yes':
        STREAMINGMOVIES_No_internet = 0
        STREAMINGMOVIES_Yes = 1
    elif Streaming_Movies == 'No Internet Service':
        STREAMINGMOVIES_No_internet = 0
        STREAMINGMOVIES_Yes = 1
    else :
        STREAMINGMOVIES_No_internet = 0
        STREAMINGMOVIES_Yes = 0

            ########ONLINE BACKUP#########
            ##############################

    Online_Backup = request.form['Online Backup']

    if Online_Backup == 'Yes':
        ONLINEBACKUP_No_internet = 0
        ONLINEBACKUP_Yes = 1
    elif Online_Backup == 'No Internet Service':
        ONLINEBACKUP_No_internet = 1
        ONLINEBACKUP_Yes = 0
    else:
        ONLINEBACKUP_No_internet = 0
        ONLINEBACKUP_Yes = 0

    prediction = model.predict(np.array([TENURE,
    MONTHLYCHARGES,
    CONTRACT_One_year,
    CONTRACT_Two_year,
    TECHSUPPORT_No_internet,
    TECHSUPPORT_Yes,
    INTERNETSERVICE_Fiber_optic,
    INTERNETSERVICE_No,
    ONLINESECURITY_No_internet,
    ONLINESECURITY_Yes,
    DEVICEPROTECTION_No_internet,
    DEVICEPROTECTION_Yes,
    PAYMENTMETHOD_Credit_card_automatic,
    PAYMENTMETHOD_Electronic_check,
    PAYMENTMETHOD_Mailed_check,
    STREAMINGMOVIES_No_internet,
    STREAMINGMOVIES_Yes,
    ONLINEBACKUP_No_internet,
    ONLINEBACKUP_Yes]).reshape(1, -1))

    output = prediction[0]
    if output == 0:
        return render_template('index.html',prediction_text = 'Customer will not churn')
    else:
        return render_template('index.html', prediction_text='Customer will churn')

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)