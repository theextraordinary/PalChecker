from flask import Flask, render_template, request, jsonify
from neural import NeuralNetwork
import numpy as np
W1=np.array([[  2.40978071,   0.30247406],
       [ 56.97853286,  19.73117201],
       [ 17.14350164,   5.97852652],
       [ 36.74955628,  12.72768208],
       [-23.36598997,  -8.12649493],
       [ -9.7293887 ,  -3.37495321],
       [  9.73855317,   3.34281586],
       [ 23.34620624,   8.08943399],
       [-36.67738699, -12.73407755],
       [-17.21293862,  -6.01362317],
       [-56.95966552, -19.74872262]])
W2=np.array([[ 30.45563674],
       [-40.03618253]])
net=NeuralNetwork(W1,W2)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/check_palindrome', methods=['POST'])
def check_palindrome():
    input_string = request.form.get('inputString').lower()
    if len(input_string)!=10:
        k="Please enter valid length."
        return jsonify({'result': k})
    
    s='1'+input_string
    X=list(s)
    X=[int(x) for x in X]

    flag=False
    for i in X:
        if i!=0 and i!=1:
            k="Please enter valid string."
            flag=True
            break
    if flag:
        return jsonify({'result': k})
    else:
        is_palindrome =net.predict(X,W1,W2)    
        result = 'It\'s a palindrome!' if is_palindrome[0] else 'It\'s not a palindrome.'

        return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
