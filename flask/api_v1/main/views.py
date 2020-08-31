from .models import MyTable
from .forms import TokenizerForm
from .. import db
from . import main
from flask import (
    request, render_template, redirect,
    flash, url_for, current_app, g
)

# 형태소 분석기
from konlpy.tag import Okt
tokenizer = Okt()

# ping 테스트 앤드포인트
@main.route("/ping")
def ping():
    return "pong"

# db 테스트 앤드포인트
@main.route('/db')
def db_test():
    # insert
    inserted_tables = [ MyTable(test=test) for test in ['test1','test2']]
    db.session.add_all(inserted_tables)
    db.session.commit()

    # select
    mytables = MyTable.query.all()
    mytable_cnt = len(mytables)
    if len(mytables) >= 100:
        # delete
        MyTable.query.delete()
        db.session.commit()

    return render_template('main/db_test.html', mytables=mytables, mytable_cnt=mytable_cnt)

# index 페이지 ( 형태소 분석기 )
@main.route('/', methods=['GET', 'POST'])
def index():
    form = TokenizerForm(request.form)
    tokenized_sentence = "분석전"

    if form.validate_on_submit():
        input_sentence = form.input_sentence.data.strip()
        tokenized_sentence = str(tokenizer.pos(input_sentence))

    return render_template('main/index.html', tokenized_sentence=tokenized_sentence, form=form)
    

