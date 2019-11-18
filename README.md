# BulkFileRename

Run *Main.py* file.

The app is based on **argparse** library and **re** module.


usage: **Bulk File Rename [-h] [-path PATH]
                        (-lowercase | -uppercase | -convention CONVENTION)
                        [-ext EXT]**

This app enables you to bulk rename the files.

optional arguments:

  **-h, --help**            show this help message and exit
  
  **-path PATH**            Your directory full path, if skipped, will use currect
                        directory
                        
  **-lowercase**            This option will change files casing to lowercase
  
  **-uppercase**            This option will change files casing to uppercase
  
  **-convention CONVENTION**
  
                        This option will apply specific convention to files eg.
                        "File000" will name files in the following manner:
                        File001, File002... Please note that the 000 will be
                        used as starting point and it can be used wherever in
                        the name.
                        
  **-ext EXT**              This option will narrow group of files,to those
                        matching convention. For convention,use extension eg.
                        ".txt", ".xlsx"
