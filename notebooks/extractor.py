import javalang
import sys

def main(path: str):
    with open(path, "r") as f:
        source = f.read()

    myast = javalang.parse.parse(source)

    #print(javalang.ast.walk_tree(myast))
    for path, node in javalang.ast.walk_tree(myast):
        """
        if isinstance(node, javalang.tree.PackageDeclaration):
            print("name:", node.name)
            print("document:", type(node.documentation))
            print("modifiers:", node.modifiers)
            print("annotations:", node.annotations)
        
        if isinstance(node, javalang.tree.Import):
            print("path:", node.path)
            print("static:", node.static)
            print("wildcard:", node.wildcard)
        
        if isinstance(node, javalang.tree.ClassDeclaration):
            print("name:", node.name)
            print("modifiers:", node.modifiers)
            print("annotations:", node.annotations)
            print("type_parameters:", node.type_parameters)
            print("extends:", node.extends)
            print("implements:", node.implements)
            print("document:", len(node.documentation))
        """ 
        if isinstance(node, javalang.tree.FieldDeclaration):
            print("type:", node.type)
            print("modifier:", node.modifiers)
            print("annotations:", node.annotations)
            print("declarator:", node.declarators)

if __name__ == "__main__":
    main(sys.argv[1])
