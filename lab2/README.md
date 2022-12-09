# ID2223 Lab2
## Feature pipline
The feature pipeline is edited and processed on Colab using GPU (we didn't split feature pipeline with training pipeline when we train the model in task 1), but we just pasted our codes in [feature_pipeline.ipnb](https://github.com/CleanRipple/ID2223/blob/main/lab2/feature_pipeline.ipynb). The language we chose is Chinese, and the data we used is from Common Voice dataset, subset “zh-CN”. The features we obtained is about 10 GB, which is stored in Hopsworks.
![hopsworks files](https://github.com/CleanRipple/ID2223/blob/main/lab2/pictures/hopsworks.png)

## Training pipline
When doing training pipeline, we also used GPU on Colab. The pre-trained model “whisper-small” is loaded and word error rate (WER) is used to evaluate the performance. The code is in [training_pipeline.ipnb](https://github.com/CleanRipple/ID2223/blob/main/lab2/training_pipeline.ipynb). We set the max step as 4000, and a checkpoint every 1000 steps. After 11 hours training, we finally reached a WER of 69.69%. The trained model is uploaded on Hugging Face.
![checkpoint results](https://github.com/CleanRipple/ID2223/blob/main/lab2/pictures/checkpoint.png)

## User Interface
We created a user interface on Hugging Face. The codes are available in app.py. The interface is shown as below:

Users are able to enter a YouTube link or speak to the microphone. Then click the button “submit”, and the audio will be transformed into simplified Chinese and shown in “output” bar on the right.

To try the YouTube link insertion, you can use this link https://www.youtube.com/watch?v=neIHIdko0E0
![translate](https://github.com/CleanRipple/ID2223/blob/main/lab2/pictures/translate.png)

## Improve model performance
### modal centric approach
- Increase "max_steps" or "learning_rate"

Since the wer result of each checkpoint keeps decreasing, we can see that our model is underfitting. Hence, increasing the "max_steps" or "learning_rate" in Seq2SeqTrainingArguments can improve the model.
![wer](https://github.com/CleanRipple/ID2223/blob/main/lab2/pictures/wer_pic.png)

- Change the model architecture

Constrained by the devices and the large dataset, we only use the model whisper-small for now. Perhaps applying a larger model with more layers like whisper-medium or whisper-large can give us a better result.

### data centric approach
