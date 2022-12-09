# ID2223 Lab2
## Feature pipline
The feature pipeline is edited and processed on Colab using GPU (we didn't split feature pipeline with training pipeline when we train the model in task 1), but we just pasted our codes in https://github.com/CleanRipple/ID2223/blob/main/lab2/feature_pipeline.ipynb. The language we chose is Chinese, and the data we used is from Common Voice dataset, subset “zh-CN”. The features we obtained is about 10 GB, which is stored in Hopsworks.
![hopsworks files](https://github.com/CleanRipple/ID2223/blob/main/lab2/pictures/hopsworks.png)

## Training pipline

## User Interface

## Improve model performance
### modal centric approach
- Increase "max_steps" or "learning_rate"

Since the wer result of each checkpoint keeps decreasing, we can see that our model is underfitting. Hence, increasing the "max_steps" or "learning_rate" in Seq2SeqTrainingArguments can improve the model.
![checkpoint results](https://github.com/CleanRipple/ID2223/blob/main/lab2/pictures/checkpoint.png)

- Change the model architecture

Constrained by the devices and the large dataset, we only use the model whisper-small for now. Perhaps applying a larger model with more layers like whisper-medium or whisper-large can give us a better result.

### data centric approach
