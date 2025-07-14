from flask import Flask, request, jsonify
import threading
import gradio as gr
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze():
    print("I am working!")  # Print to logs
    return jsonify({"status": "I am working!"})

# Run Flask in a separate thread so Gradio doesn't block
def run_flask():
    app.run(host="0.0.0.0", port=7860)

# Just a dummy Gradio UI so Spaces runs
def dummy_ui():
    return "Flask is running in background."

iface = gr.Interface(fn=dummy_ui, inputs=[], outputs="text")

if __name__ == '__main__':
    threading.Thread(target=run_flask).start()
    iface.launch()
