from restaurant_db import app 
from flask import Flask, render_template, request, flash
from menus import Data

@app.route('/', methods=['GET','POST'])
def home():

    data = Data()

    result = []
    selected= []
    if request.method == 'POST':
        # GET POST FROM FLASK HOWWWWWW         
        restaurant = request.form['restaurant']
        option = request.form['option']

        if option == "CSM" :
            date = request.form['date']
            result.append(date)
            result.append(data.csm[restaurant][data.dates[date]])
            selected.append("Date")
            selected.append("CSM")
        elif option == "Average CSM vs Yelp Factor" :
            result = [
                    data.csm_yelp[restaurant]['csm'],
                    data.csm_yelp[restaurant]['yelp']
                    ]
            selected.append("Average CSM")
            selected.append("Yelp Factor")

        elif option == "Vegetarian Factor vs Average Tip" :
            result = [
                data.v_tip[restaurant]['tip'], 
                data.v_tip[restaurant]['v']
                ]
            selected.append("Average Tip")
            selected.append("Vegetarian Factor")

        elif option == "Vegetarian Factor vs Yelp Factor" :
            result = [
                    data.v_yelp[restaurant]['v'],
                    data.v_yelp[restaurant]['yelp']
                    ]
            selected.append("Vegetarian Factor")
            selected.append("Yelp Factor")

        return render_template('home.html', data=data, selected=selected, result=result, restaurant_name=restaurant)

    elif request.method == 'GET':
        return render_template('home.html', data=data, selected=selected, result=result)

    return render_template('home.html')

@app.route('/testdb')
def testdb():
    if db.session.query("1").from_statement("SELECT 1").all():
        return 'It works.'
    else:
        return 'Something is broken'

def parse_query(q):
    return 'your query was ' + q

