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

    def generate_order(self, song):
        pass

    def generate_noise(self, song):
        pass
