from cards import card_name, adv, card_recommend
from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)
app.secret_key = "Something"

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/recommend')
def recommend():
    return render_template('recommend.html')

@app.route('/recommend/result', methods=['POST','GET'])
def result():
    if request.method == 'POST':
        if len(request.form) < 13:
            flash("놓친 항목은 없는지 확인해 주세요!")
            return redirect('/recommend')
        else:
            infos, prop_card = card_recommend(request.form)
            img_url = infos[0]
            details = infos[1]
            pdf = infos[2]
            return render_template('recommend_result.html',img_url = img_url, details = details, pdf = pdf, card = prop_card)

@app.route('/cards')
def cards() :
    return render_template('cards.html',  map_active = "None", cards_active = "active")

@app.route('/cards/<int:id>')
def card_detail(id):
    adv_single = adv[id]
    name_single = card_name[id]
    img_url = "/static/img/" + str(id) + ".png"
    return render_template(
        'card_detail.html',
        id = id, 
        map_active = "None", 
        cards_active = "active",
        adv=adv_single,
        name = name_single,
        img_url = img_url
        )


if __name__ == "__main__":
    app.run()