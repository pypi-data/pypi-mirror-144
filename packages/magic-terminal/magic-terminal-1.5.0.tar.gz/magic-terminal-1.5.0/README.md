# :art: magic-terminal
A fun way to customize your terminal with colors, styles etc...

### Install
```cmd
py -m pip install -U magic-terminal

:: for latest/unstable
py -m pip install -U git+https://github.com/Marseel-E/magic-terminal
```
### Import
```py
from MagicTerminal import Magic, Style, Color, Highlight
```

### Magic.styalize()
```py
print(Magic.styalize("Some fancy text", Style.default, Color.green, Highlight.red))

# >>> Some fancy text
```

### Magic.print()
```py
Magic.print("Some fancy text", Style.default, Color.green, Highlight.red, True, True)

# >>> 
# >>> Some fancy text
# >>> 
```

### Magic.typed_print()
```py
Magic.typed_print(420)

# >>> 420
```

### 📜 [License](LICENSE)
