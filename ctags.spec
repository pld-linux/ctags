Summary:	Exuberant ctags -- C cross-reference tool
Summary(de):	Exuberant ctags - C-Cross-Reference-Tool 
Summary(fr):	ctags exubérant
Summary(pl):	ctags - generator list odwo³añ
Summary(tr):	C dili için çapraz-baþvuru (cross-reference) aracý
Name:		ctags
Version:	3.2.1
Release:	1
Copyright:	GPL
Group:		Development/Tools
Group(pl):	Programowanie/Narzêdzia
Source:		ftp://ftp.revnet.com/pub/ctags/archives/%{name}-%{version}.tar.gz
patch0:		ctags-glibc.patch
URL:		http://darren.hiebert.com/ctags/
Buildroot:	/tmp/%{name}-%{version}-root

%description
Ctags generates an index (or tag) file of C language objects found in C
source and header files.  The index makes it easy for text editors or other
utilities to locate the indexed items.  Ctags can also generate a cross
reference file which lists information about the various objects found in a
set of C language files in human readable form.  Exuberant Ctags improves on
ctags because it can find all types of C language tags, including macro
definitions, enumerated values (values inside enum{...}), function and
method definitions, enum/struct/union tags, external function prototypes,
typedef names and variable declarations.  Exuberant Ctags is far less likely
to be fooled by code containing #if preprocessor conditional constructs than
ctags.  Exuberant ctags supports output of emacs style TAGS files and can be
used to print out a list of selected objects found in source files.
                                                                                                              
Install ctags if you are going to use your system for C programming.                                          

%description -l de
Ein verbessertes ctags, das tags für alle möglichen tag-Typen generiert:
Makrodefinitionen, aufgezählte Werte (Werte in enum{...}), Funktions- und
Methodendefinitionen, enum/struct/union-tags, externe Funktionsprototypen
(wahlweise), typedefs und variable Deklarationen. Es läßt sich weit weniger
gut durch Code täuschen, der #if-Präprozessor-Bedingungen enthält, dank
eines konditionalen Pfadauswahlalgorithmus, der komplizierte Entscheidungen
trifft, und eines Ausweiche-Algorithmus, der ins Spiel kommt, wenn der erste
dem Problem nicht gewachsen ist.  Kann auch benutzt werden, um eine Liste
ausgewählter Objekte, die in Quelldateien gefunden wurden, auszudrucken.

%description -l fr
un ctags amélioré générant des tags pour tous les types de tags possibles :
définitions de macros, valeurs énumérées (valeurs dans enum{...}),
définitions de fonctions et de méthodes, enum/struct/union tags, prototypes
de fonctions externes (optionnel), typedefs, et déclarations de variables.
Peut aussi être utilisé pour afficher une liste des objets choisis trouvés
dans les fichiers source.

%description -l pl
Generator tabeli odwo³añ dla: makr, zmiennych, funkcji i procedur, definicji
typów, metod (C++) itp. U¿ywany do generacji listy wyspecyfikowanych
obiektów znalezionych w plikach ¼ród³owych. Tablica owych odwo³añ mo¿e byæ
wykorzystywana przez wiekszosæ standardowych edytorów tekstu (vim, joe,
emacs), do przemieszczania siê w ¼ród³ach miêdzy deklaracj± i u¿yciem danego
symbolu.

%description -l tr
Olabilecek her türlü etiket çeþitleri - makro tanýmlamalarý, sayýlý
(enumerated) deðerler, fonksiyon ve yöntem (method) tanýmlamalarý, tip ve
deðiþken tanýmlarý - için etiketler üretir. Kaynak kodlarýnda bulunan,
seçilmiþ nesnelerin listesinin çýktýsýný yazýcýdan almak için de
kullanýlabilir.

%prep
%setup -q
%patch0 -p1

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT/usr install

rm -f $RPM_BUILD_ROOT/usr/share/man/man1/etags.1
echo ".so ctags.1" > $RPM_BUILD_ROOT/usr/share/man/man1/etags.1

strip $RPM_BUILD_ROOT/usr/bin/*

gzip -9nf $RPM_BUILD_ROOT/usr/share/man/man1/* \
	 FAQ NEWS QUOTES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) /usr/bin/*
/usr/share/man/man1/*

%changelog
* Tue May 11 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.2.1-1]
- now package is FHS 2.0 compiliat.

* Wed Apr 28 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.2-2]
- added patch for glibc 2.1,
- recompiled on new rpm.

* Mon Apr 12 1999 Micha³ Kuratczyk <kura@pld.org.pl>
  [3.0.3-3]
- added gzipping docimentation
- removed man group grom man pages
- added stripping binaries
- added %defattr(644,root,root,755)

* Tue Jan 26 1999 Micha³ Kuratczyk <kura@pld.org.pl>
  [3.0-2]
- changed Group to /Development/Tools
- added Group(pl)

* Fri Dec 11 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.0-1]
- added gzipping man pages,
- added using LDFLAGS="-s" to ./configure enviroment.
- etags(1) man page is now maked as nroff include to ctags(1) instead
  making sym link to ctags.1 (this allow compress man pages).

* Wed Aug 26 1998 Wojciech "Sas" Ciêciwa <cieciwa@zarz.agh.edu.pl>
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
