Summary:	Exuberant ctags -- C cross-reference tool
Summary(de):	Exuberant ctags - C-Cross-Reference-Tool 
Summary(fr):	ctags exubérant
Summary(pl):	ctags - generator list odwo³añ
Summary(tr):	C dili için çapraz-baþvuru (cross-reference) aracý
Name:		ctags
Version:	5.1
Release:	1
License:	GPL
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Source0:	http://ctags.sourceforge.net/archives/%{name}-%{version}.tar.gz
Patch0:		%{name}-glibc.patch
URL:		http://ctags.sourceforge.net/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ctags generates an index (or tag) file of C language objects found in
C source and header files. The index makes it easy for text editors or
other utilities to locate the indexed items. Ctags can also generate a
cross reference file which lists information about the various objects
found in a set of C language files in human readable form. Exuberant
Ctags improves on ctags because it can find all types of C language
tags, including macro definitions, enumerated values (values inside
enum{...}), function and method definitions, enum/struct/union tags,
external function prototypes, typedef names and variable declarations.
Exuberant Ctags is far less likely to be fooled by code containing #if
preprocessor conditional constructs than ctags. Exuberant ctags
supports output of emacs style TAGS files and can be used to print out
a list of selected objects found in source files.

%description -l de
Ein verbessertes ctags, das tags für alle möglichen tag-Typen
generiert: Makrodefinitionen, aufgezählte Werte (Werte in enum{...}),
Funktions- und Methodendefinitionen, enum/struct/union-tags, externe
Funktionsprototypen (wahlweise), typedefs und variable Deklarationen.
Es läßt sich weit weniger gut durch Code täuschen, der
#if-Präprozessor-Bedingungen enthält, dank eines konditionalen
Pfadauswahlalgorithmus, der komplizierte Entscheidungen trifft, und
eines Ausweiche-Algorithmus, der ins Spiel kommt, wenn der erste dem
Problem nicht gewachsen ist. Kann auch benutzt werden, um eine Liste
ausgewählter Objekte, die in Quelldateien gefunden wurden,
auszudrucken.

%description -l fr
un ctags amélioré générant des tags pour tous les types de tags
possibles : définitions de macros, valeurs énumérées (valeurs dans
enum{...}), définitions de fonctions et de méthodes, enum/struct/union
tags, prototypes de fonctions externes (optionnel), typedefs, et
déclarations de variables. Peut aussi être utilisé pour afficher une
liste des objets choisis trouvés dans les fichiers source.

%description -l pl
Generator tabeli odwo³añ dla: makr, zmiennych, funkcji i procedur,
definicji typów, metod (C++) itp. U¿ywany do generacji listy
wyspecyfikowanych obiektów znalezionych w plikach ¼ród³owych. Tablica
owych odwo³añ mo¿e byæ wykorzystywana przez wiekszosæ standardowych
edytorów tekstu (vim, joe, emacs), do przemieszczania siê w ¼ród³ach
miêdzy deklaracj± i u¿yciem danego symbolu.

%description -l tr
Olabilecek her türlü etiket çeþitleri - makro tanýmlamalarý, sayýlý
(enumerated) deðerler, fonksiyon ve yöntem (method) tanýmlamalarý, tip
ve deðiþken tanýmlarý - için etiketler üretir. Kaynak kodlarýnda
bulunan, seçilmiþ nesnelerin listesinin çýktýsýný yazýcýdan almak için
de kullanýlabilir.

%prep
%setup -q
#%patch -p0

%build
autoconf
cp -f /usr/share/automake/install-sh .
cp -f /usr/share/automake/config.sub .
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir} 

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/etags.1
echo ".so ctags.1" > $RPM_BUILD_ROOT%{_mandir}/man1/etags.1

gzip -9nf FAQ NEWS QUOTES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
