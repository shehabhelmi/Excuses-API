from flask import Flask , render_template

import random

developer_excuses = [
    "It works on my machine.",
    "The bug is shy, it only appears in production.",
    "I didn't touch anything, I swear.",
    "The code was working yesterday.",
    "It works perfectly… just not on this planet.” 🌍",
    "The bug disappeared when I started recording my screen",
    "I didn’t break the code, I simply exposed its true nature",
    "The code is fine, the universe is just having a bad day",
    "It’s not a bug, it’s an undocumented feature.",
    "The server crashed because it sensed my confidence",
    "I fixed it, but I’m not sure how… so please don’t touch anything.",
    "The problem solved itself after I threatened to rewrite everything.” 😈",
    "The code was working until someone looked at it. 👀",
    "I tested it in my head, and it worked flawlessly. 🧠✨",

 ]


def generateExcuse():
 excuse = random.choice(developer_excuses)
 return excuse 

app = Flask(__name__)

@app.route("/")
def Home():
 return render_template("index.html",Excuse = generateExcuse() )


app.run(host="0.0.0.0" , port=5004 , debug = False)
