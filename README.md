# Quizbot

Pràctica de l'assignatura Llenguatges de Programació 19-20Q1. Consisteix en un bot per Telegram que constesta textualment i gràficament a preguntes relacionades amb les enquestes descrites amb el compilador descrit prèviament, així com recullir les dades d’enquestes.



## Requeriments

Per instal·lar els requeriments només caldrà instal·lar els imports necessaris fent la comana:

```
pip install -r requirements.txt
```

Podrem generar el compilador d'Enquestes en qualsevol distribució de Linux.

El bot funcionarà amb el Telegram Desktop o l'App de mòbil tant de iOS com Android.



## Començar la utilització

**Compilador**

Dins de la carpeta cl, executarem des de terminal la següent comana:

```
python3 test.gramatica.py input.txt
```

Podrem veure per terminal la forma que té la gramàtica i com es genera l'AST. El resultat hauría de ser una cosa com aquesta:

![](https://imgur.com/XKWeGtr.png)



Dins de la carpeta cl, executarem des de terminal la següent comana:

```
python3 test.test.py input.txt
```

input.txt conté l'arxiu de texte on es mostra el llenguatge (preguntes, respostes, items, alternatives...) que ens facilita l'enunciat del projecte.

amb aquesta comana, se'ns obrirà una finestra amb la imatge que representa el graf del compilador esmentat a l'enunciat del projecte, es crearà un arxiu 'graf.png' amb aquesta mateixa imatge i es crearà el fitxer test.gpickle al que recurrim per la part del bot de Telegram.

![graf.png](https://imgur.com/ibWCcNb.png)

**Bot**

Una vegada tinguem els requeriments instal·lats, dins de la carpeta bot, posarem en marxa el bot gràcies a la comana:

```
python3 bot.py
```

És important que dins del directori tinguem també un arxiu **token.txt** per poder associar-lo al bot de Telegram.



## Tests i exemples

#### Comanes del bot

```
/start
```

Inicia la conversa amb el Bot.

![image-20200106204357815](https://imgur.com/e9tpafc.png)



```
/help
```

Retorna una llista amb totes les comanes disponibles i una breu descripció.

![image-20200106204525681](https://imgur.com/SMOVEJ4.png)



```
/author
```

Retorna l'autor d'aquest Bot.![image-20200106204808498](https://imgur.com/DfxmRTM.png)



```
/quiz <idEnquesta>
```

Inicia un intèrpret de l'enquesta <idEnquesta> descrita previament en el compilador. 

![image-20200106205821331](https://imgur.com/sAmduXv.png)



L'<idEnquesta> ha d'estar descrita prèviament en el compilador. De no ser així, es donarà un error i no  carregarà l'arxiu corresponent

![image-20200106211124370](https://imgur.com/qSRJmKz.png)



Quan, per exemple, responem al bot amb una resposta que no está dins de les donades, el bot no guardarà la informació de la resposta donada i esperarà fins a que es doni una resposta vàlida a la pregunta.

![image-20200106210938804](https://imgur.com/hKDzJql.png)

Si desprès de finalitzar una enquesta responem amb cualsevol cosa, ens donarà un Error i la resposat no quedarà guardadaen cap lloc.

![image-20200106211243772](https://imgur.com/Yv1plCz.png)

```
/bar <idPregunta>
```

 El Bot retorna una gràfica de barres mostrant un diagrama de barres de les respostes a la pregunta donada. 

Per exemple, en un moment determinat tenim la següent bar per P1:

![image-20200106212818600](https://imgur.com/JhvYCds.png)

Si tornem a contestar a la pregunta P1 del quiz E d'aquesta manera...

![image-20200106212556853](https://imgur.com/S62klGT.png)

La nova bar per P1 té la següent forma:

![image-20200106212849936](https://imgur.com/Dq3lQfM.png)



```
/pie <idPregunta>
```

 El Bot retorna una gràfica de formatget amb el percentatge de les respostes a la pregunta donada. 

Per exemple, en un moment determinat tenim el següent pie per P1:

![image-20200106212350460](https://imgur.com/Orv3597.png)

Si tornem a contesr a la pregunta P1 del quiz E d'aquesta manera...

![image-20200106212556853](https://imgur.com/S62klGT.png)

El nou pie per P1 té la següent forma:

![image-20200106212631660](https://imgur.com/qTjvysZ.png)



```
/report
```

El Bot retorna quelcom tipus taula amb el nombre de respostes obtingudes per cada valor de cada pregunta. 

Per exemple, en un moment determinat tenim el següent report:

![image-20200106213057254](https://imgur.com/z2khNx9.png)

Si tornem a contestar al quiz E d'aquesta manera...

![image-20200106213200257](https://imgur.com/0G70vw1.png)

El nou report té la següent forma:

![image-20200106213236435](https://imgur.com/vSP0das.png)



## Autor

Joan Manuel Ramos Refusta

e-mail de la FIB: joan.manuel.ramos@est.fib.upc.edu