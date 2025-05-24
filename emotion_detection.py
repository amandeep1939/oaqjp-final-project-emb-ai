from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Function to call Watson Emotion Detection API
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    return response.json().get("text")  # return the 'text' attribute from response

# Flask route to handle emotion detection
@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Missing "text" in request'}), 400

    text_to_analyze = data['text']
    try:
        result = emotion_detector(text_to_analyze)
        return jsonify({'emotion_result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)