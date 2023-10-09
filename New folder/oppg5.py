
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


#5.1 B)  + 5.1 C)

def legg_til(filmlist, name, year, rating):
    if rating == "":
        rating ="5.0"
    
    filmlist.append({"name": name,
                     "year": year,
                     "rating": rating
                    })

legg_til(filmlist, "The Matrix", "1999", "8.7")
legg_til(filmlist,"Pulp fiction","1994","8.9")
legg_til(filmlist,"The Godfather","1972","9.2")
#print(filmlist)

#5.2 A)
def print_ut(ny_liste):
    for x in ny_liste:
        print(x["name"] + " - " + x["year"] + " has a rating of " + x["rating"])

print_ut(filmlist)

#5.2 B)
def gjennomsnitt_rating(filmlist):
    total = 0
    for x in filmlist:
        total += float(x["rating"])
    return(total/len(filmlist))

print(gjennomsnitt_rating(filmlist))


funn=[]

# def finn_film(yuo):
#     for x in filmlist:
#         if yuo in x.values():
#             funn.append(x)

#5.2 C)
def search_by_year(filmlist, search):
    for x in filmlist:
        if int(x["year"]) >= int(search):
            funn.append(x)




tjueti = 2010
search_by_year(filmlist, tjueti)



print_ut(funn)


#5.3 A)
def skriv_til_fil(filmlist):
    with open("movies.txt", "w", ) as f:
        for x in filmlist:
            f.write(x["name"] + " - " + x["year"] + " has a rating of " + x["rating"] + "\n")


skriv_til_fil(filmlist)


#5.3 B)
def print_fil(fil):
    with open(fil, "r") as f:
        for x in f:
            print(x)


print_fil("movies.txt")