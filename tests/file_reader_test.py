# -*- coding: utf-8 -*-

import pytest

from film_script_formatter.file_reader import FileReader

class TestFileReader:

    def setup_class(self):
        ## Init FileReader
        self.fileReader = FileReader()

    def test_file_reader_with_invalid_type(self):
        with pytest.raises(TypeError):
            (FileReader()).read(11)

    def test_file_reader_with_None_value(self):
        with pytest.raises(ValueError):
            (FileReader()).read(None)

    def test_file_reader_with_empty_value(self):
        with pytest.raises(ValueError):
            (FileReader()).read('')
    
    def test_file_reader_decorator(self):
        #@FileReader.read
        #def jojo_rabbit_scritp_reader(filename):
        #    pass

        #jojo_rabbit_scritp_reader('jojo-rabbit-script-pdf.txt')
        def readOperation():
            print("hello")

        self.fileReader.read('jojo-rabbit-script-pdf.txt', readOperation)
        
