from flask import Blueprint, render_template, redirect, url_for, request

import stripe

stripe.api_key = 'sk_test_g53JOW09nFINCJSdhaGTEbuu00t5waE8kI'

bp = Blueprint('payment', __name__)


@bp.route('/checkout', methods=('GET', 'POST'))
def checkout():
    if request.method == 'POST':
        token = request.form.get('stripeToken')
        charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description='test charge',
            source=token
        )
        return redirect(url_for('payment.index'))
    return render_template('checkout.html')


@bp.route('/', methods=('GET',))
def index():
    return render_template('index.html')
