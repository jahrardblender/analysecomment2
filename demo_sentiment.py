from Sentiment_analyzer import Sentiment_analyzer
import numpy as np

sa = Sentiment_analyzer(threshold = 0.8)

f = open("Data/datablender_comments.sql", "r")
lines = f.readlines()
f.close()

comments = []
for l in lines:
    if l[0] == "(":
        com = l.split("', ")[2]
        if com != " '":
            comments.append(com)

print("\nResults:\n")
for k in np.random.randint(0, 200, 10):
    print(str(comments[k]))
    print()
    label, score = sa.predict(comments[k])
    print(str(label) + " /// " + str(score))
    print("\n ------------------------- \n")

sa.clean_session()
