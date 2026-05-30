from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input from form
        budget_value = request.form.get('budget')

        # Validation
        if budget_value == "" or budget_value is None:
            return render_template('index.html', prediction_text="⚠️ Please enter budget")

        # Convert to float
        budget = float(budget_value)

        # Dummy prediction logic (you can replace with ML model later)
        if budget > 100:
            result = "🎬 Hit Movie"
        else:
            result = "❌ Flop Movie"

        return render_template('index.html', prediction_text=f"Prediction: {result}")

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")


if __name__ == "__main__":
    app.run(debug=True)