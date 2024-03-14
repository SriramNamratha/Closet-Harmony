from tkinter import *
import menu

def details(dress, color, occasion, place):
    li = [dress, color, occasion, place]
    segregate(li)

colorSegregate = {}
categorySegregate = {}
ocasionSegregate = {}
placeSegregate = {}
dailyStack = []


def segregate(li):

    if li[2].lower() == "daily":
        dailyStack.append(li)

    def colorseg(li):
        list1 = [li[0], li[2], li[3]]
        if li[1] in list(colorSegregate.keys()):
            colorSegregate[li[1]].append(list1)
        else:
            colorSegregate[li[1]] = [list1]

    def catseg(li):
        list1 = [li[1], li[2], li[3]]
        if li[0] in list(categorySegregate.keys()):
            categorySegregate[li[0]].append(list1)
        else:
            categorySegregate[li[0]] = [list1]

    def ocaseg(li):
        list1 = [li[0], li[1], li[3]]
        if li[2] in list(ocasionSegregate.keys()):
            ocasionSegregate[li[2]].append(list1)
        else:
            ocasionSegregate[li[2]] = [list1]

    def placeseg(li):
        list1 = [li[0], li[1], li[2]]
        if li[3] in list(placeSegregate.keys()):
            placeSegregate[li[3]].append(list1)
        else:
            placeSegregate[li[3]] = [list1]

    colorseg(li)
    catseg(li)
    ocaseg(li)
    placeseg(li)

def display_next_two_days_outfits():
    list1 = []
    print("Next two days outfits:")
    for i in range(min(len(dailyStack), 2)):
        string = "A "+dailyStack[i][2]+" wear "+dailyStack[i][1]+" "+dailyStack[i][0]+" placed - "+dailyStack[i][3]
        list1.append(string)
    return list1


def display_colorseg_outfits():
        print("Color-wise segregation: \n")
        print(colorSegregate)
        return printcolorSeg(colorSegregate)

def display_catseg_outfits():
        print("Category-wise segregation: \n")
        return printcatSeg(categorySegregate)

def display_ocaseg_outfits():
        print("Occasion-wise segregation: \n")
        return printocasSeg(ocasionSegregate)

def display_placeseg_outfits():
        print("Place-wise segregation: \n")
        return printplaceSeg(placeSegregate)



def printcolorSeg(dic):
  key =[]
  value=[]
  for category in dic :
    key.append(category)
    print("-------")
    items=[]
    for i in dic[category] :
        string = "A "+i[1]+" wear "+i[0]+" placed - "+i[2]
        items.append(string)
    print("\n")
    value.append(items)
  print(list(zip(key,value)))
  return list(zip(key,value))

def printcatSeg(dic):
  key =[]
  value=[]
  for category in dic :
    key.append(category)
    items=[]
    for i in dic[category] :
        string = "A "+i[1]+" wear "+i[0]+" "+category+" placed - "+i[2]
        items.append(string)
    print("\n")
    value.append(items)
  print(list(zip(key,value)))
  return list(zip(key,value))

def printocasSeg(dic):
  key =[]
  value=[]
  for category in dic :
    key.append(category)
    items =[]
    for i in dic[category] :
        string = ("A "+i[1]+" "+i[0]+" placed - "+i[2])
        items.append(string)
    print("\n")
    value.append(items)
  print(list(zip(key,value)))
  return list(zip(key,value))

def printplaceSeg(dic):
  key =[]
  value=[]
  for category in dic :
    key.append(category)
    items =[]
    for i in dic[category] :
        string = ("A "+i[2]+" wear "+i[1]+" "+i[0])
        items.append(string)
    print("\n")
    value.append(items)
  print(list(zip(key,value)))
  return list(zip(key,value))