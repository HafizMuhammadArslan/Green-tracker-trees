from flask import Flask, request, render_template

app = Flask(__name__, template_folder='../templates')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('tree_name')
        location = request.form.get('location')
        date = request.form.get('date_planted')
        status = request.form.get('status')

        print("✅ Received:", name, location, date, status)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
