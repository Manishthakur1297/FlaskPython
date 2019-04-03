from flask import Flask, jsonify, request;
import pickle;


app = Flask(__name__)

@app.route("/", methods=['GET'])

def first():
    return jsonify({"Welcome": "Here"})

@app.route("/displayAll/", methods = ['GET'])

def displayAll():
    f1 = open("person.ser","rb")
    try:
        res = pickle.load(f1)
        f1.close()
        results =[]
        for i in res:
            results.append({"id " : i.id, "Name ": i.name,
                            "Age ": i.age,
                            "Salary ": i.salary,
                            "Designation ": i.designation})
        return jsonify(results)
    except (EOFError, Exception):
            f1.close()
            return jsonify({'No Employee Record ':"Found!!!!"})
    

@app.route("/displayById/<int:num>", methods = ['GET'])

def displayById(num):
    f1 = open("person.ser","rb")
    try:
        res = pickle.load(f1)
        for i in res:
            if(int(i.id)==num):
                return jsonify({"id " : i.id, "Name ": i.name,
                            "Age ": i.age,
                            "Salary ": i.salary,
                            "Designation ": i.designation})
        return jsonify({"Record with ID [ "+str(num)+" ] " : " do not exists....." })
    except (EOFError, Exception):
            f1.close()
            return jsonify({'No Employee Record ':"Found!!!!"})


if __name__=='__main__':
    app.run(debug=True)
