from yattag import Doc

doc, tag, text = Doc().tagtext()

def add_tags(tags,description):
    with tag(tags):
        text(description)

add_tags('i','python')
add_tags('b', 'python tutorial')
print(doc.getvalue())