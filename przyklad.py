print('Hello, Django girls!')
if 3 > 2:
    if 3 > 2:
        print('To działa')
        if 5 > 2:
            print('5 jest jednak większe od 2')
        else:
            print('5 nie jest większe od 2')
        name = 'Sonja'
        if name == "Gosia":
            print('Hej Gosia!')
        elif name == 'Sonja':
            print('Hej Sonja!')
        else:
            print('Hej anonimie!')
        volume = 57
        if volume < 20:
            print("It's kinda quiet.")
        elif 20 <= volume <40:
            print("it's nice for background music")
        else:
            print("My ears are hurting! :(")
        # Change the volume if it's too loud or tooquiet
        if volume < 20 or volume > 80:
            volume = 50
            print("That's better!'")
        def hi():
            print("Hej")
            print("Jak się masz?")


def hi():
    print("podaj imie")
    imie = input()
    if imie == "Ola":
        print("Hej Ola!")
    elif imie == "Sonja":
        print("Hej Sonja!")
    else:
        print("Hej " + imie)


#hi("Ola")
#hi("Ania")
#hi()

def hi(imie):
    print('Hej ' + imie + '!')

dziewczyny = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Ty']
for imie in dziewczyny:
    hi(imie)
    print('Kolejna dziewczyna')

for i in range(1, 6):
    print(i)




