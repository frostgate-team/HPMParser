# HPMParser

This scripts are used to make a list of models each level of Amnesia: Rebirth (or ATDD) uses and put their filenames into the separate file.

## Usage

First of all, you have to put map directories into the **maps** directory.

The structure of files should look like this:

root directory
maps/
- mapname/
- - mapname.hpm*

**Note**, that if you are going to parse maps that are designed to be used on HPL3 (these are maps for Amnesia: Rebirth, SOMA), you should **not** create additional chapter directories

### Wrong!

root directory
maps/
- chapter01
- - mapname/
- - - mapname.hpm*

### Right!

root directory
maps/
- mapname/
- - mapname.hpm*

After you done with moving map files into maps/ directory, you should open up *run.bat* file, or type in the following commands:

```
mkdir out
mkdir maps
python getmaps.py
python main.py
python trim.py
```

Note, that required version of Python is 3!

After you have done all previous steps, **meshlist.txt** will be available in out/ directory. This file contains all model names those are used in the game.
