from flask import Flask, render_template, request
import openai
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

openai.api_key = os.getenv('OPENAI_API_KEY')

db_config = {
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'port': os.getenv('DB_PORT', 5432),
    'sslmode': 'require'
}

def generate_sql_query(natural_language_query):
    prompt = f"Convert the following natural language query into a SQL query for PostgreSQL:\n\n{natural_language_query}\n\nSQL Query:"
    response = openai.Completion.create(
        engine='gpt-3.5-turbo-instruct',
        prompt=prompt,
        max_tokens=150,
        temperature=0,
        n=1,
        stop=[";"]
    )
    sql_query = response.choices[0].text.strip()
    return sql_query

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    user_input = ''
    error = None
    if request.method == 'POST':
        user_input = request.form['user_input']
        try:
            sql_query = generate_sql_query(user_input)
            conn = psycopg2.connect(**db_config)
            cur = conn.cursor()
            cur.execute(sql_query)
            result = cur.fetchall()
            cur.close()
            conn.close()
        except Exception as e:
            error = str(e)
    return render_template('index.html', result=result, user_input=user_input, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    