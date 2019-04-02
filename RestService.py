from flask import Flask, jsonify, request;
import pickle


app = Flask(__name__)

@app.route("/", methods=['GET'])

def first():
    return jsonify({"Welcome": "Here"})


@app.route("/displayAll/", methods = ['GET'])

def displayAll():
    f1 = open("person.ser","rb")
    res = pickle.load(f1)
    f1.close()
    results =[]
    for i in res:
        results.append({"Name ": i.name,
                        "Age ": i.age,
                        "Salary ": i.salary,
                        "Designation ": i.designation})
    return jsonify({'Employee Details ':results})


if __name__=='__main__':
    app.run(debug=True)
