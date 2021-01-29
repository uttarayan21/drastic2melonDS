## Drastic to MelonDS

This script will convert the dsv save from drastic emulator to a melonDS save file

### How to use

You need python 3 installed.  
Specify the input save file

```bash
./dr2mds.py "Pokemon Black.dsv"
```

This will make a "Pokemon Black.sav" file as output
You can also specify the output like

```bash
./dr2mds.py "Pokemon Black.dsv" -o "PKMN.sav"
```

### How this works ?

MelonDS determines the type of save using exact byte count in the save file

Which needs to be a power of 2 as mentioned [here](http://melonds.kuribo64.net/faq.php).  
In _Importing a savefile from another emulator_ part under _How to_ section

This script calculates the closest power of 2 to the save file and removes the padding.

### Other ways of doing this

This can be done manually by removing the padding using a hex editor.
Or using dd like this (on linux/macos)

```bash
dd if=Pokemon.dsv of=Pokemon.sav bs=1 count=524288
```

This will make a 4KiB EEPROM save from drastic to melonDS save.
