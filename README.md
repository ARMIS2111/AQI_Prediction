# AQI_Prediction
This is a Regression model that can be used to predict the AQI of a county in a state in the USA.

# Web Scraping:-
This project has used data from <a href="https://aqs.epa.gov/aqsweb/airdata/download_files.html#Meta"> United States Environmental Protection Agency's website </a>
The data in the table named Annual Summary Data's - AQI by County column has been used. The web scraping script uses beautiful Soup 4 to select the last child of every row. After getting all the files, they are extracted and all the zips are deleted. After this, all the CSV files extracted from the zip files are merged and all the individual files are deleted. The merged file is the final dataset and can be found in the dataset folder of this repository.<br/>

# Exploratory Data Analysis (EDA):-
EDA has been performed on this dataset to gather some insights regarding the dataset itself. One interesting trend that was found is The average AQI has been decreasing i.e. Air quality has been getting better since the 1980s.<br/>

# Machine Learning model
After label encoding the categorical values and scaling the dataset using standard scaler, the dataset has been split into training and testing dataset with 70:30 split.<br/>
Three machine learning models have been created: One using XGBoost and the other two using different models of Artificial Neural Networks.<br/>
All the models have minimal Mean Absolute Error(MAE) of less than 3 on the testing dataset.<br/>
However the ANN model with 64 nodes in hidden layer 1, 64 nodes in hidden layer 2, and 1 node in the output layer produced the minimal MASE of 2.007 and so it is used in the deployment. <br/>

# The EDA and ML model's code can be found in the file named Notebook.ipynb <br/>

# Deployment
The model has been deployed using a Flask app. Whenever the user presses submit button on the Web page, the route /submit is hit. It takes the input from the request object and predicts the AQI for the corresponding input.<br/>
As the response object, it sends the output data(the predicted AQI) and the historic data (Data for that county and State as available in the dataset) so that a graph can be plotted. <br/>
The output is pushed into the html page and a graph is created using javascript that is displayed below the prediction.



# How to run the app
Simply download the repository and run the app.py file. <br/>
Hit the link displayed in the terminal.<br/>
Input data in the form.<br/>
Press Submit.<br/>
See the power of Machine Learning.
