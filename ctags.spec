Summary:	Exuberant ctags -- C cross-reference tool
Summary(de):	Exuberant ctags - C-Cross-Reference-Tool 
Summary(fr):	ctags exub�rant
Summary(pl):	ctags - generator list odwo�a�
Summary(tr):	C dili i�in �apraz-ba�vuru (cross-reference) arac�
Name:		ctags
Version:	3.0.3
Release:	3
Copyright:	GPL
Group:		Development/Tools
Group(pl):	Programowanie/Narz�dzia
URL:		http://darren.hiebert.com/ctags
Source:		ftp://ftp.revnet.com/pub/ctags/archives/%{name}-%{version}.tar.gz
Buildroot:	/tmp/%{name}-%{version}-root

%description
A better ctags which generates tags for all possible tag types: macro
definitions, enumerated values (values inside enum{...}), function and
method definitions, enum/struct/union tags, external function prototypes
(optional), typedefs, and variable declarations. It is far less easily
fooled by code containing #if preprocessor conditional constructs, using a
conditional path selection algorithm to resolve complicated choices, and a
fall-back algorithm when this one fails. Can also be used to print out a
list of selected objects found in source files.

%description -l de
Ein verbessertes ctags, das tags f�r alle m�glichen tag-Typen generiert:
Makrodefinitionen, aufgez�hlte Werte (Werte in enum{...}), Funktions- und
Methodendefinitionen, enum/struct/union-tags, externe Funktionsprototypen
(wahlweise), typedefs und variable Deklarationen. Es l��t sich weit weniger
gut durch Code t�uschen, der #if-Pr�prozessor-Bedingungen enth�lt, dank
eines konditionalen Pfadauswahlalgorithmus, der komplizierte Entscheidungen
trifft, und eines Ausweiche-Algorithmus, der ins Spiel kommt, wenn der erste
dem Problem nicht gewachsen ist.  Kann auch benutzt werden, um eine Liste
ausgew�hlter Objekte, die in Quelldateien gefunden wurden, auszudrucken.

%description -l fr
un ctags am�lior� g�n�rant des tags pour tous les types de tags possibles :
d�finitions de macros, valeurs �num�r�es (valeurs dans enum{...}),
d�finitions de fonctions et de m�thodes, enum/struct/union tags, prototypes
de fonctions externes (optionnel), typedefs, et d�clarations de variables.
Peut aussi �tre utilis� pour afficher une liste des objets choisis trouv�s
dans les fichiers source.

%description -l pl
Generator tabeli odwo�a� dla: makr, zmiennych, funkcji i procedur, definicji
typ�w, metod (C++) itp. U�ywany do generacji listy wyspecyfikowanych
obiekt�w znalezionych w plikach �r�d�owych. Tablica owych odwo�a� mo�e by�
wykorzystywana przez wiekszos� standardowych edytor�w tekstu (vim, joe,
emacs), do przemieszczania si� w �r�d�ach mi�dzy deklaracj� i u�yciem danego
symbolu.

%description -l tr
Olabilecek her t�rl� etiket �e�itleri - makro tan�mlamalar�, say�l�
(enumerated) de�erler, fonksiyon ve y�ntem (method) tan�mlamalar�, tip ve
de�i�ken tan�mlar� - i�in etiketler �retir. Kaynak kodlar�nda bulunan,
se�ilmi� nesnelerin listesinin ��kt�s�n� yaz�c�dan almak i�in de
kullan�labilir.

%prep
%setup -q

%build
CFLAGS=$RPM_OPT_FLAGS LDFLAGS="-s" \
./configure \
	--prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT/usr install

rm -f $RPM_BUILD_ROOT/usr/man/man1/etags.1
echo ".so ctags.1" > $RPM_BUILD_ROOT/usr/man/man1/etags.1

strip $RPM_BUILD_ROOT/usr/bin/*

gzip -9nf $RPM_BUILD_ROOT/usr/man/man1/* \
	 FAQ NEWS QUOTES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) /usr/bin/*
/usr/man/man1/*

%changelog
* Mon Apr 12 1999 Micha� Kuratczyk <kura@pld.org.pl>
  [3.0.3-3]
- added gzipping docimentation
- removed man group grom man pages
- added stripping binaries
- added %defattr(644,root,root,755)

* Tue Jan 26 1999 Micha� Kuratczyk <kura@pld.org.pl>
  [3.0-2]
- changed Group to /Development/Tools
- added Group(pl)

* Fri Dec 11 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.0-1]
- added gzipping man pages,
- added using LDFLAGS="-s" to ./configure enviroment.
- etags(1) man page is now maked as nroff include to ctags(1) instead
  making sym link to ctags.1 (this allow compress man pages).

* Wed Aug 26 1998 Wojciech "Sas" Ci�ciwa <cieciwa@zarz.agh.edu.pl>
  [2.3.1-1]
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added URL,
- changed base Source URL to ftp://ftp.revnet.com/pub/ctags/,
- added pl translation.
 
* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 2.0.3

* Mon Nov 03 1997 Michael K. Johnson <johnsonm@redhat.com>
- removed etags.  Emacs provides its own; and needs to support
  more than just C.

* Thu Oct 23 1997 Donnie Barnes <djb@redhat.com>
- updated from 1.5 to 1.6

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
