
#5.1 A)
filmlist = [
    {
        "name" : "Inception",
        "year" : "2010",
        "rating" : "8.7" 
    },
    {
        "name" : "Inside Out",
        "year" : "2015",
        "rating" : "8.1"
    },
    {
        "name" : "Con Air",
        "year" : "1997",
        "rating" : "6.9"
    }
]


#5.1 B)


def legg_til():
    name = input("navn på film: ")
    year = input("Når ble filmen lansert?: ")
    rating = input("IMDB rating?: ")
    if rating == "":
        rating ="5.0"
    
    filmlist.append({"name": name,
                     "year": year,
                     "rating": rating
                    })
#bruker kan velge selv hva som skal legges til i listen
legg_til()


print(filmlist)




funn=[]

def finn_film(yuo):
    for x in filmlist:
        if yuo in x.values():
            funn.append(x)




#finn_film(yuo = input("hvilken film skal jeg finne basert på lanseringsåret?"))
#print(funn)



def fortsatt_oppg3_c():
    for x in filmlist:
        tjueti =2010
        if int(x["year"]) >= int(tjueti):
            funn.append(x)


fortsatt_oppg3_c()

print(funn)



def skriv_til_fil(filmlist):
    with open("movies.txt", "w", ) as f:
        for x in filmlist:
            f.write(x["name"] + " " + x["year"] + " " + x["rating"] + "\n")


skriv_til_fil(filmlist)

