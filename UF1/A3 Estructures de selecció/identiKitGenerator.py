"""
descripción: para formar la cara del sosopechoso...jejeje
"""
tipus = input("Dime que cara tiene: ").lower().split()
cabells = ""
ulls = ""
nas = ""
boca = ""

match tipus[0]:
    case "arrissats" : cabells = "@@@@@"
    case "llisos" : cabells = "VVVVV"
    case "pentinats": cabells = "XXXXX"

match tipus[1]:
    case "aclucats": ulls = ".-.-."
    case "rodons": ulls = ".o-o."
    case "estrellats": ulls = ".*-*."

match tipus[2]:
    case "aixafat": nas = "..0.."
    case "aromangat": nas = "..C.."
    case "agilenc": nas = "..V.."

match tipus[3]:
    case "normal": boca = ".===."
    case "bigoti": boca = ".∼∼∼."
    case "dents-sortides": boca = ".www."

print(f"{cabells}\n{ulls}\n{nas}\n{boca}\n")