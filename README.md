## Description

Android R class generator based on public resources from decompiled APK with ApkTool

## Requestments

Requires installed **Python 3.6+**

## Usage

```
usage: rclass_generator.py [-h] [-i INPUT] [-o OUTPUT] [-p PACKNAME] [-c]

Android R class generator based on public resources from decompiled APK with ApkTool

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input public.xml file
  -o OUTPUT, --output OUTPUT
                        Output R.java class file
  -p PACKNAME, --packname PACKNAME
                        Output package name
  -c, --comments        Add comments with decimal resource ids
```