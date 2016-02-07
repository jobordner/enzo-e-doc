FILES=index.html Cello-logo3.png cello.css 1602-si2.pdf ../Tutorial/developing-with-cello.pdf  ../Tutorial/using-enzo-p.pdf

WEBSITE=/var/www/html/cello

upload:
	sudo chown www-data:www-data $(FILES)
	sudo cp -ai $(FILES) $(WEBSITE)
	sudo chown bordner:bordner $(FILES)
download:
	sudo cp -ai $(FILES) $(WEBSITE) 
	sudo chown bordner:bordner $(FILES)
