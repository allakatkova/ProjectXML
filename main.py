import collections
import xml.etree.ElementTree as ET


def import_XML_from_file(file, max_length_word=6, top_words=10):
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(file, parser)
    root = tree.getroot()
    xml_title = root.findall("channel/item")
    description_words = []
    for xmli in xml_title:
        description = [word for word in xmli.find("description").text.split(' ') if len(word) > max_length_word]
        description_words.extend(description)
        counter_words = collections.Counter(description_words)
    print(counter_words.most_common(top_words))


if __name__ == '__main__':
    import_XML_from_file("newsafr.xml")
