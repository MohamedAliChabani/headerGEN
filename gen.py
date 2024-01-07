def write_system_headers(header, config, system_headers):
    if (system_headers == None):
        return

    for h in config.get("system_headers"):
        header.write(f"#include <{h}>\n")

    header.write("\n");

def write_project_headers(header, config, project_headers):
    if (project_headers == None):
        return

    for h in config.get("project_headers"):
        header.write(f'#include "{h}"\n')

    header.write("\n")

def write_headers(header, config):
    """
    This function takes the headers listed in the headers key
    and writes them on top of file
    """
    header.write("#pragma once\n\n")

    system_headers = config.get("system_headers")
    write_system_headers(header, config, system_headers)

    project_headers = config.get("project_headers")
    write_project_headers(header, config, project_headers)


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


def write_getters(header, private_attr):
    for attr in private_attr:
        # Parse the type and identifier of each attribute
        type, identifier = attr.split(" ")[0], attr.split(" ")[1]

        getter_function = f"\t {type} get_{identifier}() " + "{return " + identifier + ";}\n"
        header.write(getter_function.expandtabs(4))

def write_setters(header, private_attr):
    for attr in private_attr:
        # Parse the type and identifier of each attribute
        type, identifier = attr.split(" ")[0], attr.split(" ")[1]

        setter_function = f"\t void set_{identifier}({type} {identifier}) " + \
            "{this->" + identifier + f" = {identifier}" + ";}\n"
        header.write(setter_function.expandtabs(4))

def write_getters_setters(header, getters_setters, attributes):
    private_attr = attributes.get("private")
    if (getters_setters == None or private_attr == None):
        return

    header.write("public:\n")
    write_getters(header, private_attr)
    write_setters(header, private_attr)

def write_classes(header, config):
    classes = config.get("classes")

    for key, val in classes.items():
        # Writing the name of the class
        class_name = "class " + key + " {\n"
        header.write(class_name)

        # Writing the body of the class
        attributes = val.get("attributes")
        write_attributes(header, attributes)

        getters_setters = val.get("getters_setters")
        write_getters_setters(header, getters_setters, attributes)

        header.write("};\n\n")
