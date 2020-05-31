from flask import Flask,render_template,url_for, request, redirect
import csv
app = Flask(__name__)

print('Server starting-----------\n')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def My_home(page_name):
    return render_template(page_name)


#@app.route('/about.html')
#def about():
 #   return render_template('about.html')

def write_to_csv(data):
    with open('database.csv', 'a') as database:
        email = data["email"]
        message = data["message"]
        subject = data["subject"]

        csv_writer = csv.writer(database, delimiter=',')
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        #print(data)

        #with open('database.txt', 'a') as f:
         #   f.write(f'\n{data["email"]}, {data["subject"]}, {data["message"]}')

        return redirect('/thankyou.html')
    else:
        return 'Something Went Wrong'



