
import json
from speech_recognition import transcribe_audio

def lambda_handler(event, context):
    audio_path = event['audio_path']
    transcription = transcribe_audio(audio_path)
    return {
        'statusCode': 200,
        'body': json.dumps({'transcription': transcription})
    }
