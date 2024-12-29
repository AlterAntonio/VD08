from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    # Запрос случайной цитаты из Forismatic API
    response = requests.get("http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=ru")
    quote_data = response.json()

    quote = quote_data['quoteText']
    author = quote_data['quoteAuthor'] if quote_data['quoteAuthor'] else "Неизвестный автор"

    return render_template('index.html', quote=quote, author=author)


if __name__ == '__main__':
    app.run(debug=True)