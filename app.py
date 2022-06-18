from flask import Flask, jsonify
from flask import request as rq

from model.Income import Income, IncomeSchema
from model.Expense import Expense, ExpenseSchema
from model.transaction_type import TransactionType

app = Flask(__name__)

transactions = [
    Income('Salary', 5000),
    Income('Dividends', 200),
    Expense('pizza', 50),
    Expense('Rock Concert', 100)
]


@app.route("/income")
def get_income():  # put application's code here
    schema = IncomeSchema(many=True)
    income = schema.dump(filter(lambda x: x.type == TransactionType.INCOME.name, transactions))
    return jsonify(income)


@app.route("/income", methods=["POST"])
def add_income():
    # check to make sure the incoming data matches a schema
    income = IncomeSchema().load(rq.get_json())
    transactions.append(income)
    return "", 204


@app.route("/expenses")
def get_expense():
    schema = ExpenseSchema(many=True)
    expenses = schema.dump(filter(lambda x: x.type == TransactionType.EXPENSE.name, transactions))
    return jsonify(expenses)


@app.route("/expense", methods=["POST"])
def add_expense():
    expense = ExpenseSchema().load(rq.get_json())
    transactions.append(expense)
    return "", 204


@app.route("/")
def get():
    return "Init success"


if __name__ == '__main__':
    app.run()
