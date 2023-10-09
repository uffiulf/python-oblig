#5.3 B)
def les_fil(print_filmlist):
    with open("movies.txt", "r") as f:
        for x in f:
            x = x.strip()
            x = x.split(" - ")
            print_filmlist.append({"name": x[0],
                             "year": x[1],
                             "rating": x[2]
                            })

print_filmlist = []
les_fil(print_filmlist)

print(print_filmlist)