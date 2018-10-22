all: intro containers vc ci doc

intro:
	pdflatex 00-Intro.tex

containers:
	pdflatex 01-containers.tex
vc:
	pdflatex 02-Version-Control.tex
ci:
	pdflatex 03-CI-and-testing.tex

doc:
	pdflatex 04-Documenting.tex

clean: 
	rm *.aux
	rm *.log
	rm *.nav
	rm *.out
	rm *.snm
	rm *.toc
	rm *.vrb
	rm *~
