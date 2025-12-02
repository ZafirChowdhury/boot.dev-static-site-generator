import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()


    def test_props_to_html(self):
        test_props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        
        node = HTMLNode(props=test_props)
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')


    def test_props_to_html_empty(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")


if __name__ == "__main__":
    unittest.main()
