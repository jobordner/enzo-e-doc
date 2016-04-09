#DOCUMENTS = using-enzo-p developing-with-cello
#DOCUMENTS = developing-with-cello
DOCUMENTS = pp16
#DOCUMENTS = 1509


current:pdf

all:
	$(MAKE) pdf-homework pdf-reference pdf-evaluation 
#DOCUMENTS = 1509-intro 1509-enzo
#DOCUMENTS = 1509-intro
#DOCUMENTS = 1509-using
#DOCUMENTS = 1509-devel
#DOCUMENTS = 1509 handout
#DOCUMENTS = 1509 1509-amr handout
#DOCUMENTS = 1509-intro
#DOCUMENTS = 1509 pdf-evaluation pdf-homework pdf-reference



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
