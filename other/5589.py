import socket
from pprint import pprint as pp
import json

HOST = "137.151.29.179"  # The server's hostname or IP address
PORT = 5589  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  s.recv(4096)
  for j in range(50):
    print(f"Loop {j}")
    msg = s.recv(8192).decode('utf-8')
    diff = 0

    # parse word
    if j == 0:
      word = msg.split('\n')[0].strip()
    else:
      word = msg.split('\n')[1].split(':')[-1].strip()
    
    # parse list of guesses
    # pp(msg.split('\n'))
    if j == 0:
      guesses = eval(msg.split('\n')[1][17:].strip())
    else:
      guesses = eval(msg.split('\n')[2][17:].strip())


    for i in guesses:
      if i in word:
        diff += 1
    parts = len(guesses) - diff

    # pp(word)
    # pp(guesses)
    # pp(parts)

    men = msg.split('\n')[3:]
    parsed = []
    temp = ""
    # pp(men)
    for i in men:
      if "Which" in i or "Enter" in i:
        continue
      elif i[0].isdigit():
        parsed.append(temp)
        temp = ""
      else:
        temp += i
    parsed.append(temp)
    pp(parsed)

    scores = []
    for man in parsed:
      if man == '':
        continue
      body = man.count('|') - 6
      head = man.count('O')
      limbs = man.count('/') + man.count('\\')
      # print("score:", head, body, limbs)
      scores.append(body + head + limbs)
    
    scoreDict = {}
    for i, score in enumerate(scores):
      scoreDict[score] = i + 1
    
    pp(scoreDict)

    s.sendall(bytes(str(scoreDict[parts]) + '\n', encoding="utf-8"))
    # s.recv(4096)
    print("test", s.recv(4096).decode('utf-8'))
    # print("bruh", s.recv(4096))
  s.close()
