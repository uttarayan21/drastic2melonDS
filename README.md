## Drastic to MelonDS

This script will convert the dsv save from drastic emulator to a melonDS save file

### Usage

```bash
usage: dr2mds.py [-h] [-o OUTPUT] [-f] file

positional arguments:
  file                  The drastic save file

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Specify the output file
  -f, --force           Overwrite the output file if it exists
```

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

### How does this works ?

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

### How to calculate the save size

Run `wc -c file` in terminal to count the number of bytes in the file

```bash
wc -c Pokemon\ Black.dsv
```

which will output something like

```
524410 Pokemon Black.dsv
```

Now calculate log(524410)/log(2) which equates to 19.000335671081253  
Take its floor i.e. 19 and calculate the power of 2 to the number ie 2<sup>19</sup> which equates to 524288
The resulting number is the number of blocks to put in `dd count=` if you are manually making the save.
