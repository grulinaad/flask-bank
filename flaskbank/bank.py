from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskbank.auth import login_required
from flaskbank.db import get_db

bp = Blueprint('bank', __name__)



@bp.route('/')
def index():
    db = get_db()
    accounts = db.execute(
        
    ).fetchall()
    return render_template('bank/index.html', accounts=accounts)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?. ?, ?)'
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('bank.index'))

        return render_template('bank/create.html')


@bp.route('/int:id>/delete', methods=('POST'))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id, ))
    db.commit()
    return redirect(url_for('blog.index'))

@bp.route('/transaction', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        from_account = int(request.form['from_account'])
        to_account = request.form['to_account']
        amount = request.form['amount']
        error = None
        correct_owner = 0

        if not from_account:
            error = "From account is required."
        if not to_account:
            to_account = "From account is required."
        if not amount:
            amount = "Amount is required."
        if error is not None:
            flash(error)
        else:
            db = get_db()

            db.execute(
                correct_owner = 'EXISTS(SELECT * FROM account WHERE id = ? AND owner_id = ?' , (from_account, userid?)))
            db.commit()
            if correct owner = 1: 
                db.execute(
                bal1 = 'SELECT balance FROM account WHERE id = ?' , (from_account, )
                bal2 = 'SELECT balance FROM account WHERE id = ?' , (from_account, )
                new_bal1 = bal - amount
                new_bal2 = bal + amount
                'UPDATE account'
                if bal1 > 0: 
                    'SET balance = ? ', (newbal1, )
                    'WHERE id = ? ', (to_account, )
                'SET balance = ? ', (newbal2)
                'WHERE id = ? ', (from_account))

            return redirect(url_for('bank.index'))

        return render_template('bank/create.html')