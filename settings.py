from datetime import date, timedelta
PAGINA = 0
SIZE = 20
N_AGENDAMENTO = 0
PROBLEMA  = "vago"
MODELO_CARRO = "vago" 
MARCA_CARRO = "vago" 


DATA = (date.today() + timedelta(days=3)).strftime("%d/%m/%y")
DATA0 = (date.today() + timedelta(days=3)).strftime("%d/%m/%y")
DATA1 = (date.today() + timedelta(days=17)).strftime("%d/%m/%y") 
DATA2 = (date.today() + timedelta(days=24)).strftime("%d/%m/%y")  

DATAOP1 = (date.today() + timedelta(days=17)).strftime("%d/%m/%y") 
DATAOP2 = (date.today() + timedelta(days=24)).strftime("%d/%m/%y")

MARCA_CARROS = [
    "toyota", "ford", "chevrolet", "honda", "nissan", 
    "volkswagen", "bmw", "mercedes-benz", "audi", "hyundai", 
    "kia", "subaru", "mazda", "dodge", "jeep", 
    "porsche", "lexus", "jaguar", "ferrari", "lamborghini"
]

MODELOS_CARROS = [
    ["corolla", "camry", "rav4", "highlander", "prius"],  # toyota
    ["f-150", "mustang", "explorer", "escape", "fusion"],  # ford
    ["silverado", "equinox", "malibu", "tahoe", "camaro"],  # chevrolet
    ["civic", "accord", "cr-v", "pilot", "fit"],  # honda
    ["altima", "sentra", "rogue", "murano", "pathfinder"],  # nissan
    ["golf", "passat", "tiguan", "jetta", "polo"],  # volkswagen
    ["3 series", "5 series", "x5", "x3", "4 series"],  # bmw
    ["c-class", "e-class", "glc", "gle", "s-class"],  # mercedes-benz
    ["a4", "a6", "q5", "q7", "a3"],  # audi
    ["elantra", "sonata", "tucson", "santa fe", "kona"],  # hyundai
    ["soul", "sportage", "sorento", "optima", "stinger"],  # kia
    ["outback", "forester", "impreza", "crosstrek", "legacy"],  # subaru
    ["mazda3", "mazda6", "cx-5", "cx-9", "mx-5 miata"],  # mazda
    ["charger", "challenger", "durango", "ram 1500", "grand caravan"],  # dodge
    ["wrangler", "grand cherokee", "cherokee", "compass", "renegade"],  # jeep
    ["911", "cayenne", "macan", "panamera", "taycan"],  # porsche
    ["rx", "es", "nx", "gx", "ls"],  # lexus
    ["f-pace", "xe", "xf", "e-pace", "i-pace"],  # jaguar
    ["488 gtb", "portofino", "f8 tributo", "roma", "sf90 stradale"],  # ferrari
    ["huracan", "aventador", "urus", "gallardo", "murcielago"]  # lamborghini
]


OFICINAS_MECANICAS = [
    "Auto Mecânica Silva",
    "Oficina do João",
    "ReparAuto",
    "Mecânica Rápida",
    "Oficina São José",
    "Auto Center Elite",
    "Oficina Bom Carro",
    "Mecânica da Vila",
    "Oficina dos Amigos",
    "Mecânica Qualicar"
]

