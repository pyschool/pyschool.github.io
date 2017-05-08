# Translations template
POT_FILE=locale/pyschool.pot
# Template files
TEMPLATES=templates/*.html
# Target files
TARGET_FILES=index.html index.es.html

all: $(TARGET_FILES)

clean:
	rm -f `find -name messages.mo`
	rm -f $(TARGET_FILES)

# Translations template
locale/pyschool.pot: $(TEMPLATES)
	pybabel extract -F babel.cfg -o $(POT_FILE) $(TEMPLATES)

# (Source) translations
locale/%/LC_MESSAGES/messages.po: $(POT_FILE)
	pybabel update -i $(POT_FILE) -l $* -d locale/

# (Compiled) translations
locale/%/LC_MESSAGES/messages.mo: locale/%/LC_MESSAGES/messages.po
	pybabel compile -d locale -f --locale $*

# Localized target files
index.%.html: $(TEMPLATES) locale/%/LC_MESSAGES/messages.mo
	python scripts/render.py index.html --language $* > index.$*.html

# English target file
index.html: index.en.html
	cp index.en.html index.html
