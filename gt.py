#!/usr/bin/python3
##################
#############
ver = '0.1' #
#############

###########
# Version #
###########
import sys
if '--version' in sys.argv:
	print(f'gt version: {ver}')
	exit(0)
###########

##############
# Debug Mode #
##############
if '--debug' in sys.argv:
	is_debug = True
	sys.argv.remove('--debug')
else:
	is_debug = False
##############


#############
# Help Menu #
#############
script_name = sys.argv[0]

if len(sys.argv) == 1:
	print(f'Usage:\n'
		  f' {script_name} {{destination}} {{text}}\n'
		  f' {script_name} {{source}} {{destination}} {{text}}\n'
		  f' {script_name} {{text}} {{destination}}\n'
		  f' {script_name} {{text}} {{destination}} {{source}}')
	exit(1)
#############

##################
# Debug function #
##################
if is_debug:
	import datetime
	def debug(message):
		print(f'{datetime.datetime.now()} ({ver}) {message}')
else:
	def debug(message):
		pass
##################


#################################
# Initialize googletrans plugin #
#################################
from googletrans import Translator
from googletrans import LANGUAGES as translator_languages
translator = Translator()
#################################


################################################
# Initialize and configure behaviour of script #
################################################
# gt dest text
# gt src dest text
# gt text dest
# gt text dest src

""" Initialize variables """
first = ""
second = ""
last = ""
penultimate = ""
source = ""
dest = ""
text = ""

first = sys.argv[1]
try:
	second = sys.argv[2]
	last = sys.argv[len(sys.argv)-1]
	penultimate = sys.argv[len(sys.argv)-2]
except:
	pass
""""""

""" Check for used arguments"""
if first in translator_languages:
	if second in translator_languages: # gt src dest text
		source = first
		dest = second
	else: # gt dest text
		dest = first
elif last in translator_languages:
	if penultimate in translator_languages: # gt text dest src
		source = last
		dest = penultimate
	else: # gt text dest
		dest = last
""""""

""" Remove unnecessary arguments from sys.argv array"""
if source is not "":
	sys.argv.remove(source)

if dest is not "":
	sys.argv.remove(dest)

sys.argv.remove(script_name)
""""""

""" Convert arguments to string """
for arg in sys.argv:
	text += f'{arg} '
""""""
################################################


debug(f'I will translate from: {source}, to: {dest} language')
debug(f'Text to translate: {text}')


################################################
# Translate {text} based on provided arguments #
################################################
if source and dest is not "":
	translated_text = translator.translate(text,src=source,dest=dest)
elif dest is not "":
	translated_text = translator.translate(text,dest=dest)
else:
	translated_text = translator.translate(text)

debug(f'Text translated: {translated_text.text}')
debug(f'GoogleTranslate language detection')
debug(f'From: {translated_text.src}, To: {translated_text.dest}')
################################################

###########################
# Display translated text #
###########################
print(translated_text.text)
###########################
