import pandas as pd
from Topic import Topic
from Topic_manager import Topic_manager

f = open("Data/datablender_comments.sql", "r")
lines = f.readlines()
f.close()

comments = []
for l in lines:
    if l[0] == "(":
        com = l.split("', ")[2]
        if com != " '":
            comments.append(com)

dfs = pd.read_excel("Data/ETUDE-25-06-20.xlsx", sheet_name = "TERMES")
categories = dfs.columns.tolist()

topics = []
for k in categories:
    wl = [x for x in dfs[k].values if str(x) != 'nan']
    topics.append(Topic(k, wl))

manager = Topic_manager(topics, discarded_words = ["le", "la", "les"])

for c in comments[:3]:
    print(c)
    scores, wp, wa = manager.get_scores(c)
    for i in range(len(scores)):
        if scores[i] > 0:
            print("{:<17}".format(manager.get_topic_list()[i] + ": "))
            print(str(scores[i]) + "     ")
            print(str(wp[i]) + "\n")
    print("Words Absent: ", wa)
    print("\n\n")

    manager.discard_list(["de", "du", "des"])
