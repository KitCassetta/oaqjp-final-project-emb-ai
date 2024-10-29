"""Flask and IBM emotion detector project"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def get_analysis():
    """send a request for analysis"""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid Text! Please try again!"

    return f"""For the given statement, the system response is 'anger': {response["anger"]},
     'disgust': {response["disgust"]}, 'fear': {response["fear"]}, 'joy': {response["joy"]}
      and 'sadness': {response["sadness"]}. 
      The dominant emotion is <b>{response["dominant_emotion"]}</b>"""

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
