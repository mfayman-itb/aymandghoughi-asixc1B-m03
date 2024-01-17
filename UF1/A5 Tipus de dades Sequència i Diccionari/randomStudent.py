import random

CORREO = (
    "tamoor.asghar.7e7@itb.cat",
    "xavier.cabello.7e7@itb.cat",
    "oriol.canellas.7e3@itb.cat",
    "ayman.dghoughi.7e7@itb.cat",
    "ian.diaz.7e7@itb.cat",
    "nizar.elkhoulfi.7e7@itb.cat",
    "izan.fernandez.7e7@itb.cat",
    "eric.gonzalez.7e7@itb.cat",
    "hugo.gonzalez.7e7@itb.cat",
    "marc.guerra.7e7@itb.cat",
    "rafael.guiotto.7e7@itb.cat",
    "jaffet.hernandez.7e5@itb.cat",
    "daniel.hernandez.zerpa.7e7@itb.cat",
    "helena.herrera.7e5@itb.cat",
    "faizan.hussain.7e7@itb.cat",
    "iker.jimenez.7e7@itb.cat",
    "matvei.karikh.7e6@itb.cat",
    "alejandro.liebana.7e7@itb.cat",
    "didac.lloret.7e7@itb.cat",
    "yeray.lopez.7e7@itb.cat",
    "trishan.mizhquiri.7e6@itb.cat",
    "david.munoz.7e7@itb.cat",
    "andre.oyarzo.7e7@itb.cat",
    "saul.requena.7e7@itb.cat",
    "andrea.riba.7e7@itb.cat",
    "ruben.sanchez.7e7@itb.cat",
    "pol.sanchez.7e7@itb.cat",
    "taranpreet.singh.7e7@itb.cat",
    "rene.tubiera.7e7@itb.cat",
    "jordi.yu.7e7@itb.cat"
)

pick = random.randint(0, len(CORREO) - 1)
print(CORREO[pick])
