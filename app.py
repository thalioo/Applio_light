import gradio as gr

def process_audio(audio):
    # audio is a tuple: (sample_rate, data)
    return audio  # You can process the audio here if needed

with gr.Blocks() as demo:
    with gr.Row():
        audio_input = gr.Audio(sources="microphone", type="numpy", label="Record Audio")
        audio_output = gr.Audio(label="Playback")

    audio_input.change(fn=process_audio, inputs=audio_input, outputs=audio_output)

demo.launch()
