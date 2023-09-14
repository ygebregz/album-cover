"""
@author: Yonas Gebregziabher
Main file to execute program
"""
from src.image_processor import ImageProcessor
from src.song_processor import SongProcessor
from src.markov_chain import MarkovChain
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--Image", help="Base image", required=True)
    parser.add_argument("-s", "--Song", help="Song file", required=True)
    parser.add_argument("-t", "--Title", help="Song Title",
                        type=str, required=True)

    args = parser.parse_args()
    image = ImageProcessor(args.Image)
    song = SongProcessor(args.Song)
    song_tempo = song.get_song_tempo()
    chain = MarkovChain(song_tempo)
    chain.populate_transition_matrix(image.rgb_data)
    new_song_cover = chain.generate_image_data(image.image.size)
    final_song_cover = image.gen_img_from_rgb(
        new_song_cover, args.Title, song_tempo, image.image.size)
    final_song_cover.show()
