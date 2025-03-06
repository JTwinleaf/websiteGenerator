from textnode import *
from htmlnode import *

def main():
    test = TextNode("Hello World!", TextType.BOLD)
    print(test.__repr__())
    test2 = LeafNode("p", "Hello World but in HTML")
    print(test2.__repr__())

if __name__ == "__main__":
    main()