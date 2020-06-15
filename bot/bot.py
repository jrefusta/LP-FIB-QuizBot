import pandas as pd
import numpy as np
import telegram
from telegram import ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import networkx as nx
import matplotlib.pyplot as plt
import os
import pickle


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hola! Soc el QuizBot.")


def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="QuizBot contesta textualment i gràficament a preguntes relacionades a les enquestes descrites en el compilador.\nComanes:\n/start inicia la conversa amb el Bot.\n/help contesta amb una llista de comanes amb una breu descripció.\n/author nom complet de l'autor del projecte i mail de la FIB.\n/quiz <idEnquesta> inicia un intèrpret de l'enquesta descrita previament en el compilador.\n/bar <idEnquesta> mostra una gràfica de barres mostrant un diagrama de barres a la pregunta donada.\n/pie <idEnquesta> mostra una gràfica de formatget amb el percentatge a la pregunta donada.\n/report el bot ha de donar quelcom tipus taula amb el nombre de respostes obtingudes per cada valor de cada pregunta.")


def author(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Joan Manuel Ramos Refusta joan.manuel.ramos@est.fib.upc.edu")


def afegirVot(preg, val):
    try:
        dict = pickle.load(open("dict.pickle", "rb"))
        p = tuple([preg, val])
        if p in dict:
            dict[p] = dict[p] + 1
        else:
            dict[p] = 1
        pickle.dump(dict, open("dict.pickle", "wb"))
    except (OSError, IOError) as e:
        dict = {}
        p = tuple([preg, val])
        dict[p] = 1
        pickle.dump(dict, open("dict.pickle", "wb"))


def respostes(r):
    global possiblesRes
    possiblesRes = []
    res = ""
    for i in range(len(r)):
        if (r[i] == ':'):
            possiblesRes.append(r[i-2])
        if (r[i] == ' '):
            if (not r[i-1].isdigit() and r[i-1] != ';'):
                res = res + ' '
        elif (r[i] == ';'):
            res = res + '\n'
        else:
            res = res + r[i]
    return res


def quiz(bot, update, args):
    try:
        global dicN
        global listE
        global preg
        global identificador
        global destiN
        global listAltern
        global origenN

        listAltern = []
        destiN = ""
        G = nx.read_gpickle("../cl/test.gpickle")
        dicN = dict(G.nodes(data=True))
        identificador = str(args[0])
        inici = "Enquesta " + (dicN[identificador]['id']) + ":"
        bot.send_message(chat_id=update.message.chat_id, text=inici)
        listE = list(G.edges(data=True))
        origenN = (dicN[identificador]['id'])
        for i in range(len(listE)):
            if (listE[i][0] == origenN):
                destiN = (listE[i][1])
        preg = identificador
        if (dicN[destiN]['tipus'] == 'pregunta'):
            preg = preg + dicN[destiN]['p'] + "\n"
        origenN = destiN
        for i in range(len(listE)):
            if (listE[i][0] == origenN):
                if (listE[i][2]['tipus'] == 'item'):
                    resposta = (listE[i][1])
                if (listE[i][2]['tipus'] == 'normal'):
                    destiN = listE[i][1]
                if (listE[i][2]['tipus'] == 'alternativa'):
                    listAltern.append(tuple([listE[i][2]['number'], listE[i][1]]))
        if (dicN[resposta]['tipus'] == 'resposta'):
            r = dicN[resposta]['r']
        r = respostes(r)
        preg = preg + r
        bot.send_message(chat_id=update.message.chat_id, text=preg)

    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text="Error")


def interaccio(bot, update):
    try:
        global destiN
        global listAltern
        global ptControl
        global origenN
        global identificador
        global possiblesRes
        answer = update.message.text
        if (answer in possiblesRes and answer[0] != '/'):
            afegirVot(origenN, answer)
            for i in range(len(listAltern)):
                if (listAltern[i][0] == answer):
                    ptControl = destiN
                    destiN = listAltern[i][1]
            listAltern = []
            destiPrev = destiN
            if (dicN[destiN]['tipus'] != 'end'):
                preg = identificador
                if (dicN[destiN]['tipus'] == 'pregunta'):
                    preg = preg + dicN[destiN]['p'] + "\n"
                origenN = destiN
                for i in range(len(listE)):
                    if (listE[i][0] == origenN):
                        if (listE[i][2]['tipus'] == 'item'):
                            resposta = (listE[i][1])
                        if (listE[i][2]['tipus'] == 'normal'):
                            destiN = listE[i][1]
                        if (listE[i][2]['tipus'] == 'alternativa'):
                            listAltern.append(tuple([listE[i][2]['number'], listE[i][1]]))
                if (destiPrev == destiN):
                    destiN = ptControl
                if (dicN[resposta]['tipus'] == 'resposta'):
                    r = dicN[resposta]['r']
                r = respostes(r)
                preg = preg + r
                louise = update.message.text
                bot.send_message(chat_id=update.message.chat_id, text=preg)
            else:
                bot.send_message(chat_id=update.message.chat_id, text=identificador+"> Gràcies pel teu temps!")
                destiN = ""

    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text='Error')


def report(bot, update):
    try:
        dict = pickle.load(open("dict.pickle", "rb"))
        text = "*pregunta   valor   respostes* \n"
        for i in dict:
            text = text + str(i[0]) + '   ' + str(i[1]) + '   ' + str(dict[i]) + '\n'
        bot.send_message(chat_id=update.message.chat_id, text=text, parse_mode=ParseMode.MARKDOWN)
    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text="Error")


def pie(bot, update, args):
    try:
        dict = pickle.load(open("dict.pickle", "rb"))
        preg = str(args[0])
        labels = []
        sizes = []
        for i in dict:
            if (str(i[0]) == preg):
                labels.append(str(i[1]))
                sizes.append(int(dict[i]))
        explode = []
        for i in range(len(sizes)):
            explode.append(0.1)
        fig1, ax1 = plt.subplots()
        plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
        plt.axis('equal')
        plt.savefig('pie.png')
        bot.send_photo(chat_id=update.message.chat_id, photo=open('pie.png', 'rb'))
        plt.clf()
        os.remove('pie.png')
    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text="Error")


def bar(bot, update, args):
    try:
        dict = pickle.load(open("dict.pickle", "rb"))
        preg = str(args[0])
        labelsb = []
        sizesb = []

        for i in dict:
            if (str(i[0]) == preg):
                labelsb.append(str(i[1]))
                sizesb.append(int(dict[i]))
        plt.bar(labelsb, sizesb)
        plt.savefig('bar.png')
        bot.send_photo(chat_id=update.message.chat_id, photo=open('bar.png', 'rb'))
        plt.clf()
        os.remove('bar.png')
    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text="Error")


TOKEN = open('token.txt').read().strip()
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('author', author))
dispatcher.add_handler(CommandHandler('quiz', quiz, pass_args=True))
dispatcher.add_handler(MessageHandler(Filters.text, interaccio))
dispatcher.add_handler(CommandHandler('report', report))
dispatcher.add_handler(CommandHandler('pie', pie, pass_args=True))
dispatcher.add_handler(CommandHandler('bar', bar, pass_args=True))
updater.start_polling()
