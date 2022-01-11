from gevent.pywsgi import WSGIServer


from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

from app import register_error_handlers
from app.error_handling import ObjectNotFound
from temperature.temperature import TemperatureFromFile

app = Flask(__name__)
CORS(app)
api = Api(app)


class TemperatureListResource(Resource):
    def get(self):
        temperatures = TemperatureFromFile("resources/weather.json")
        return temperatures.all()


class TemperatureResource(Resource):
    def get(self, day_id):
        temperatures = TemperatureFromFile("resources/weather.json")
        x = temperatures.get_day(day_id)
        if x is None:
            raise ObjectNotFound('the day does not exist')
        return x


api.add_resource(TemperatureListResource, '/api/v1/temperatures')
api.add_resource(TemperatureResource, '/api/v1/temperatures/<int:day_id>')

register_error_handlers(app)

if __name__ == "__main__":
    app.debug = True
    http_server = WSGIServer(('localhost', 5000), app)
    http_server.serve_forever()
