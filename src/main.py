from textnode import TextNode, TextType

def main():
    dummyTextNode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    
    print(dummyTextNode)

if __name__ == "__main__":
    main()
