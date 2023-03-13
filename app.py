#Importing Modules
from flask import Flask, render_template, request
from keras.models import load_model
from keras.utils import load_img, img_to_array
import numpy as np
import os

#intializing the flask app
app  = Flask('Soil_Identifier',template_folder=r'C:\Users\hp\Documents\SoilStation-Website\templates', static_folder =r'C:\Users\hp\Documents\SoilStation-Website\static')

#Class of soil
classes = ["Black Soil","Laterite Soil","Peat Soil","Yellow Soil"]

#Loading trained model
model = load_model(r"C:\Users\hp\Documents\SoilStation-Website\SoilTypeIdentify.h5")


#Function to predict the soil type
def predict(file):
    
	#Preprocessing the image
    image = load_img(file, target_size=(220, 220)) #Resizing
    image = img_to_array(image) #image to array
    image = np.reshape(image,[1,220,220,3]) #reshaping according to the reqiuired dimensions
    image = (image/255.) #Rescaling
    
	#predicting
    preds = model.predict(image) #return array with probabilities for each class
    predsLabel = np.argmax(preds) #return the class with highest probability
    
	#Converting probabilities in to percentages
    num0 = (preds[0][0])*100 #black percentage
    num1 = (preds[0][1])*100 #laterite percentage
    num2 = (preds[0][2])*100 #peat percentage
    num3 = (preds[0][3])*100 #yellow percentage
    
    #Rounding to two decimal places
    num0 = round(num0, 2)
    num1 = round(num1, 2)
    num2 = round(num2, 2)
    num3 = round(num3, 2)
    
    prediction = classes[predsLabel] #predicted class
    
	#Return predicted class and percentages as a tuple
    return prediction, num0, num1, num2, num3


#Setting starting app route
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("home.html")

#Setting home page app route
@app.route("/home.html", methods=['GET', 'POST'])
def toHome():
	return render_template("home.html")

#Setting reccomendation page app route
@app.route("/Recommendation.html", methods=['GET', 'POST'])
def recommend():
	return render_template("Recommendation.html")

#Setting prediction page app route
@app.route("/predict.html", methods=['GET', 'POST'])
def predicting():
	return render_template("predict.html")	

#Setting submit page app route
@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		#Request user uploaded image
		img = request.files["my_image"]

		#Set path to save image
		img_path1 = r"C:\Users\hp\Documents\SoilStation-Website\static\img"
		img_path2 = img.filename
		stat_dir = r"\static\img" #Flask static directory

		#Path to save image
		img_path = os.path.join(img_path1+"\\"+img_path2)	
		img.save(img_path)

		#Predicting the given image
		reuslts = predict(img_path)

		#New saved image in the static directory
		img_path = os.path.join(stat_dir+"\\"+img_path2)

		#Predicted results
		prediction = (reuslts[0]) # Predicted soil type
		blackPercentage = ("{:.2f}".format(reuslts[1])+" %") #Black percentage
		lateralPercentage = ("{:.2f}".format(reuslts[2])+" %") #Laterite percentage
		peatPercentage = ("{:.2f}".format(reuslts[3])+" %") #Peat percentage
		yellowPercentage = ("{:.2f}".format(reuslts[4])+" %") #Yellow percentage


	return render_template("predict.html", prediction = prediction, img_path = img_path, blackPercentage = blackPercentage,
			lateralPercentage = lateralPercentage, peatPercentage = peatPercentage, yellowPercentage = yellowPercentage)

#Setting AboutUs page app route
@app.route("/AboutUs.html", methods=['GET', 'POST'])
def about():
	return render_template("AboutUs.html")	

#Setting login page app route
@app.route("/login.html", methods=['GET', 'POST'])
def logIn():
	return render_template("login.html")

#Setting signup page app routw
@app.route("/signup.html", methods=['GET', 'POST'])
def signIn():
	return render_template("signup.html")

#Setting signup page app routw
@app.route("/contact.html", methods=['GET', 'POST'])
def contactUs():
	return render_template("contact.html")


#Running the app
if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)