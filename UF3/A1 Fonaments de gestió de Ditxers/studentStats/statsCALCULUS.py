import os
import statistics

studentSTATS = os.path.join('.','student.stats')

def leerYcontaar(archivo):
    with open(studentSTATS, mode="r") as entrada:
        stats = entrada.read()
    stats = stats.split()
    stats = [int(num) for num in stats if num.isdigit()]
    return stats

def minGrade(stats):
    minG = min(stats)
    return minG

def maxGrade(stats):
    maxG = max(stats)
    return maxG

def mitjGrade(stats):
    mitjG = statistics.mean(stats)
    return mitjG

def showRESULT(minG,maxG,mitjG):
    print("Nota mínima: ", minG)
    print("Nota màxima: ", maxG)
    print("Nota mitjana: ", mitjG)

leerYcontaar()
minGrade()
maxGrade()
mitjGrade()
showRESULT()