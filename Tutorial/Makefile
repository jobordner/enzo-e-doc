

#DOCUMENTS = 1805-1-status
#DOCUMENTS = 1805-2-intro
DOCUMENTS = 1805-3-using
#DOCUMENTS =  1805-1-status 1805-2-intro 1805-3-using

#DOCUMENTS = cello-project
#DOCUMENTS = using-enzo-p
#DOCUMENTS = developing-with-cello

#DOCUMENTS = cello-project using-enzo-p developing-with-cello
#DOCUMENTS = enzo-p-cello
#DOCUMENTS = 1706

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
