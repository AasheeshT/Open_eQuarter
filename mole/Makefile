#***************************************************************************
# OpenEQuarterMain
#
# The plugin automates the setup for investigating an area.
#                             -------------------
#        begin                : 2014-10-07
#        copyright            : (C) 2014 by Kim Gülle / UdK-Berlin
#        email                : kimonline@example.com
# ***************************************************************************/
#
#/***************************************************************************
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU General Public License as published by  *
# *   the Free Software Foundation; either version 2 of the License, or     *
# *   (at your option) any later version.                                   *
# *                                                                         *
# ***************************************************************************/

# CONFIGURATION
PLUGIN_UPLOAD = $(CURDIR)/plugin_upload.py

QGISDIR=.qgis2

# Makefile for a PyQGIS plugin

# translation
SOURCES = open_equarter_main.py __init__.py
#TRANSLATIONS = i18n/OpenEQuarterMain_en.ts

# global

PLUGINNAME = Open eQuarter

PY_FILES = open_equarter_main.py __init__.py

EXTRAS = icons/sources.png icons/magnifying_glass.png icons/gearwheel.png icons/OeQ_plugin_icon.png icons/OeQ_logo_footer.png icons/checkmark.png icons/semiopenmark.png icons/openmark.png icons/arrow_right.png icons/scissor.png metadata.txt

PACKAGE_PREFIX = view/

UI_FILES = ui_information_source_dialog.py ui_project_does_not_exist_dialog.py ui_request_wms_url_dialog.py ui_modular_dialog.py ui_modular_info_dialog.py ui_main_process_dock.py ui_project_settings_form.py ui_color_picker_dialog.py ui_estimated_energy_demand_dialog.py

RESOURCE_FILES = resources_rc.py

HELP = help/build/html

default: compile

# Compile depends on all ui- and resource-files
compile: $(UI_FILES) $(RESOURCE_FILES)

%_rc.py : $(PACKAGE_PREFIX)%.qrc
	pyrcc4 -o $(PACKAGE_PREFIX)$*_rc.py  $<

%.py : $(PACKAGE_PREFIX)%.ui
	pyuic4 -o $(PACKAGE_PREFIX)$@ $<

%.qm : $(PACKAGE_PREFIX)%.ts
	lrelease $<

# The deploy  target only works on unix like operating system where
# the Python plugin directory is located at:
# $HOME/$(QGISDIR)/python/plugins
deploy: compile doc transcompile
	mkdir -p $(HOME)/$(QGISDIR)/python/plugins/$(PLUGINNAME)
	cp -vf $(PY_FILES) $(HOME)/$(QGISDIR)/python/plugins/$(PLUGINNAME)
	cp -vf $(UI_FILES) $(HOME)/$(QGISDIR)/python/plugins/$(PLUGINNAME)
	cp -vf $(RESOURCE_FILES) $(HOME)/$(QGISDIR)/python/plugins/$(PLUGINNAME)
	cp -vf $(EXTRAS) $(HOME)/$(QGISDIR)/python/plugins/$(PLUGINNAME)
	cp -vfr i18n $(HOME)/$(QGISDIR)/python/plugins/$(PLUGINNAME)
	cp -vfr $(HELP) $(HOME)/$(QGISDIR)/python/plugins/$(PLUGINNAME)/help

# The dclean target removes compiled python files from plugin directory
# also delets any .svn entry
dclean:
	find $(HOME)/$(QGISDIR)/python/plugins/$(PLUGINNAME) -iname "*.pyc" -delete
	find $(HOME)/$(QGISDIR)/python/plugins/$(PLUGINNAME) -iname ".svn" -prune -exec rm -Rf {} \;

# The derase deletes deployed plugin
derase:
	rm -Rf $(HOME)/$(QGISDIR)/python/plugins/$(PLUGINNAME)

# The zip target deploys the plugin and creates a zip file with the deployed
# content. You can then upload the zip file on http://plugins.qgis.org
zip: deploy dclean
	rm -f $(PLUGINNAME).zip
	cd $(HOME)/$(QGISDIR)/python/plugins; zip -9r $(CURDIR)/$(PLUGINNAME).zip $(PLUGINNAME)

# Create a zip package of the plugin named $(PLUGINNAME).zip.
# This requires use of git (your plugin development directory must be a
# git repository).
# To use, pass a valid commit or tag as follows:
#   make package VERSION=Version_0.3.2
package: compile
		rm -f $(PLUGINNAME).zip
		git archive --prefix=$(PLUGINNAME)/ -o $(PLUGINNAME).zip $(VERSION)
		echo "Created package: $(PLUGINNAME).zip"

upload: zip
	$(PLUGIN_UPLOAD) $(PLUGINNAME).zip

# transup
# update .ts translation files
transup:
	pylupdate4 Makefile

# transcompile
# compile translation files into .qm binary format
transcompile: $(TRANSLATIONS:.ts=.qm)

# transclean
# deletes all .qm files
transclean:
	rm -f i18n/*.qm

clean:
	rm $(UI_FILES) $(RESOURCE_FILES)

# build documentation with sphinx
doc:
	cd help; make html
