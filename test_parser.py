from lark import Lark

def main():
    """
    Reads the Ren'py grammar, loads a sample .rpy file,
    and tries to parse it.
    """
    try:
        # Load the grammar from our .lark file.
        # The 'start' parameter tells Lark where to begin parsing.
        renpy_parser = Lark.open('renpy.lark', rel_to=__file__, parser='lalr', start='start')
        print("Grammar loaded successfully.")

        # Read the sample Ren'py code.
        with open('sample.rpy', 'r', encoding='utf-8') as f:
            sample_code = f.read()
        print(f"--- Parsing Sample Code ---\n{sample_code}\n-------------------------")

        # Parse the code.
        tree = renpy_parser.parse(sample_code)

        # Print the resulting Abstract Syntax Tree (AST) in a pretty format.
        print("Parsing successful!")
        print("\n--- Abstract Syntax Tree ---")
        print(tree.pretty())

    except Exception as e:
        print("An error occurred:")
        print(e)

if __name__ == "__main__":
    main()