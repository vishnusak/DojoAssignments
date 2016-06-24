from system.core.controller import *

class Tunes(Controller):
    def __init__(self, action):
        super(Tunes, self).__init__(action)

    def index(self):
        return self.load_view('itunes.html', video_url = '')

    def get_video(self, artist):
        req_url = "https://itunes.apple.com/search?term="
        req_url += artist
        req_url += "&entity=musicVideo"

        resp = requests.get(req_url).content
        return resp
