import cowsay
import sys
# from saying import hello
from saying import goodbye

# if len(sys.argv) == 2:
#     message = "hello, " + sys.argv[1]
#     cowsay.tux(message)
#     cowsacow(message)
#     cowsay.dragon(message)
# else:
#     print("Usage: python say.py [name]")


if len(sys.argv) == 2:
  goodbye(sys.argv[1])
