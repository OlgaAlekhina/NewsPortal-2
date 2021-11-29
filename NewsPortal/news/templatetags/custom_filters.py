from django import template

register = template.Library()

@register.filter(name='censor')
def censor(text):
    stop_words = [['хуй', '..'], ['ебат', '...'], ['пизд', '...'], ['бляд', '...']] # и всё в таком духе
    
    ind = 0

	for stop in stop_words:
		while stop[0] in text:
			ind = (text.lower()).index(stop[0])
			text = text[0 : ind + 1] + stop[1] + text[(ind + len(stop[0])):]

	return text

    
