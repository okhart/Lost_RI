# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.

define e = Character('Эйлин', color="#c8ffc8")

define a = Character('Артем', color="#c8ffc8")

#define narrator = Character('', color="#ffffff")

define zaitsev = Character("Зайцев", color="#ff0000")

image white_room = im.Scale("images/bg/white_room.webp", 1920, 1080)


# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene white_room


    show narrator default
    with dissolve

    narrator "Привет, я Рассказчик"

    hide narrator default
    show narrator sitting:
        xalign 0.15 yalign 0.7    
    with dissolve

    python:
        import time
        time.sleep(1)
    
    show zaitsev:
        xalign 0.15 yalign 0.45
    with dissolve



    zaitsev "Сухарев, вы же помните про литсеминар на следующей неделе?"

    hide zaitsev

    show eileen
    with dissolve
    e "Кто это был?"
    hide eileen
    hide narrator sitting
    show narrator exhausted:
        zoom 0.6
        xalign 0.1 yalign 0.54
    narrator "Нам пизда..."

    menu:
        "What should I do?"

        "Drink coffee.":
            "I drink the coffee, and it's good to the last drop."

        "Drink tea.":
            $ drank_tea = True

            "I drink the tea, trying not to make a political statement as I do."

    "Genuflect."
    
    jump trash
label trash:
    return
