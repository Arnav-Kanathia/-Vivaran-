from deep_translator import GoogleTranslator
from summarizer import textrank

with open('HindiText', 'r', encoding='utf-8') as f:
    hinText = f.read()

translator = GoogleTranslator(source='hi', target='en', timeout=10)
engText = translator.translate(hinText)

engSum = textrank(engText)

with open('HindiSum', 'w', encoding='utf-8') as f:
    for sentence in engSum:
        hinSent = GoogleTranslator(source='en', target='hi').translate(sentence)
        f.write(hinSent)

print('Summary generated successfully!')
