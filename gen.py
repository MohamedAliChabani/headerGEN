def write_headers(header, config):
    """
    This function takes the headers listed in the headers key
    and writes them on top of file
    """
    header.write("#pragma once\n\n")
    for h in config.get("headers"):
        header.write(f"#include <{h}>\n")
    header.write("\n")

def write_attributes(header, attributes: dict):
    public_attr = attributes.get("public")
    private_attr = attributes.get("private")

    if public_attr != None:
        header.write("public:\n")
        for attr in public_attr:
            header.write(f"\t{attr};\n".expandtabs(4))

    if private_attr != None:
        header.write("private:\n")
        for attr in private_attr:
            header.write(f"\t{attr};\n".expandtabs(4))

def write_classes(header, config):
    classes = config.get("classes")

    for key, val in classes.items():
        class_name = "class " + key + " {\n"
        header.write(class_name)
        write_attributes(header, val.get("attributes"))

        header.write("}\n\n")
