from flask import Flask, render_template, redirect, url_for
import requests

app = Flask(__name__)

# Sample content data (for demonstration)
content = [
    {"title": "Iron Man", "description": "Tony Stark becomes Iron Man.", "type": "movie"},
    {"title": "The Avengers", "description": "Marvel superheroes unite to save the world.", "type": "movie"},
    {"title": "WandaVision", "description": "Wanda and Vision's mysterious suburban life.", "type": "series"},
    {"title": "Black Panther", "description": "T'Challa returns to Wakanda as king.", "type": "movie"},
    {"title": "Loki", "description": "Loki's adventures after Endgame.", "type": "series"},
]


# OMDb API key (replace with your actual API key)
OMDB_API_KEY = "6a934989"

@app.route('/content/<int:index>')
def content_page(index):
    if 0 <= index < len(content):
        content_data = content[index]
        if content_data["type"] == "movie":
            return redirect(url_for('movie', index=index))
        elif content_data["type"] == "series":
            return redirect(url_for('series', index=index))
    else:
        return "Content not found"

@app.route('/movie/<int:index>')
def movie(index):
    if 0 <= index < len(content):
        content_data = content[index]
        content_title = content_data["title"]
        
        # Fetch movie details from OMDb API
        params = {"t": content_title, "apikey": OMDB_API_KEY}
        response = requests.get("http://www.omdbapi.com/", params=params)
        movie_info = response.json()
        
        return render_template('movie.html', content=content_data, movie=movie_info)
    else:
        return "Movie not found"

@app.route('/series/<int:index>')
def series(index):
    if 0 <= index < len(content):
        content_data = content[index]
        content_title = content_data["title"]
        
        # Fetch series details from OMDb API
        params = {"t": content_title, "apikey": OMDB_API_KEY}
        response = requests.get("http://www.omdbapi.com/", params=params)
        series_info = response.json()
        
        return render_template('series.html', content=content_data, series=series_info)
    else:
        return "Series not found"

@app.route('/')
def index():
    return render_template('index.html', content=content)

@app.route('/skrull')
def skrull():
    return render_template('species/skrull.html')



if __name__ == '__main__':
    app.run(debug=True)
