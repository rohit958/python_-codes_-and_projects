txt1='hello world'
txt2='I am boy'

def word_reversal(text):
  words = text.strip().split()
  new_txt = ''
  for i in range(len(words)-1, -1, -1):
    new_txt += words[i]
    if i != 0:
      new_txt += ' '
  return new_txt

print(word_reversal(txt1))
print(word_reversal(txt2))