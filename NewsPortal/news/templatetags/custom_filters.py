from django import template

register = template.Library()

@register.filter(name='censor')
def censor(text):
    stop_words = ['хуй', 'Хуй', 'хуе', 'Хуе', 'пизд', 'Пизд', 'бля', 'Бля']  # и всё в таком духе
    words = text.split()

    for stop_word in stop_words:
        words = list(map(lambda x: x.replace(stop_word, '...'), words))

    return ' '.join(words)