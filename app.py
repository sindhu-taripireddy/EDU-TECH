import os
from flask import Flask, render_template, abort

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

app = Flask(__name__, template_folder=TEMPLATE_DIR)

@app.route("/")
@app.route("/index")
@app.route("/index.html")
@app.route("/home")
@app.route("/home.html")
def index():
    return render_template("home.html")

@app.route("/<path:page>")
def render_page(page):
    # Ensure page ends with .html for template lookup
    template_name = page if page.endswith(".html") else f"{page}.html"
    
    # Check if template file exists in templates folder
    template_path = os.path.join(app.template_folder, template_name)
    if os.path.exists(template_path):
        return render_template(template_name)
        
    abort(404)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("home.html"), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "True").lower() == "true"
    print("\n" + "=" * 55)
    print(f" [EduTech] Flask Application Running on http://127.0.0.1:{port}")
    print(" Press CTRL+C in terminal to stop the server")
    print("=" * 55 + "\n")
    app.run(debug=debug, host="0.0.0.0", port=port)