# Translations template
POT_FILE=locale/pyschool.pot
# Template files
TEMPLATES=templates/*.html
# Target files
TARGET_FILES=index.html index.es.html
# MAIN CSS FILE
CSSFILE=css/index.css

all: $(TARGET_FILES)

clean:
	rm -f `find -name messages.mo`
	rm -f $(TARGET_FILES)
	rm -f $(CSSFILE)
	rm -f $(CSSFILE).map
	rm -f index.en.html

# SASS
$(CSSFILE): styles/*.scss
	sassc styles/main.scss $@ -m -t compressed

# Translations template
locale/pyschool.pot: $(TEMPLATES)
	python scripts/check.py index.html
	pybabel extract -F babel.cfg -o $(POT_FILE) $(TEMPLATES)

# (Source) translations
locale/%/LC_MESSAGES/messages.po: $(POT_FILE)
	pybabel update -i $(POT_FILE) -l $* -d locale/

# (Compiled) translations
.PRECIOUS: locale/%/LC_MESSAGES/messages.mo
locale/%/LC_MESSAGES/messages.mo: locale/%/LC_MESSAGES/messages.po
	pybabel compile -d locale -f --locale $*


# Localized target files
index.%.html: $(TEMPLATES) $(CSSFILE) locale/%/LC_MESSAGES/messages.mo
	python scripts/render.py index.html --language $* --output index.$*.html

# English target file
index.html: index.en.html
	cp $< $@

# Used for local development along with livereload
watch:
	python -m http.server 8000 &
	livereload . -w 2 &
	while true; do \
		make all; \
		inotifywait -qre close_write locale templates styles; \
	done
