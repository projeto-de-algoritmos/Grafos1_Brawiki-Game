# from lxml import etree

# context = etree.iterparse('ptwiki-latest-pages-meta-current.xml', events=("start", "end"))
# for event, element in context:
#     if event == "end":
#         print(element.tag)
#         element.clear()

with open('wiki-topcats.txt', 'r') as arquivo:
    conteudo = arquivo.read()

print(conteudo)
