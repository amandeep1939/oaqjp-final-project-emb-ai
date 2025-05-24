from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def emotionDetector():
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return jsonify({'error': 'Missing textToAnalyze parameter'}), 400

    try:
        result = emotion_detector(text_to_analyze)

        response_text = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']}, "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )
        return response_text, 200, {'Content-Type': 'text/plain'}
    except Exception as e:
        return jsonify({'error': str(e)}), 500

        
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)