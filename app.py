from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def process_data():
    data = request.get_json().get('data', [])
    numbers = [x for x in data if x.isdigit()]
    alphabets = [x for x in data if x.isalpha()]
    highest_alphabet = max(alphabets, default='', key=str.casefold)

    response = {
        "is_success": True,
        "user_id": "your_name_ddmmyyyy",  # Replace with your actual details
        "email": "your_email@example.com",  # Replace with your actual email
        "roll_number": "your_roll_number",  # Replace with your actual roll number
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": [highest_alphabet] if highest_alphabet else []
    }
    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    response = {
        "operation_code": 1
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
