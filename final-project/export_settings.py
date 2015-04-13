from moviepy.editor import *

class Export():
    """ This class allows users re-encode videos for web delivery """

    VALID_CODECS = ['libx264', 'mpeg4', 'libvorbis', 'libvpx', 'rawvideo', 'png']

    def __init__(self, filename, fps, codec, bitrate):
        if codec == 'libx264' or 'mpeg4':
            self.filename = filename + '.mp4'
        elif codec == 'libvorbis':
            self.filename = filename + '.ogv'
        elif codec == 'libvpx':
            self.filename = filename + '.webm'
        else:
            self.filename = filename + '.avi'

        self.fps = fps

        if codec in VALID_CODECS:
            self.codec = codec

        self.bitrate = bitrate + 'k'
