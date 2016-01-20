FILES=index.html Cello-logo3.png cello.css

WEBSITE=/var/www/html/cello

upload:
	sudo chown www-data:www-data $(FILES)
	sudo cp -ai $(FILES) $(WEBSITE)
	sudo chown bordner:bordner $(FILES)
download:
	sudo cp -ai $(FILES) $(WEBSITE) 
	sudo chown bordner:bordner $(FILES)
