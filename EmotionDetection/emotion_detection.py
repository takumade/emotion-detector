'''
Emotion Detection
'''

import json
import requests

def emotion_detector(text_to_analyze):
    '''
    Perfom a emotion detection on text 
    '''

    url =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    myobj = {"raw_document": {
        "text": text_to_analyze
    }}

    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(
        url,
        json=myobj,
        headers=header
    )

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }



    emotions = json.loads(response.text)['emotionPredictions'][0]['emotion']
    dominant_emotion = "anger"

    for emotion in emotions.keys():
        if emotions[emotion] > emotions[dominant_emotion]:
            dominant_emotion = emotion

    

    emotions['dominant_emotion'] = dominant_emotion

    return emotions
