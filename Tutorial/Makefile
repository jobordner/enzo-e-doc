# DOCUMENTS = using-enzo-p developing-with-cello
DOCUMENTS = enzo-p-cello

current:pdf

all:
	$(MAKE) pdf-homework pdf-reference pdf-evaluation 

PAPER = `pwd | awk 'BEGIN{FS="/"}{print $$NF}'`
abstract = 'abstract'

#-----------------------------------------------------------------------
# BUILD
#-----------------------------------------------------------------------

.PHONY: ps
ps:   $(patsubst %,ps-%,$(DOCUMENTS))
ps-%:
	echo "PS $*"
	latex $*.tex
	latex $*.tex
	dvips $*.dvi

.PHONY: pdf
pdf:   $(patsubst %,pdf-%,$(DOCUMENTS))
pdf-%:
	echo "PDF $*"
	pdflatex -shell-escape $*.tex

#	pdflatex abstract.tex

#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
# CLEAN
#-----------------------------------------------------------------------

.PHONY: clean

clean: $(patsubst %,clean-%,$(DOCUMENTS))
	-@rm -f *~ *.aux \
	*.nav \
	*.out \
	*.pyg \
	*.snm \
	*.toc \
	*.vrb

clean-%:
	-@rm -rf  $*.bbl \
        $*.blg \
        $*.pdf \
        $*.dvi \
        $*.html \
        $*.log \
        $*.nav \
        $*.out \
        $*.ps \
        $*.snm \
        $*.toc

#-----------------------------------------------------------------------

.PHONY: distclean

distclean: clean
#	-@rm makefile # Must be last!
