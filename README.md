## Drastic to MelonDS

This script will convert the dsv save from drastic emulator to a melonDS save file

How this works ?

MelonDS determines save type using exact byte count in the save file
Which needs to be a power of 2 as mentioned [here](http://melonds.kuribo64.net/faq.php).
This script calculates the closest power of 2 to the save file and removes the padding

This can be easily done manually by removing the padding using a hex editor.
Or using dd like this

```bash
dd if=Pokemon.dsv of=Pokemon.sav bs=1 count=524288
```

This will make a 4KiB EEPROM save from drastic to melonDS save.

I will add argparse later.
