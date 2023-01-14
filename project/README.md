# ID2223 project
## Predect Air Quality Index of Oslo
### Introduction
In this project, we used air quanlity and weather in the past of Oslo to train our model to predict the AQI( Air Quality Index). The data used in air quality are the indexex of PM2.5, PM10 and NO2, and AQI is the maximum of PM2.5, PM10 and NO2. The porject is able to predict AQI for the next seven days in Oslo.
### Data Source
Air quality:https://aqicn.org/city/norway/norway/oslo/hjortnes/
Weather condition:https://weather.visualcrossing.com/
### Project Architecture
The project is divided into 6 parts:
1.Request API-key and download data from data source. The API key is stored in .env file. The data downloaded is stored in .csv files.
2.Use Backfill_feature_groups.py to drop the data we don't need and creat feature group in Hopsworks.
3.Usese Feature_pipeline.py to create feature pipeline to creat a feature pipeline and insert new data everyday.
4.Use Feature_views_and_training_dataset.py to creat feature views and training dataset.
5.Use Model_training.py to train the model.
6.Use streamlit_app.py to deploy streamlit app. Use app.py to create user Interface on Huggingface.
### User Interface 
Huggingface URL:https://huggingface.co/spaces/kk90ujhun/air_quality

Click "submit" and you can see the prediction of AQI for next 7 days.
![image](https://user-images.githubusercontent.com/117844256/212493882-4d66565c-b106-4fff-a4c4-0c394b487968.png)


We also deployed a streamlit app, but there's something wrong with the huggingface so it can't be displayed on huggingface. You can see the prediction of AQI for next 7 days on the left.
<img width="960" alt="a526d2ec889ac33d3d4e6e875ad8ead" src="https://user-images.githubusercontent.com/117844256/212493729-63704c62-0814-4bb5-9507-9a5e61efcf09.png">
