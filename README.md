# Django Deployment - Thyroid Disorder Prediction 

Thyroid disease is a common cause of medical diagnosis and prediction, with an onset that is difficult to forecast in medical research. The thyroid gland is one of our body's most vital organs. Thyroid hormone releases are responsible for metabolic regulation. Hyperthyroidism and hypothyroidism are one of the two common diseases of the thyroid that releases thyroid hormones in regulating the rate of body's metabolism. The main goal is to predict the estimated risk on a patient's chance of obtaining thyroid disease or not.

## Dataset 

Link: https://github.com/Oviyashri/Thyroid_disorder_prediction/tree/main/data_given

## Notebook

Link: https://github.com/Oviyashri/Thyroid_disorder_prediction/tree/main/notebooks

## Web Deployment

Thyroid disease detection Web App: https://thyroid-pred.herokuapp.com/ 

# Others

## Procfile 

web: gunicorn prediction.wsgi --log-file -
