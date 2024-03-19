from flask import Flask, render_template
import ec2

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    # Execute o código Python do arquivo ec2.py e obtenha a saída
    resultado = ec2.main()
    return render_template('resultado.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
