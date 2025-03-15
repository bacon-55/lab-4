import json
ffile = "c:/Users/denis/Documents/LAB4/json/data.json"
with open(ffile) as file:
    our_json = json.load(file) 
    print('''Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------''')
    imdata = our_json['imdata']
    for x in imdata:
        item = x['l1PhysIf']
        attributes = item['attributes']
        dn = attributes['dn']
        speed = attributes['speed']
        mtu = attributes['mtu']
        print(dn + '                              ' + ' '*abs(42-len(dn)) + speed + '   ' + mtu)