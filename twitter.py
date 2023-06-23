sent = "Python is fun"
sent_list = sent.split(" ")
up_list = []

for word in sent_list:
    up_list.append(word.replace(word[0], word[0].upper()))

up_sent = "".join(up_list)

hashtag = "#"
hashtag += up_sent
print(hashtag)



# o/p = #PythonIsFun