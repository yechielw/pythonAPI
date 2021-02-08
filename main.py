from flask import Flask, request, escape
from os import popen

app = Flask(__name__)
history = list()
@app.route("/")
def index():
    cmd = str(escape(request.args.get("cmd", "")))
    result = popen(cmd).read()
    history.append(cmd)
    return("""
                <h1>Python API v 0.0.3 (β)</h1>
                <p>welcome!</p>
                <p>You cat send commands here or as a simple get request in the URL</p>
                <form action="" method="get">
                    <input type="text" name="cmd">
                    <input type="submit" value="Send">
                </form>

""" + result + "<h3>Lasr command</h3> {} <br>".format(cmd) + "<br> History: <br> {}".format("<br>".join(reversed(history[:-1]))))

@app.route("/<cmd>")
def command(cmd):
    system(cmd)
    return cmd
    #system(cmd)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
