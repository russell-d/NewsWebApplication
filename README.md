
**[NewsWebApplication ](http://23.239.22.138/)**

This News Web Application was created for [Capital One's coding challenge](https://www.mindsumo.com/contests/newsapi) to build a web application to search for Entertainment, News, and Sports news using [News API](https://newsapi.org/) as an exclusive data source.

## Table of Contents

 - [Description](#description)
 - [Technologies](#technologies)
 - [Launching Web App](#launching-web-app)
 -	[How It Works](#how-it-works)
 -	[Deploying Web App](#deploying-web-app)
 -	[Features](#features)
 -	[User Experience](#user-experience)


## 📝 Description

This web application gets its news articles from News API and displays articles in a visually pleasing way to the user. Users are able to choose from three categories of news to look at: Entertainment, Sports, or Technology, each having their own page. Each article can be clicked on to bring you to the actual article URL. It also includes a Home URL that allows you to look at some featured articles picked out from each of those three categories. There are visual features to make the experience on the web app much more enjoyable. 

## Technologies
 - [Python](https://www.python.org/)
 - [Flask](https://flask.palletsprojects.com/en/1.1.x/)
 - [HTML/CSS](https://www.w3.org/standards/webdesign/htmlcss.html#:~:text=HTML%20(the%20Hypertext%20Markup%20Language,for%20a%20variety%20of%20devices.))
 - [News API](https://newsapi.org/)
 - [WSGI](https://wsgi.readthedocs.io/en/latest/what.html)
 - [Apache](https://www.apache.org/)
 - [Ubuntu](https://ubuntu.com/)

## Launching Web App
To launch this application **locally**, you need to have Flask, Python, and the NewsAPI installed. Then you can run the init. py file. This should give give you a local URL to use to view it.  Otherwise, this application is already launched on a Linux server using Ubuntu.

***IMPORTANT: API KEY IS NOT INSIDE PYTHON FILE. MUST NEED OWN API KEY.***

**For Capital One: if web page is down, you may run locally. (python file needs API key) or contact: rdevera@csumb.edu** 

```
* Serving Flask app "__init__" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 766-717-937
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
***127.0.0.1:5000 is the URL for the local web app to run. Press it and will open up in web browser to be viewed.***
## How It Works

1. Get JSON file from News API python library. Depending on the category, passthrough the corresponding data.
```python
	tech_data = newsapi.get_everything(q = 'technology') 
```
This code gets all news articles pertaining to the category: technology.
	
2. Within HTML file, use a Flask for loop to go through dictionary given from JSON file. From here, we can access the keys to get information of each article.  ***This automation using Flask's loop helped tremendously to output all the articles.***

```html
{% for article in t_data["articles"] %}
<div  class = "art">
	<a href="{{article['url']}}"  target="_blank"  style="color:black; text-decoration: none;">
	<img src = "{{article['urlToImage']}}">
	<h3>{{article['title']}}</h3></a>
	<p class = "author">{{article['author']}}</p>	
</div>
{% endfor %}
```

3. Using CSS Grid, we could output each of these articles in a nice simple layout. Because the divs for the articles were created within the for loop, we can style all the articles the same, keeping it simple and clean for the user. 
```css
.layout{
	display:grid;
	grid-template-columns: 1fr  1fr  1fr;
	grid-auto-rows: minmax(200px,auto);
	grid-gap: 2em;
	margin: 50px;
	margin-top: 10px;
}
```
This is the base of the project with articles shown in a grid. I added a lot more features in the [features](#features) section!

  ## Deploying Web App
To deploy this application, I used a Linux server running Ubuntu. I used [Linode](https://cloud.linode.com/linodes) to host my server. I had to use Apache and WSGI in order to deploy the Flask Python application. 

## Features
**Technical features** would include the **Flask for loop** to go through all the articles within the JSON file. This was a very easy and simple way to display all the articles given. 

For **visual features**, I wanted to create a **user friendly** navigation, so I included a navigation bar with buttons for **home, sports, technology, and entertainment** which brought you to the URL. I also created links to my [LinkedIn](https://www.linkedin.com/in/russelldevera/) and [GitHub](https://github.com/russell-d) within the navigation bar. I also made a **main article**, which was bigger, to show **more details** like a bigger photo and description of the article. I picked a **second article** to have showcase as well. I included a **Top Headline article** at the top of the grid, which got the first article in the top headlines JSON. 

**Small aesthetic** features included were **light backgrounds** applied to the articles to show the grid, but not look ***too bold*** with all the images. The light backgrounds would turn a bit darker once you **hovered your mouse over the article** making it pop out more to the user. Buttons in the navigation bar also change color once you hover over them. The buttons in the navigation bar also have a color on them to **indicate which page** you are currently on.

 ## User Experience
 My goal was to create a **very visually pleasing**, *but simple layout* for users. Each article is **clickable** and will send the user to the chosen article URL for easy use. I decided that a **grid of articles** was the best way to approach this. I made sure to space out the articles evenly and give enough space so that it would not seem like they're all smushed together. I chose a **white background** to make it bright, and also gave each article a very light blue to not **overpower the article images**. To indicate the article hovered over, each article box **changes color** to a darker color.

The **home page** is much more simpler than the category pages, as it features only six articles from the different categories. I kept this **page simple** and the **content low**, so that the user would feel more inclined to look at the other URLs. I really liked the clean look with visual hover features for each article box. 

For each category page, I included a **Top Headline article** to showcase a top headline of that category. The first two articles shown are articles that **bring attention** to the user because they're displayed differently from the other articles on the page. The main article (the biggest) also displays the description of that article. They also have visual hover animations to **enchance the user experience**. The background changes on the main article and the second article turns the transparent title box to solid once hovered over. 

 ## Contact Info
 **email:** rdevera@csumb.edu
   --------[LinkedIn](https://www.linkedin.com/in/russelldevera/)
 --------[GitHub](https://github.com/russell-d)






