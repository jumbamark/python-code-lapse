"""
blank lines cause issues with doctest because they are used to delimit tests
test will fail if we literally left a blank line because it interprets it as the
end of the sample output
doctest will replace the actual blank lines with the same literal before performing the 
comparison
"""

def double_space(lines):
    """Prints a list of lines double-spaced

    >>> double_space(['Line one.', 'Line two.'])
    Line one.
    <BLANKLINE>
    Line two.
    <BLANKLINE>
    """
    for line in lines:
        print(line)
        print()
