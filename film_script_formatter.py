import re

class FilmScriptFormatter:

    def __init__(self, filename, encoding = 'utf-8'):
        self.filename = filename
        self.encoding = encoding
        self.SHOT_HEADING_MODIFIERS = ['INT.', 'EXT.', 'INT./EXT']
        self.ACTOR_KEY_WORDS = ['(MORE)', '(POINTING)', '(A SMILE)']
        self.ACTOR_EMPTY_IDENTIFIERS = ['...', '---', '***']
        self.ACTOR_MODIFIERS = ['CONT\'D', 'CONT', '' 'CONTINUED']

    def actors(self, indentation = 16):
        actor_regex = r'^([^\S\r\n]{%s,}|\t{3,6})([A-Z\'\.\(\)\s]{2,}\n)' % indentation
        actors_scenes = {}
        count = 0

        with open(self.filename) as file:
            for line in file:
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
                if not actor_name in self.ACTOR_KEY_WORDS:
                    print(actor_name)
                    ## Get the string found between parenthesis
                    actor_modifier = actor_name[actor_name.find("(")+1:actor_name.find(")")]
                    ## Append to `actors_scenes` if it is not a continued dialouge
                    if not actor_modifier in self.ACTOR_MODIFIERS:
                        ## Since at this stage it is a new dialouge increment count
                        count += 1
                        ## Check if actor name key exists append if found or create new one
                        actor_name_wo_modifier, *b = actor_name.split('(')
                        if actor_name_wo_modifier in actors_scenes:
                            actors_scenes[actor_name_wo_modifier] = actors_scenes[actor_name_wo_modifier] + ',' + str(count)
                        else:
                            actors_scenes[actor_name_wo_modifier] = str(count)

        print(actors_scenes)