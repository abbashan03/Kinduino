abc = { "1":"a",
        "2":"b",
        "3":"c"}

deutsch = {'key':['Schlüssel', 'Taste'],
           'slice':['Scheibe', 'Stück'],
           'value':['Wert']}

f = open("Testabc.txt", "r")
daten = f.read()
text = input("Drücken sie Enter ")
abctext = [print(daten)]
for buchstabe in text:
    if buchstabe in abc.keys():
        abctext.append(abc[buchstabe])

