from flask import Flask, render_template, request

app = Flask(__name__)

total_categoria_I = 0
total_categoria_II = 0
total_categoria_III = 0
total_categoria_IV = 0
total_categoria_V = 0
total_categoria_VI_VII = 0

@app.route('/cobrar', methods=['POST'])
def cobrar():
    global total_categoria_I, total_categoria_II, total_categoria_III, total_categoria_IV, total_categoria_V, total_categoria_VI_VII
    opc = int(request.form['opc'])
    vlr = int(request.form['vlr'])

    if opc == 1:
        if vlr < 10600:
            dif = 10600 - vlr
            faltante = int(request.form['faltante'])
            vlr += faltante
            if vlr == 10600:
                total_categoria_I += vlr
        else:
            total_categoria_I += vlr

    elif opc == 2:
        if vlr < 11500:
            dif = 11500 - vlr
            faltante = int(request.form['faltante'])
            vlr += faltante
            if vlr == 11500:
                total_categoria_II += vlr
        else:
            total_categoria_II += vlr

    elif opc == 3:
        if vlr < 25400:
            dif = 25400 - vlr
            faltante = int(request.form['faltante'])
            vlr += faltante
            if vlr == 25400:
                total_categoria_III += vlr
        else:
            total_categoria_III += vlr

    elif opc == 4:
        if vlr < 33200:
            dif = 33200 - vlr
            faltante = int(request.form['faltante'])
            vlr += faltante
            if vlr == 33200:
                total_categoria_IV += vlr
        else:
            total_categoria_IV += vlr

    elif opc == 5:
        if vlr < 38400:
            dif = 38400 - vlr
            faltante = int(request.form['faltante'])
            vlr += faltante
            if vlr == 38400:
                total_categoria_V += vlr
        else:
            total_categoria_V += vlr

    elif opc == 6:
        if vlr < 38400:
            dif = 38400 - vlr
            faltante = int(request.form['faltante'])
            vlr += faltante
            if vlr == 38400:
                total_categoria_VI_VII += vlr
        else:
            total_categoria_VI_VII += vlr

    total = total_categoria_I + total_categoria_II + total_categoria_III + total_categoria_IV + total_categoria_V + total_categoria_VI_VII

    return render_template('index.html', total_categoria_I=total_categoria_I, total_categoria_II=total_categoria_II, total_categoria_III=total_categoria_III, total_categoria_IV=total_categoria_IV, total_categoria_V=total_categoria_V, total_categoria_VI_VII=total_categoria_VI_VII, total=total)