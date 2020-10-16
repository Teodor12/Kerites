import random

even_properties = []
odd_properties = []
properties = []


def feladat_1():
    try:
        file = open("kerites.txt")
        for row in file:
            properties.append(row.strip("\n"))
            datas = row.split(" ")
            if(datas[0] == "0"):
                even_properties.append(row.strip('\n'))
            else:
                odd_properties.append(row.strip('\n'))
        print("Fajl olvasasa befejezve!")
    except IOError as e:
        print("Hiba fajl olvasasakor!")


def feladat_2():
    print("2. feladat")
    print("Az eladott telkek szama: ", len(properties))


def feladat_3():
    print("3. feladat")
    datas = properties[-1].split(" ")
    side = datas[0]

    if(side == "0"):
        print("Paros oldalon adtak el az utolso telket!")
        print("Az utolso telek szama: ", len(even_properties)*2)
    else:
        print("Paratlan oldalon adtak el az utolso telket!")
        print("Az utolso telek szama: ", len(odd_properties)*2 - 1)


def feladat_4():
    print("4. feladat")
    previous_color = ""
    number = -1
    for property in odd_properties:
        datas = property.split(" ")
        current_color = datas[2]
        if(previous_color == current_color and current_color!= "#" and current_color!= ":" and previous_color!= "#" and previous_color!=":"):
            print("A szomszedossal egyezik a kerites szine: ", number)
            break
        number +=2
        previous_color = current_color
   
        
def feladat_5():
    print("5. feladat")
    color_1 = ""
    color_2 = ""
    colors =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Y',':','#']
    x = int(input("Adjon meg egy hazszamot!"))
    print(x)
    if x % 2 == 0:
        index = int(x/2-1)
        property = even_properties[index]
        print("A kerites allapota/szine: ",property.split(" ")[2])
        color_1 = even_properties[index - 1].split(" ")[2]
        color_2 = even_properties[index + 1].split(" ")[2]
      
        
    else:
        index = int(x/2)
        property = odd_properties[index]
        print("A kerites allapota/szine: ",property.split(" ")[2])
        color_1 = odd_properties[index - 1].split(" ")[2]
        color_2 = odd_properties[index + 1].split(" ")[2]
      

    colors.remove(color_1)
    colors.remove(color_2)
    print("Egy lehetseges festesi szin: ", random.choice(colors))

        
    
def feladat_6():
    print("6. feladat")
    output_file = open("utcakep.txt","w")
    for property in odd_properties:
        datas = property.split(" ")
        fence_color = datas[2]
        fence_length = int(datas[1])
        for i in range(0,fence_length):
            print(fence_color,end = "",file = output_file)
        ## itt is elakadtam a masodik reszevel


feladat_1()
feladat_2()
feladat_3()
feladat_4()
feladat_5()
feladat_6()
