from flask import Flask, redirect, url_for, render_template #flask
from newsapi import NewsApiClient #importing NewsAPI API client

newsapi = NewsApiClient(api_key='') #business key
app = Flask(__name__)

#NewsAPI dictionaries for each category
top_tech_data = newsapi.get_top_headlines(q = 'technology')
top_sports_data = newsapi.get_top_headlines(q = 'sports')
top_ent_data = newsapi.get_top_headlines(q = 'entertainment')
tech_data = newsapi.get_everything(q = 'technology')
sports_data = newsapi.get_everything(q = 'sports')
ent_data = newsapi.get_everything(q = 'entertainment')

@app.route('/')
def home(): #home page
	return render_template('homepage.html', t_data = tech_data, s_data = sports_data, e_data = ent_data) #pass in these dictionaries

@app.route('/TechnologyNews')
def tech(): #tech page
    return render_template('technews.html', t_data = tech_data, top_t_data = top_tech_data)

@app.route('/SportsNews')
def sports(): #sports page
    return render_template('sportsnews.html' , s_data = sports_data, top_s_data = top_sports_data)

@app.route('/EntertainmentNews')
def ent(): #entertainment page
    return render_template('entnews.html', e_data = ent_data, top_e_data = top_ent_data)

if __name__ == '__main__':
    app.run(debug = True)

