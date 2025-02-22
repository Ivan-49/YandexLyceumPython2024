def translate(text):
    global translated_text
    glass = "аоиёеуыэюя,.?!-"
    glass += glass.upper()
    for i in glass:
        while i in text:
            text = text.replace(i, "")
    text = " ".join(text.split())
    translated_text = text
    return text


translated_text = None
translate(
    "Удивительный факт, но текст на языке НЕРАЗБОРЧИВО оказывается довольно просто читать. Достаточно небольшой тренировки - и вы сможете это делать."
)

print(translated_text)
