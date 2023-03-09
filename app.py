from flask import Flask, render_template, request
from keras.models import load_model
from keras.utils import load_img, img_to_array
import numpy as np
import os


app  = Flask('Soil_Identifier',template_folder=r'C:\Users\dell\Documents\SoilStation-Website\templates', static_folder =r'C:\Users\dell\Documents\SoilStation-Website\static')

classes = ["Black Soil","Laterite Soil","Peat Soil","Yellow Soil"]

model = load_model(r"C:\Users\dell\Documents\SoilStation-Website\SoilTypeIdentify.h5")

def predict(file):
    
    image = load_img(file, target_size=(220, 220))
    image = img_to_array(image)
    image = np.reshape(image,[1,220,220,3])
    image = (image/255.)
    
    preds = model.predict(image)
    predsLabel = np.argmax(preds)
    
    num0 = (preds[0][0])*100
    num1 = (preds[0][1])*100
    num2 = (preds[0][2])*100
    num3 = (preds[0][3])*100
    
    num0 = round(num0, 2)
    num1 = round(num1, 2)
    num2 = round(num2, 2)
    num3 = round(num3, 2)
    prediction = classes[predsLabel]
    return prediction, num0, num1, num2, num3


@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("predict.html")

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files["my_image"]

		img_path1 = r"C:\Users\dell\Documents\SoilStation-Website\static\img"
		img_path2 = img.filename
		stat_dir = r"\static\img"


		img_path = os.path.join(img_path1+"\\"+img_path2)	

		img.save(img_path)
		print(img_path)

		reuslts = predict(img_path)

		img_path = os.path.join(stat_dir+"\\"+img_path2)

		prediction = (reuslts[0])
		blackPercentage = ("{:.2f}".format(reuslts[1])+" %")
		lateralPercentage = ("{:.2f}".format(reuslts[2])+" %")
		peatPercentage = ("{:.2f}".format(reuslts[3])+" %")
		yellowPercentage = ("{:.2f}".format(reuslts[4])+" %")


	return render_template("predict.html", prediction = prediction, img_path = img_path, blackPercentage = blackPercentage,
			lateralPercentage = lateralPercentage, peatPercentage = peatPercentage, yellowPercentage = yellowPercentage)

if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)