from htmlnode import *

def main():
    test_node = HTMLNode(props={"href": "https://www.twinleaf.town", "target": "my ass",})
    print(test_node.props_to_html())

main()