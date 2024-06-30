''' 
Emotion Detector Server
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector



app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_detector():
    '''
    Grab text and pass to sentiment_analyzer
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    result = emotion_detector(text_to_analyze)
    f_text = f"For the given statement, the system response is 'anger': {result['anger']}," 
    f_text += f" 'disgust': {result['disgust']}, 'fear': {result['fear']}, "
    f_text += f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
    f_text += f"The dominant emotion is {result['dominant_emotion']}." 

    return f_text

@app.route("/")
def render_index_page():
    '''
    Return index page
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
