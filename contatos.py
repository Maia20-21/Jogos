from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/contatos.html', methods=['GET', 'POST'])
def contatos():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        

       
        msg = MIMEText(f'Nome: {nome}\nEmail: {email}\n') 
        msg['Subject'] = 'Novo contato'
        msg['From'] = 'seu_email@gmail.com' 
        msg['To'] = 'br2020maia@gmail.com'


        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login('seu_email@gmail.com', 'sua_senha')
        smtp.sendmail('seu_email@gmail.com', 'br2020maia@gmail.com', msg.as_string())
        smtp.quit()

        return 'Cadastro finalizado com sucesso'

    return render_template('contatos.html')

if __name__ == '__main__':
    app.run(debug=True)
