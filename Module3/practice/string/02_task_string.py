# Пользователь Василий очень часто злоупотребляет восклицательными знаками!
# Напишите программу, которая будет заменять восклицательные знаки на точки.
# Пример строки: «Вася самый умный! Вася лучше всех! И ждет его успех! Вот так!»

text = "Вася самый умный! Вася лучше всех! И ждет его успех! Вот так!"
text = text.replace('!', '.')
print(text)
