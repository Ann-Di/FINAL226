from flask import Flask, request, redirect, render_template
import sqlite3

app = Flask(__name__)

# === Initialize database ===
def init_db():
    conn = sqlite3.connect('zodiac.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS zodiac_quiz_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            q1_day_or_night TEXT CHECK(q1_day_or_night IN ('day', 'night')),
            q2_element TEXT CHECK(q2_element IN ('fire', 'earth', 'water', 'air')),
            q3_friend_description TEXT CHECK(q3_friend_description IN ('leader', 'kind', 'smart', 'chill')),
            q4_favorite_season TEXT CHECK(q4_favorite_season IN ('spring', 'summer', 'autumn', 'winter')),
            q5_favorite_activity TEXT CHECK(q5_favorite_activity IN ('reading', 'sports', 'music', 'traveling')),
            result TEXT,
            submitted_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# === Zodiac logic (can be improved later) ===
def determine_zodiac_result(q2, q3):
    if q2 == "fire" and q3 == "leader":
        return "Aries"
    elif q2 == "fire" and q3 == "chill":
        return "Leo"
    elif q2 == "fire":
        return "Sagittarius"
    elif q2 == "earth" and q3 == "hardworking":
        return "Capricorn"
    elif q2 == "earth" and q3 == "kind":
        return "Taurus"
    elif q2 == "earth":
        return "Virgo"
    elif q2 == "air" and q3 == "smart":
        return "Aquarius"
    elif q2 == "air" and q3 == "leader":
        return "Gemini"
    elif q2 == "air":
        return "Libra"
    elif q2 == "water" and q3 == "kind":
        return "Cancer"
    elif q2 == "water" and q3 == "leader":
        return "Scorpio"
    elif q2 == "water":
        return "Pisces"
    return "Unknown"

# === Quiz form ===
@app.route("/")
def quiz():
    return render_template("zodiac_quiz.html")

# === Submission handling ===
@app.route("/submit", methods=["POST"])
def submit():
    q1 = request.form.get("q1")
    q2 = request.form.get("q2")
    q3 = request.form.get("q3")
    q4 = request.form.get("q4")
    q5 = request.form.get("q5")

    result = determine_zodiac_result(q2, q3)

    conn = sqlite3.connect('zodiac.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO zodiac_quiz_results (
            q1_day_or_night,
            q2_element,
            q3_friend_description,
            q4_favorite_season,
            q5_favorite_activity,
            result
        ) VALUES (?, ?, ?, ?, ?, ?)
    ''', (q1, q2, q3, q4, q5, result))
    conn.commit()
    conn.close()

    return redirect(f"/{result.lower()}")

# === Result pages ===
@app.route("/aries")
def aries(): return render_template("ariesResult.html")

@app.route("/taurus")
def taurus(): return render_template("taurusResult.html")

@app.route("/gemini")
def gemini(): return render_template("geminiResult.html")

@app.route("/cancer")
def cancer(): return render_template("cancerResult.html")

@app.route("/leo")
def leo(): return render_template("leoResult.html")

@app.route("/virgo")
def virgo(): return render_template("virgoResult.html")

@app.route("/libra")
def libra(): return render_template("libraResult.html")

@app.route("/scorpio")
def scorpio(): return render_template("scorpioResult.html")

@app.route("/sagittarius")
def sagittarius(): return render_template("sagittariusResult.html")

@app.route("/capricorn")
def capricorn(): return render_template("capricornResult.html")

@app.route("/aquarius")
def aquarius(): return render_template("aquariusResult.html")

@app.route("/pisces")
def pisces(): return render_template("piscesResult.html")

if __name__ == "__main__":
    app.run(debug=True)

