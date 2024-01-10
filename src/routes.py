from flask_restful import Resource

from src import api


class FilmListApi(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

    def patch(self):
        pass


api.add_resource(FilmListApi, '/films', strict_slashes=False)
