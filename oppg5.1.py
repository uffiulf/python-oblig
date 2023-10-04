
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
    
    filmlist.append({"name": name,
                     "year": year,
                     "rating": rating
                    })


#legg_til()

#print(filmlist)


#C)

funn=[]

def finn_film(yuo):
    for x in filmlist:
        if yuo in x.values():
            funn.append(x)

#finn_film()


#finn_film(yuo = input("hvilken film skal jeg finne basert på lanseringsåret?"))
#print(funn)



def fortsatt_oppg3_c():
    for x in filmlist:
        tjueti =2010
        if int(x["year"]) >= int(tjueti):
            funn.append(x)


fortsatt_oppg3_c()

print(funn)

open("filmliste.txt", "r", )
