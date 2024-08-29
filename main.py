import sys
import os
import time

import tts


def main():
  while True:
    text = input("> ")
    tts.va_speak(text)
    if text == 'exit':
      break

if __name__ == '__main__':
  main()
