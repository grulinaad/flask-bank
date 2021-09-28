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
        'SELECT a.id, title, balance, owner_id, username'
        ' FROM account a JOIN user u ON a.owner_id = a.id'
        ' ORDER BY id DESC'
    ).fetchall()
    # 'SELECT p.id, title, body, created, author_id, username'
    # ' FROM post p JOIN user u ON p.author_id = u.id'
    #   ' ORDER BY created DESC'
    return render_template('bank/index.html', accounts=accounts)

@bp.route('/create', methods=['GET', 'POST'])
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


@bp.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id, ))
    db.commit()
    return redirect(url_for('blog.index'))
