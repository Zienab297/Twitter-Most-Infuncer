import csv
users = {}
followers = {}
suggestions = []
x= int(input())
thershold = 15
with open("./twitter.csv", 'r') as file:
  csvreader = csv.reader(file)
  #O(n)
  for row in csvreader:
      if row[1] not in users:
          users[row[1]] = [row[0]]
      else:
          users[row[1]].append(row[0])
      
if __name__ == '__main__':
    #complixity of O(n)
    for i in users.keys():
        followers[i] = len(users[i])
        
    Influence = dict(sorted(followers.items(), key = lambda x: x[1], reverse=True))
    #O(n)
    print("Most influncers are: " )
    for i in range(0, x):
        print( list(Influence)[i])
        
    # Bonus part complixity of O(n)
    user = input()
    if(user in users.keys()):
        #O(n)
        for i in users.keys():
            common_list = set(users[user]).intersection(users[i])
            if len(common_list) >= thershold:
                if i != user and i not in users[user]:
                    suggestions.append(i)
        print("firiend suggestions are: ")
        print(suggestions)
    else:
        print("user not available")
        
#overall complixity for most influence = O(2n) = O(n)
#overall complixity for suggestion = O(n)
#overall complixity = O(n)