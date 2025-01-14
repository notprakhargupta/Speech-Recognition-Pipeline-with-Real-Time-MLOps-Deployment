
import torch
import torchaudio

class SpeechRecognitionModel(torch.nn.Module):
    def __init__(self):
        super(SpeechRecognitionModel, self).__init__()
        self.wav2vec = torchaudio.models.Wav2Vec2Model.from_pretrained("facebook/wav2vec2-large-960h")
    
    def forward(self, waveform):
        return self.wav2vec(waveform)

# Function to transcribe audio
def transcribe_audio(audio_path):
    model = SpeechRecognitionModel()
    model.eval()
    waveform, sample_rate = torchaudio.load(audio_path)
    with torch.no_grad():
        transcription = model(waveform)
    return transcription
