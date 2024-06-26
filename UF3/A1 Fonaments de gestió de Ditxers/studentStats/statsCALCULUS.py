"""
Description: Conèixer la nota mínima, la màxima i la mitjana dels seus alumnes apartir d'un fitxer amb moltes notes

Usage:
Input --> File
"""

import os
import statistics

studentSTATS = os.path.join('.','student.stats')

def leerYcontaar(studentSTATS):
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

stats = leerYcontaar(studentSTATS)
minG = minGrade(stats)
maxG = maxGrade(stats)
mitjG = mitjGrade(stats)
showRESULT(minG, maxG, mitjG)