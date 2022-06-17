from flask import Flask, jsonify, request

app = Flask(__name__)

# app route defines the url place
# the return of the first page determines what is displayed.
# the return is a generic HTML thing.

incomes = [
    {'description': 'salary', 'amount': 5000}
]


@app.route('/incomes')
def get_incomes():  # put application's code here
    return jsonify(incomes)


@app.route('/incomes', methods=['POST'])
def add_income():
    incomes.append(request.get_json())
    return '', 204


def nonConflict():
    return "wildcard"


if __name__ == '__main__':
    app.run()
