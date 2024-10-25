def props_to_str(props: dict | None):
    if props:
        return f"{{ {', '.join([f'{k}: "{v}"' for k, v in props.items()])} }}"
    return ''


def create_node(label, props: dict | None = None):
    props_str = props_to_str(props)
    return f"CREATE (n:{label} {props_str}) RETURN n"



def read_node(node):
    ...


def read_nodes(self):
    ...


def update_node(node):
    ...


def delete_node(node):
    ...


# Edge
def create_edge(edge):
    ...


def read_edge(edge):
    ...


def read_edges(self):
    ...


def update_edge(edge):
    ...


def delete_edge(edge):
    ...
