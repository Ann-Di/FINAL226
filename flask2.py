from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('zodiac_quiz.html')  # Make sure index.html is in the templates folder

@app.route('/submit', methods=['POST'])
def submit():
    # Get the form data
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')
    q4 = request.form.get('q4')
    q5 = request.form.get('q5')

    # Optional: process or print the responses
    print("User answers:")
    print(f"Q1: {q1}")
    print(f"Q2: {q2}")
    print(f"Q3: {q3}")
    print(f"Q4: {q4}")
    print(f"Q5: {q5}")
    
    #save the result to the database
    answers = f"<h1>Thanks for your submission!</h1><p>Your choices: {q1}, {q2}, {q3}, {q4}, {q5}</p>"

    

    # Render a response page (or redirect)
    return answers

if __name__ == '__main__':
    app.run(debug=True)
