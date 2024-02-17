from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)

# app.config['SECRET_KEY'] = 'chickenzarecool21837'
# debug = DebugToolbarExtension(app)
# Debug toolbar kept giving me a strange error so I commented it out.

@app.route('/')
def homepage():
    prompts = story.prompts

    return render_template('home.html', prompts=prompts)

@app.route('/story')
def make_story():
    prompts = story.prompts
    res = {}

    for word in prompts:
        res[word] = request.args[word]

    story_markup = story.generate(res)
    
    return render_template('story.html', story_markup=story_markup)