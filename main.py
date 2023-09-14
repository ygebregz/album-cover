from src.image_processer import ImageProcesser
from src.song_processer import SongProcessor
from src.markov_chain import MarkovChain


# TODO: take terminal args and execute program

image_processor = ImageProcesser()
img, img_rgb = image_processor.get_image("assets/input_images/adele.jpeg")
song_processor = SongProcessor()
song, sample_rate = song_processor.load_song(
    "assets/input_songs/burna_last_last.mp3")
song_tempo = song_processor.get_song_tempo(song, sample_rate=sample_rate)
chain = MarkovChain(song_tempo)
chain.populate_transition_matrix(img_rgb)
new_song_cover = chain.generate_image_data(img.size)
final_song_cover = image_processor.gen_img_from_rgb(
    new_song_cover, "Love In The Dark", song_tempo, img.size)
final_song_cover.show()
