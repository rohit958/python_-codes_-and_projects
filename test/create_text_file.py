import os
import datetime

global text
text = """First of all I've no idea why I've been requested this answer. Anyways. 
 Bal Narendra is a comic anthology extolling the virtues and inherent leadership qualities of Narendra Modi.
  Now, one may be interested in verifying whether the anecdotes are true; and one can't because the stories are too abstract to fact check; I'll just advise to read and determine by yourself. I think it's a clever piece of propaganda aimed at a very specific demographic - gullible citizens. The stories themselves are a papparazical take on the iconic leader, who has nowadays been answering critical issues like how to consume mangoes, his sleeping habits and stress management.
 I'll just wrap up by saying, Modi is cultivating support by the masses.
  He's very good at it. And he's playing the long term game.
   So if you think his antics from his comics are a topic to be discussed in election season, thanks but no thanks."""


def create_text_file(text_str):
    try:
        with open("D:\git\python_-codes_-and_projects\sample_text_files\File1.txt", "w") as file:
            file.write(text_str)
            file.close()
        return "file created successfully"
    except IOError as e:
        return e


if __name__ == '__main__':
    response = create_text_file(text)
    print(response)
