from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# This will store the responses from your Dockerized Flask API
data_store = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-file', methods=['POST'])
def send_file():
    audio_file = request.files['audio_file']
    
    # Ensure there's a file
    if audio_file:
        # API endpoint of the Dockerized Flask app
        api_url = 'http://localhost:8086/api/file_tempo'

        # Send the file to the Dockerized Flask API
        response = requests.post(api_url, files={'my_audio_file': audio_file})
        
        if response.status_code == 200:
            # Store the response
            data_store.append(response.json())

    return render_template('index.html', data=data_store)

if __name__ == '__main__':
    app.run(debug=True)
