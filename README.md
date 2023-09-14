# Song Cover Art Generator

Generate song covers based on the tempo of a song!

<img width="1394" alt="Input to output comparison" src="https://github.com/ygebregz/album-cover/assets/86376122/05cfc351-41f5-48a3-b8a1-f514909fcee4">

![image](https://github.com/ygebregz/album-cover/assets/86376122/fd086840-e4b2-495f-9fdf-6b713c90d098)

The unedited base photographs are the input photographs and the altered photographs on the polaroid frames on the right are some examples of the system output.

## How the Program Works

Throughout the source code, I've added documentation that explains what each class and function is responsible for. However, I want to talk a bit more about how the whole system works as well as the reasons for the technical decisions I've made.

### Getting Song Data

I used `librosa`, a python library, to load the song files and determine the song's tempo. This information is then fed into the next system.

### Image Processing

I used `Pillow`, a python library, to load, manipulate, and create images. I found the library to be the easiest to use and it provided all the functionalities I needed. After loading the image from the file path provided, I parse the image to get the RGB data associated with it.

### Markov Chain

After getting the RGB data associated with an image, the `MarkovChain` class is responsible for populating a transition matrix.

1. Using the song's tempo, calculate the noise(0 - 1) that we apply to the pixels. I then iterate through the pixels and randomly add 1 to the channels. It wraps around to ensure that we don't exceed the 255 max value.
2. Go through the transition matrix and the generated keys based on the order to increment their count, corresponding to the current RGB value transitioning into the next RGB value.
3. We then normalize each row in the transition matrix.
4. Finally, we iteratively call the `get_next_state()` function through `generate_image_data()` the image's width \* height times function to generate a pixel. The `get_next_state()` function uses the `numpy` library to randomly select a state based on a distribution of probabilities.

### Final Image Generation

Now that `generate_image_data()` generated the RGB data of the altered image, we do some post processing work. Using the functionalities provided in the `ImageProcessor` class, we convert the RGB data into an actual image file. However, before that, we adjust the pixels one more time. Based on the tempo of the song, `calculate_brightness_factor()` calculates a brightness factor to multiply the pixels by in `adjust_pixel_rgb()`. Finally, `gen_img_from_rgb()`, positions it directly on top of the polaroid frame. Look at `assets/layer_photo.png` to see the empty frame. The song's title is also added at the bottom of the frame.

## Running the programming

### Installing Dependencies

After cloning the project, simply navigate to the folder to first install the dependencies. They're all listed in the `requirements.txt` file. Simply run `pip install -r requirements.txt` to install all required modules.

### Executing Program

You can run the program by running

```
python3 main.py -i <image_path> -s <song_path> -t <song_title>
```

For example,

```
python3 main.py -i images/j_hus.jpeg -s drake_rescue_me.mp3 -t "Common Person"
```

## Personal Significance

This project is personally meaningful to me because I want to look into building a collection of music that I make either by myself or with friends. Currently, all of the songs have the default grey picture that IOS generates with audio files. However, when I play the songs, I don't want to have it feel like I'm listening to a voice note. Additionally, I also don't have the visual art skills or interest to make song covers for every random song I make. Therefore, this program is significant to me. Based on the type of songs that I make, the cover art will be manipulated accordingly so that the song cover sort of feels like the song, which is super important to me. The slower the tempo, the less bright but more distorted it becomes, which creates an abstract representation of a slow song. However, when the tempo is higher, pixels get brighter and there tends to be less randomness and noise in the picture.

## Personal Challenge

This project has been challenging in many ways. This is the first time where I've worked with images therefore I learned about how images are represented and how to manipulate them. I learned about the `Pillow` and `librosa` libraries as well, which were both new to me. I also challenged myself to further understand how markov chains work programmatically and doing so has solidified the topic for me. This was an important challenge for me because I wanted to work with images. I've found the text to image diffusion model based approaches interesting and I wanted to see how else a probabilistic model can be used to generate images on a simpler scale. Next steps for me going forward is to generate song title automatically based on the lyrics of the song, use more information from the song outside of the tempo to manipulate the image, and have more templates beyond the polaroid frame for different genres. It would also be nice to maybe add a web app component to this.

## Is this system creative?

I think so, at least to an extent. I think it is creative because it tries to visualize what the song feels like on the provided canvas. In _How to Build a CC System_ a computationally creative system has three characteristics: novelty, value, and intentionality. While my program lacks novelty since it doesn't generate new and original image, it certainly has value to me and is intentional about how it generates its output.

## Sources

The work for this program is inspired by the following sources.

- [Can we generate images with Markov Chains ?](https://medium.com/@abdellahsabiri/can-we-generate-images-with-markov-chains-84c3dea5cdd7)
- [Markov Chain Image Generation](https://jonnoftw.github.io/2017/01/18/markov-chain-image-generation)
- [Using Machine Learning to Make Art](https://magenta.as/using-machine-learning-to-make-art-84df7d3bb911)
- [Pillow documentation](https://pillow.readthedocs.io/en/stable/)
