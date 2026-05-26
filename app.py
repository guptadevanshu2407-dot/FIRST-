from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)


# ==============================
# HOME PAGE
# ==============================

@app.route("/")
def home():
    return render_template("index.html")


# ==============================
# ADD EXPENSE
# ==============================

@app.route("/add", methods=["POST"])
def add_expense():

    data = request.get_json()

    category = data["category"]
    amount = data["amount"]
    description = data["description"]

    with open("expenses.txt", "a") as file:

        file.write(
            f"{category},{amount},{description}\n"
        )

    return jsonify({
        "message": "Expense Added Successfully"
    })


# ==============================
# VIEW EXPENSES
# ==============================

@app.route("/view")
def view_expenses():

    expenses = []

    if os.path.exists("expenses.txt"):

        with open("expenses.txt", "r") as file:

            for line in file:

                category, amount, description = \
                    line.strip().split(",")

                expenses.append({
                    "category": category,
                    "amount": amount,
                    "description": description
                })

    return jsonify(expenses)


# ==============================
# DELETE ALL EXPENSES
# ==============================

@app.route("/delete", methods=["POST"])
def delete_expenses():

    open("expenses.txt", "w").close()

    return jsonify({
        "message": "All Expenses Deleted"
    })


# ==============================
# RUN APPLICATION
# ==============================

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
    
