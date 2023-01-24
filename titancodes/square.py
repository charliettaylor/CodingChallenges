import time as t
import os
from datetime import datetime
import sys
import turtle

def draw_square(n: int):
  if n < 2:
    print('don\'t do that')
    return

  print('*', '#' * (n-2), '*', sep='')
  for _ in range(n-2):
    print('#' * n)
  print('*', '#' * (n-2), '*', sep='')


def progress_bar(time: int):
  for i in range(time+1):
    sys.stdout.write(u'\u001b[1000D')
    sys.stdout.write('x' * i)
    sys.stdout.write('0' * (time - i))
    t.sleep(1)
    sys.stdout.flush()

def clock():
  while True:
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    sys.stdout.write(u'\u001b[1000D')
    sys.stdout.write(current_time)
    t.sleep(1)
    sys.stdout.flush()

def illuminati():
  tu = turtle.Turtle()

  tu.forward(100)

illuminati()