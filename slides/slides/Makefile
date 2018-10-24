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
	rm -rf *.aux
	rm -rf *.log
	rm -rf *.nav
	rm -rf *.out
	rm -rf *.snm
	rm -rf *.toc
	rm -rf *.vrb
	rm -rf *~
	rm -rf *.synctex.gz
	rm -rf *.fls
	rm -rf *fdb_latexmk