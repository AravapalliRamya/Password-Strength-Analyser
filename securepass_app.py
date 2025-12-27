from flask import Flask, render_template, request, jsonify
import re
import math

app = Flask(__name__)

def calculate_entropy(password):
    charset = 0
    if re.search(r"[a-z]", password): charset += 26
    if re.search(r"[A-Z]", password): charset += 26
    if re.search(r"[0-9]", password): charset += 10
    if re.search(r"[^a-zA-Z0-9]", password): charset += 32

    if charset == 0:
        return 0

    return round(len(password) * math.log2(charset), 2)

def estimate_crack_time(entropy):
    guesses_per_second = 1e9
    seconds = (2 ** entropy) / guesses_per_second

    if seconds < 60: return "Seconds"
    if seconds < 3600: return "Minutes"
    if seconds < 86400: return "Hours"
    if seconds < 31536000: return "Days"
    if seconds < 31536000 * 100: return "Years"
    return "Centuries"

def analyze_password(password):
    score = 0
    score += 20 if len(password) >= 8 else 0
    score += 20 if re.search(r"[A-Z]", password) else 0
    score += 20 if re.search(r"[a-z]", password) else 0
    score += 20 if re.search(r"[0-9]", password) else 0
    score += 20 if re.search(r"[^a-zA-Z0-9]", password) else 0

    strength = "Weak" if score < 40 else "Medium" if score < 70 else "Strong"
    entropy = calculate_entropy(password)
    crack_time = estimate_crack_time(entropy)

    return strength, score, entropy, crack_time

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    password = request.json.get("password", "")
    strength, score, entropy, crack_time = analyze_password(password)

    return jsonify({
        "strength": strength,
        "percentage": score,
        "entropy": entropy,
        "crack_time": crack_time
    })

if __name__ == "__main__":
    app.run(debug=True)
