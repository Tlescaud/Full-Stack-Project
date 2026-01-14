from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    # Temporary hard-coded values for the chart
    total_income = 2000
    total_expenses = 750

    return render_template(
        "index.html",
        total_income=total_income,
        total_expenses=total_expenses
    )

@app.route("/add", methods=["POST"])
def add():
    description = request.form.get("description")
    amount = request.form.get("amount")
    entry_type = request.form.get("type")

    print("Received:", description, amount, entry_type)

    # After submitting, reload the main page
    total_income = 2000
    total_expenses = 750

    return render_template(
        "index.html",
        total_income=total_income,
        total_expenses=total_expenses
    )

if __name__ == "__main__":
    app.run(debug=True)




