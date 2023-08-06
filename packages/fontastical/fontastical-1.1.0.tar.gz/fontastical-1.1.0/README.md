# Fontastical
![1](https://fontastical.epiccodewizard.repl.co/1.png)

So, what do you do?

![2](https://fontastical.epiccodewizard.repl.co/2.png)

Fontastical uses special characters, that work in dumb terminals too!

# Classes:
```
serif.normal
serif.bold
serif.italic
serif.bold_italic

calligraphy.normal
calligraphy.bold

fraktur.normal
fraktur.bold

sans_serif.normal
sans_serif.bold
sans_serif.italic
sans_serif.bold_italic
```
Note: `serif.normal` is the normal font anywhere, so passing something to it will return itself.

# Stand alone functions:
```
overline
strikethrough
underline
spaced_underline
double_underline
monospace
double_struck
```
The function names are self explanatory. This library uses character maps. If a character isn't supported, the normal version of it will be returned.

# Full Support For English Letters, Partial Support For Numbers and Greek Letters, No Support For All Other Characters/Punctuation