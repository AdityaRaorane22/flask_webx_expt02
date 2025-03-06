from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

projects = [
    {
        "title": "Hire360.ai",
        "description": "AI-powered interview analysis tool with real-time emotion detection, speech confidence assessment, and automated insights.",
        "link": "#"
    },
    {
        "title": "VahanSaathi",
        "description": "A modular Flutter app for vehicle tracking & management, featuring a queue system, secure authentication, and an intuitive UI.",
        "link": "#"
    },
    {
        "title": "Air Quality Monitoring App",
        "description": "A mobile app that provides real-time air quality data using the Atmos Urban Sciences API with interactive maps and insights.",
        "link": "#"
    }
]


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html", projects=projects)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        return redirect(url_for('success', name=name, email=email, subject=subject, message=message))
    return render_template("contact.html")

@app.route('/success')
def success():
    return render_template("success.html", name=request.args.get('name'), email=request.args.get('email'), subject=request.args.get('subject'), message=request.args.get('message'))

if __name__ == '__main__':
    app.run(debug=True)