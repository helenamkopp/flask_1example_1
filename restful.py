from flask import Flask, jsonify, request

app = Flask(__name__)


languages = [{"name" : "JavaScript"}, {"name" : "Python"}, {"name" : "Ruby"}]


@app.route("/", methods=["GET"])
def test():
    return jsonify({"message": "It works !"})


@app.route("/lang", methods=["GET"])
def returnAll():
    return jsonify({"languages": languages})


@app.route("/lang/<string:name>", methods=["GET"])
def returnOne(name):
    print(languages)
    langs = [language for language in languages if language["name"] == name]
    return jsonify({"language": langs[0]})


@app.route("/lang", methods=["POST"])
def addOne():
    language = {"name" : request.json["name"]}

    languages.append(language)
    return jsonify({"languages" : languages})




if __name__ == "__main__":
    app.run(debug=True, port=8080)
