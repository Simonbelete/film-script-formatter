# -*- coding: utf-8 -*-

import re
import json

from film_script_formatter.file_reader import FileReader

class FilmScriptFormatter:

    def __init__(self, filename, encoding = 'utf-8'):
        self.filename = filename
        self.encoding = encoding
        self.SHOT_HEADING_MODIFIERS = ['INT.', 'EXT.', 'INT./EXT']
        self.ACTOR_KEY_WORDS = ['(MORE)', '(POINTING)', '(A SMILE)']
        self.ACTOR_EMPTY_IDENTIFIERS = ['...', '---', '***']
        self.ACTOR_MODIFIERS = ['CONT\'D', 'CONT', '' 'CONTINUED']

    def actors(self, indentation = 20, output = 'screenpaly_actors.json'):
        actor_regex = r'^([^\S\r\n]{%s,}|\t{3,6})([A-Z\'\.\(\)\s]{2,}\n)' % indentation
        actors_scenes = {}
        count = 0
        readFile = (FileReader(self.encoding)).read(self.filename)

       
        for line in readFile:
            match = re.match(actor_regex, line)
            ## Read the next line if actor is not found i.e no match found
            ## or remove empty lines or strings
            if match is None or not line.strip():
                continue
            ## Remove empty tabs and strings
            actor_name = line.strip()
            ## Remove empty new lines
            actor_name = (actor_name.split('\n'))[0]
            ## Check if string is a keyword
            ## eg. if MIGUEL (CONT'D) is found it considers it as one play from the previous actor i.e not counted
            if not actor_name in self.ACTOR_KEY_WORDS:
                ## Check if actor name is refrence eg. (TO SOMEONE)
                if actor_name.find("(") + actor_name.find(")") > 0:
                    continue
                ## Get the string found between parenthesis
                actor_modifier = actor_name[actor_name.find("(")+1:actor_name.find(")")]
                ## Append to `actors_scenes` if it is not a continued dialouge
                if not actor_modifier in self.ACTOR_MODIFIERS:
                    ## Since at this stage it is a new dialouge increment count
                    count += 1
                    ## Check if actor name key exists append if found or create new one
                    actor_name_wo_modifier, *b = actor_name.split('(')
                    ## Reclean the actor name
                    actor_name_wo_modifier = actor_name_wo_modifier.strip()
                    if actor_name_wo_modifier in actors_scenes: # and not actor_name_wo_modifier:
                        actors_scenes[actor_name_wo_modifier] = actors_scenes[actor_name_wo_modifier] + ',' + str(count)
                    else: #elif actor_name_wo_modifier:
                        actors_scenes[actor_name_wo_modifier] = str(count)
        
        ## Close resource
        readFile.close()
        ## Write to json file
        with open(output, 'w') as outputfile:
            json.dump(actors_scenes, outputfile, indent = 4)