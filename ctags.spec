Summary:     Exuberant ctags -- C cross-reference tool
Summary(de): Exuberant ctags - C-Cross-Reference-Tool 
Summary(fr): ctags exubérant
Summary(pl): ctags - generator list odwo³añ
Summary(tr): C dili için çapraz-baþvuru (cross-reference) aracý
Name:        ctags
Version:     2.3.1
Release:     1
Copyright:   GPL
Group:       Development/Languages
Source:      ftp://ftp.revnet.com/pub/ctags/archives/%{name}-%{version}.tar.gz
URL:         http://darren.hiebert.com/ctags
Buildroot:   /tmp/%{name}-%{version}-root

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

%build
CFLAGS=$RPM_OPT_FLAGS ./configure --prefix=/usr
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
strip ctags

%install
make prefix=$RPM_BUILD_ROOT/usr install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(644, root, root, 755) %doc FAQ NEWS QUOTES README
%attr(755, root, root) /usr/bin/*
%attr(644, root,  man) /usr/man/man1/*

%changelog
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
