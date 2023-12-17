from PIL import Image, ImageDraw, ImageFont
import os
print("Генератор мемов запущен")
text_type=input("Введите 1, если нужен только нижний текст, и 2, если и верхний, и нижний:")
top_text=""
bottom_text=""
if text_type == "1":
    bottom_text = input("Введите нижний текст мема: ")
elif text_type == "2":
    top_text = input("Введите верхний текст мема: ")
    bottom_text = input("Введите нижний текст мема: ")
else:
    print("Данного варианта не существует!")
    quit()
memes = os.listdir("сигма пупсик")
for meme in memes:
    print(f"{memes.index(meme)}: {meme}")
try:
    index = int(input("Введите желаемый номер шаблона!"))
except:
    print("Неверный ввод!")
    quit()

if index < 0 or index > len(memes) - 1:
    print("Тaкого шаблона нет!")
    quit()


template = Image.open(f"сигма пупсик/{memes[index]}")


w,h = template.size




draw = ImageDraw.Draw(template)



font = ImageFont.truetype("impact.ttf", size=70)
b_box_top= draw.textbbox((0,0),top_text,font=font)
b_box_bot= draw.textbbox((0,0),bottom_text,font=font)
x_top = (w - b_box_top[2]) // 2

x_bot = (w - b_box_bot[2]) // 2
y_bot = h - b_box_bot[3] - 10

y_top=10






draw.text((x_top,y_top),top_text,font=font)
draw.text((x_bot,y_bot),bottom_text,font=font)
template.save("сигмапупус.png")


print(top_text)
print(bottom_text)
