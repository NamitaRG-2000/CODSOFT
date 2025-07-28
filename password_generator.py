import random
import string

print("=== Password Generator ===")

length = int(input("Enter desired password length: "))

all_chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(all_chars) for _ in range(length))

print("Generated password:", password)
