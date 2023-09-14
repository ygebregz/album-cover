"""
Song processer 
"""
import librosa


class SongProcessor:

    def __init__(self) -> None:
        pass

    def load_song(self, song_path: str):
        return librosa.load(song_path)

    def get_song_tempo(self, song, sample_rate):
        tempo, _ = librosa.beat.beat_track(y=song, sr=sample_rate)
        return tempo

    def generate_order(self, tempo: int):
        min_tempo, max_tempo = 80, 160
        adjusted_order = 50 - int((tempo - min_tempo) /
                                  (max_tempo - min_tempo) * 50)
        adjusted_order = max(0, min(adjusted_order, 50))
        return adjusted_order

    def generate_noise(self, song):
        pass

    def generate_title(self):
        pass
