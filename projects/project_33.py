import re

def is_alnum_or_space(c):
  return re.match(r'[a-zA-Z0-9 _]', c) is not None

sender = input()
message = input()

sender_invalid = sender.isdigit()

special_count = len(re.findall(r'[^a-zA-Z0-9 _]', message))

spam_exists = re.search(r'spam', message, re.IGNORECASE) is not None

content_invalid = special_count > len(message) / 2 and spam_exists

if sender_invalid and content_invalid:
    print("Fully Invalid")
elif sender_invalid:
    print("Invalid Sender")
elif content_invalid:
    print("Invalid Content")
else:
    print("Not Spam")