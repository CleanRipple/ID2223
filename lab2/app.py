from transformers import pipeline
import gradio as gr
import pytube

pipe = pipeline(model="kk90ujhun/whisper-small-zh") 


def transcribe(my_url,audio):
  if my_url:
    my_audio = pytube.YouTube(my_url).streams.filter(subtype='mp4').first().download()
    text = pipe(my_audio)["text"]
    return text
  else:
    text = pipe(audio)["text"]
    return text

iface = gr.Interface(
    fn=transcribe, 
    inputs=[
        gr.Textbox(label="Enter your YouTube URL:"),
        gr.Audio(label="Speak to your microphone",source="microphone", type="filepath"),
        ], #
    outputs="text",
    title="Whisper Small Chinese",
    description="Realtime demo for Chinese speech recognition using a fine-tuned Whisper small model.",
)


iface.launch()