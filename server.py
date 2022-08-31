from flask import Flask, render_template,url_for,redirect,request
import csv
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit_form', methods = ['GET','POST'] )
def submit():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_data_csv(data)
            message = 'Sua mensagem foi enviada, logo retornarei!!'
            return render_template('thankyou.html',message=message)
        except:
            message = "Nao salvou."
            return render_template('thankyou.html',message=message)
    else:
        message = "Mensagem não enviada, tente outro meio de contato"
        return render_template('thankyou.html',message=message)


@app.route('/<string:page_name>')
def page(page_name='/'):
    try:
        return render_template(page_name)
    except:
        return redirect('/')



def write_data_csv(data):
    email = data['email']
    subject = data['subject']
    message = data["message"]
    with open('db.csv', 'a', newline='') as csvfile:
        db_writer = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        db_writer.writerow([email,subject,message])

if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port=5000)