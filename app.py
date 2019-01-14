from flask import Flask, jsonify, render_template
from flask import send_file
from flask import request, url_for, redirect
import pygame
import time
app = Flask(__name__)


def play_music(music_file):
    clock = pygame.time.Clock()
    try:
        pygame.mixer.music.load(music_file)
    except pygame.error:
        print(music_file)
        return
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(5)
        pygame.mixer.music.fadeout(1000)
        pygame.mixer.music.stop()

def _init_midi(midi_file):
    freq = 44100  # audio CD quality
    bitsize = -16  # unsigned 16 bit
    channels = 2  # 1 is mono, 2 is stereo
    buffer = 1024  # number of samples
    pygame.mixer.init(freq, bitsize, channels, buffer)

    # optional volume 0 to 1.0

    pygame.mixer.music.set_volume(0.8)

    if not midi_file:
        pygame.mixer.quit()
        return

    try:
        play_music(midi_file)
    except KeyboardInterrupt:
        pygame.mixer.music.fadeout(1000)
        pygame.mixer.music.stop()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ukranian')
def ukranian():
    _init_midi('./Ukrainian.mid')
    return redirect(url_for('index'))

@app.route('/country')
def country():
    _init_midi('./Country.mid')
    return redirect(url_for('index'))

@app.route('/bollywood')
def bollywood():
    _init_midi('./Bollywood.mid')
    return redirect(url_for('index'))

@app.route('/rap')
def rap():
    _init_midi('./Rap.mid')
    return redirect(url_for('index'))

@app.route('/blues')
def blues():
    _init_midi('./Blues.mid')
    return redirect(url_for('index'))

@app.route('/jazz')
def jazz():
    _init_midi('./Jazz.mid')
    return redirect(url_for('index'))



