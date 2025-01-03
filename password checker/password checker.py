import requests
import hashlib

def get_data_pawned_url(head_password):
  url = "https://api.pwnedpasswords.com/range/" + head_password
  resp = requests.get(url)

  if resp.ok != True:
    raise RuntimeError(f"The response from the url was {resp.ok}, cross-check your entries")
  return resp

def read_response(response):
  print(response.text)

def count_password_leaks(hashes_from_response, your_hashed_tail):
  hashes = (line.split(":") for line in hashes_from_response.text.splitlines())
  for hash, no_of_leaks in hashes:
  # print(hash, no_of_leaks)
    if hash == your_hashed_tail:
      return print(f"Password seems to have leaked {no_of_leaks} times")
  return 0

def check_password(your_password):
  # hash password first
  byte_object = your_password.encode() # hash fxns require byte-like objects not plain string, hence the need to encode. Default is encoding ="utf-8". you can try ascii or utf-16 as well
  # print(byte_object) optional

  hashed_password = hashlib.sha1(byte_object).hexdigest().upper() # convert to uppercase to match case used by pwned

  head_password, tail_password = hashed_password[:5], hashed_password[5:] # the pwned api requires just the first 5 characters of the hashed password to run its checks
  # print(hashed_password)
  # print(head_password, body_password)

  response = get_data_pawned_url(head_password) # 2nd fxn call

  # all_hashes_from_response = read_response(response) #3rd fxn call (optional to view the text from the response)

  return count_password_leaks(response, tail_password)

check_password("QWERTY")