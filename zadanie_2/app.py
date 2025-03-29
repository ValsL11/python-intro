import re
import math
from datetime import datetime

def isEmailCorrect(email):
  pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
  return re.match(pattern, email) is not None

def calcCircleArea(r):
  if r <= 0:
    raise ValueError("Radius cannot be negative.")
  return math.pi * r ** 2

def sortArr(arr):
  return sorted(arr)

def convertDateFormat(date_str, input_format, output_format):
  date_obj = datetime.strptime(date_str, input_format)
  return date_obj.strftime(output_format)

def isPalindrome(text):
  cleanedText = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
  return cleanedText == cleanedText[::-1]
