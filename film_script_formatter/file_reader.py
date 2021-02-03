# -*- coding: utf-8 -*-

class FileReader:
    """FileReader class.

    ...

    Attributes
    ----------
    encoding: string('utf-8', 'ASCII')
        File's Encoding type

    filename: string 
        Absolute or relative file name with file's extension.

    file: FileObject
        Holds a file object, also called a handle

    """
    
    def __init__(self, encoding = 'utf-8'):
        self.encoding = encoding
        self.filename = None
        self.file = None

    def read(self, filename):
        """File reader func.

        Parameters:
        ----------
            filename string: Absolute or relative file name with file's extension.

        Returns:
        -------
            File
        """
        ## Check for if filename is not empty
        if not filename:
            raise ValueError('Error: filename cannot be empty')

        ## `filename` must be a string type
        if not isinstance(filename, str):
            raise TypeError('Error: filename must be a string type, given %s' % type(filename))

        ## TODO: For insuring the file closed approprately `with` statement is used
        ##       All file realted reading operations are executed using python decorator operator `@`
        ## Use python built-in `open` function to open a file,
        ## with the default read `r` parameter.
        self.file = open(filename, encoding = self.encoding)

        return self.file

    def close():
        self.file.close()