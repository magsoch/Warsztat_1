from flask import Flask, request

app = Flask(_name_)


@app.route("/guessthenum", methods=["GET", "POST"])
def guessthenumber():
    guess = int(max - min) / 2 + min_
    if request.method == "GET":
        min = 0
        max = 1000
        num = 0
        return render_template("guessthenum.html")

    elif request.method == "POST":
        num += 1
        print('request.get_data: %s' % (request.get_data()))
        print("request.values: %s" % (request.args.getlist("key")))
        userans = list(request.form)[0]

        print(userans)
        if userans == " guessed":
            return " I won !"
        if userans == "more":
            min = guess
        elif userans == "less":
            max = guess
    return


app.run(port=5000)
