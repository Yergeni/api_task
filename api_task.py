from flask import Flask, jsonify, request

app = Flask(__name__)

# dictionary 'cars' to simulate a database resource
cars = [
    {
        "id": 1,
        "model": "Honda Civic",
        "year": 2017,
        "price": "$30000"
    },
    {
        "id": 2,
        "model": "Mitsubishi Lancer",
        "year": 2006,
        "price": "$3500"
    },
    {
        "id": 3,
        "model": "Toyota Corolla",
        "year": 2018,
        "price": "$18000"
    }
]

class Car():

    # GET the whole list of cars
    @app.route('/cars/all')
    def get_cars():
        return jsonify(cars)

    # GET an specific car by ID
    @app.route('/cars', methods=['GET'])
    def get_car():
        # trying to verify if id was entered
        if 'id' in request.args:
            car_id = int(request.args.get('id'))
        
        for car in cars:
            if(car["id"] == car_id):
                return jsonify(car), 200
        return "car not found", 404
    
    # POST a new car using a json body
    @app.route('/cars', methods=['POST'])
    def add_car():
        # getting the body(json object) from the request 
        car_obj = request.get_json()
        car_id = car_obj["id"]
        for car in cars:
            if(car_id == car["id"]):
                return "car with id {} already exists".format(car_id), 400

        cars.append(request.get_json())
        return "", 201

    @app.route('/cars', methods=['PUT'])
    def update_car():
        car_obj = request.get_json()
        car_id = car_obj["id"]
        for car in cars:
            if(car_id == car["id"]):
                car["model"] = car_obj["model"]
                car["year"] = car_obj["year"]
                car["price"] = car_obj["price"]
                # If requested car exist; return the updated car with HTTP Response 200.
                return jsonify(car), 200
        
        # Otherwise, create the car and send a HTTP Response 201.
        cars.append(car_obj)
        return jsonify(car_obj), 201

    @app.route('/cars', methods=['DELETE'])
    def delete_car():
        # trying to verify if id was entered
        if 'id' in request.args:
            car_id = int(request.args.get('id'))

        for car in cars:
            if(car["id"] == car_id):
                cars.remove(car)
                return "Car with id: {} have been deleted.".format(car_id), 200
        return "car not found", 404
      
if __name__ == "__main__":  
    app.run(debug=True)