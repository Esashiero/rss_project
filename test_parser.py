import sys
from lark import Lark, Transformer, Indenter

# --- New Indenter Class ---
# This class tells Lark how to handle indentation.
# It will be passed to the Lark parser.
class RenpyIndenter(Indenter):
    NL_type = '_NEWLINE'
    OPEN_PAREN_types = ['LPAR', 'LSQB', 'LBRACE']
    CLOSE_PAREN_types = ['RPAR', 'RSQB', 'RBRACE']
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 4 # Ren'py typically uses 4-space indents.

def main():
    """
    Reads the Ren'py grammar, loads a sample .rpy file,
    and tries to parse it.
    """
    try:
        # Load the grammar from our .lark file.
        # We now pass our custom indenter in the 'postlex' argument.
        renpy_parser = Lark.open(
            'renpy.lark',
            rel_to=__file__,
            parser='lalr',
            start='start',
            postlex=RenpyIndenter() # <--- THIS IS THE NEW LINE
        )
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
        print(e, file=sys.stderr) # Print errors to stderr for clarity

if __name__ == "__main__":
    main()