"""
@author Yonas Gebregziabher

Opens a song and provides functionality to get its
tempo.
"""
import librosa


class SongProcessor:

    def __init__(self, song_path: str) -> None:
        "Constructor to create SongProcessor object"
        self.song, self.sample_rate = librosa.load(song_path)

    def get_song_tempo(self) -> float:
        "Returns the song tempo's given a song and a sample rate"
        tempo, _ = librosa.beat.beat_track(y=self.song, sr=self.sample_rate)
        return tempo
