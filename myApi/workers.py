from email import message
from flask import Flask
from flask_restful import Api, Resource, abort
import json

json_data = json.loads(open('workers.json', 'r').read())

app = Flask(__name__)
api = Api(app)

class WorkersAll(Resource):
    def get(self):
        return json_data["Workers"]
class WorkersRegular(Resource):
    def get(self, id):
        if len(json_data["Workers"]["Regulars"]) <= id:
            abort(404, message="Not found")
        return json_data["Workers"]["Regulars"][id]
class CEO(Resource):
    def get(self):
        return json_data["Workers"]["CEO"]
class Founder(Resource):
    def get(self):
        return json_data["Workers"]["Founder"]
class WorkersManagers(Resource):
    def get(self, id):
        if len(json_data["Workers"]["Managers"]) <= id:
            abort(404, message="Not found")
        return json_data["Workers"]["Managers"][id]   

api.add_resource(WorkersAll, "/workers")
api.add_resource(WorkersRegular, "/workers/regulars/<int:id>")
api.add_resource(WorkersManagers, "/workers/managers/<int:id>")
api.add_resource(CEO, "/workers/ceo")
api.add_resource(Founder, "/workers/founder")

if __name__ == "__main__":
    app.run(debug=True)