from system.core.controller import *

class Directions(Controller):
    def __init__(self, action):
        super(Directions, self).__init__(action)

    def index(self):
        return self.load_view('directions.html')

    def get_directions(self):
        coordinates = {
            'origin': request.form['origin'],
            'destination': request.form['destination']
        }
        url = "https://maps.googleapis.com/maps/api/directions/json?{}&key=AIzaSyC6DTLmwYaTG6KRcVxY4gt56ZeVwRrNN-4".format(urlencode(coordinates))
        resp = requests.get(url).json()
        return self.make_directions(resp)

    def make_directions(self, r):
        if r['status'] == 'OK':
            goog = {
                'from': r['routes'][0]['legs'][0]['start_address'],
                'to': r['routes'][0]['legs'][0]['end_address'],
                'dist': r['routes'][0]['legs'][0]['distance']['text'],
                'time': r['routes'][0]['legs'][0]['duration']['text'],
                'steps': r['routes'][0]['legs'][0]['steps']
            }
        else:
            goog = {
                'msg': "Driving directions from {} to {} are not available".format(request.form['origin'].upper(), request.form['destination'].upper())
            }

        return self.load_view('dir.html', goog = goog)
