abc = { "1":"a",
        "2":"b",
        "3":"c"}

deutsch = {'key':['Schlüssel', 'Taste'],
           'slice':['Scheibe', 'Stück'],
           'value':['Wert']}
text = input("Geben Sie einen Text ein: ")
abctext = []
for buchstabe in text:
    if buchstabe in abc.keys():
        abctext.append(abc[buchstabe])


for m in abctext:
    print(m, end=" ")
