from flask import Flask, render_template
from flask import request
import openai

openai.api_key = 'Key'
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('openai.html')


@app.route("/generate-img", methods=['GET', 'POST'])
def generate_img():
   
    if request.method == 'POST':
        try:
            response = openai.Image.create(
                prompt=f"{request.form['text']}",
                n=1,
                size="1024x1024"
            )
            image_url = response['data'][0]['url']
            return f"""
                <h1> {request.form['text']}</h1>
                <img src='{image_url}' alt='#'>
            """  
        except:
            return 'Ошибка генерации'  
    return render_template('openai.html')


if __name__ == '__main__':
    app.run()
