import cowsay
import sys
from saying import hello

# if len(sys.argv) == 2:
#     message = "hello, " + sys.argv[1]
#     cowsay.tux(message)
#     cowsay.cow(message)
#     cowsay.dragon(message)
# else:
#     print("Usage: python say.py [name]")


if len(sys.argv) == 2:
  hello(sys.argv[1])
