from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'replace-with-a-secure-random-key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    products_list = [
        {'title': 'Khaki Bags', 'desc': '1 kg / 1/2 kg / 1/4 kg'},
        {'title': 'Gift Bags', 'desc': 'All sizes'},
        {'title': 'Envelopes', 'desc': 'All sizes'},
        {'title': 'Pharmacy Envelopes', 'desc': ''},
        {'title': 'Carrier Bags', 'desc': ''},
        {'title': 'Branding', 'desc': 'Custom branded packaging'},
    ]
    return render_template('products.html', products=products_list)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        flash(f'Thanks {name or "Friend"}, your message has been received!')
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
 
    
