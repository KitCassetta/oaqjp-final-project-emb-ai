import requests
import json

def emotion_detector(text_to_analyse):
    # Define the URL for the emotion analysis API
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Parse the response from the API
    formatted_response = json.loads(response.text)["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(formatted_response, key=formatted_response.get)
    dominant_value = formatted_response[dominant_emotion]
    formatted_response["dominant_emotion"] =  dominant_emotion

    return formatted_response