from flask import Flask, request,render_template
import openai
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# set up OpenAI API credentials
openai.api_key = os.environ["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"]

@app.route('/prompt', methods=['POST'])
def generate_text():
    prompt = request.form['prompt']
    model = "davinci"
    completions = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message

if __name__ == '__main__':
    app.run(debug=True)
