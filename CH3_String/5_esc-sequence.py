
# {\n} breaks line or #creates new line#
text="Amrit is good boy \nbut not a smart boy"
print(text)

# {\t} give space like Tab
text2="Amrit is good boy but not ta smart \tboy"
print(text2)


# {\ " \ "}   we can print "" in btween "" or \'\'
text3="Amrit is good boy but not a  \"smart\"  boy"
print(text3)


''' .............................................................................................................................................
 The top 3 are enough to understand the concept of sequence character
   '''


# \a - Bell sound (may beep)
text = "Amrit is good boy\a but not a smart boy"

# \b - Backspace (erases last character before it)
text = "Amrit is good bo\b\b\b\bBAD but not a smart boy"  # Changes "good bo" to "BAD"

# \f - Form feed (new page, not really visible in most consoles)
text = "Amrit is good boy\fbut not a smart boy"

# \r - Carriage return (returns to start of the line)
text = "Amrit is good boy but not\r a smart boy"  # Overwrites the beginning with " a smart boy"

# \v - Vertical tab (moves down, rarely used now)
text = "Amrit is good\vboy but not a smart boy"

# \\ - Backslash
text = "Amrit is good boy but not a smart\\boy"

# \' - Single quote
text = 'Amrit is good boy but not a smart boy\'s behavior'

# \0 - Null character (has no visible effect, ends string in C)
text = "Amrit is good boy\0 but not a smart boy"

# \x1b - Escape character (used in terminal control sequences)
text = "\x1b[31mAmrit is good boy but not a smart boy\x1b[0m"  # Makes the text red in supported terminals

# \N{name} - Unicode by name
text = "Amrit is good boy but not a smart boy \N{WHITE SMILING FACE}"

# \u03A9 - Unicode with 4 hex digits
text = "Amrit is good boy but not a smart boy \u03A9"  # Adds Ω at the end

# \U0001F600 - Unicode with 8 hex digits
text = "Amrit is good boy but not a smart boy \U0001F600"  # Adds 😀 at the end
