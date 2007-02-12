Summary:	Exuberant ctags -- C cross-reference tool
Summary(de.UTF-8):   Exuberant ctags - C-Cross-Reference-Tool
Summary(es.UTF-8):   Ctags ¡exuberantes! Herramienta de referencia cruzada para C
Summary(fr.UTF-8):   ctags exubérant
Summary(pl.UTF-8):   ctags - generator list odwołań
Summary(pt_BR.UTF-8):   Ctags exuberantes! Ferramenta de referência cruzada para C
Summary(tr.UTF-8):   C dili için çapraz-başvuru (cross-reference) aracı
Name:		ctags
Version:	5.2.3
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/%{name}/%{name}-%{version}.tar.gz
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

%description -l de.UTF-8
#if-Präprozessor-Bedingungen enthält, dank eines konditionalen
Ein verbessertes ctags, das tags für alle möglichen tag-Typen
generiert: Makrodefinitionen, aufgezählte Werte (Werte in enum{...}),
Funktions- und Methodendefinitionen, enum/struct/union-tags, externe
Funktionsprototypen (wahlweise), typedefs und variable Deklarationen.
Es läßt sich weit weniger gut durch Code täuschen, der
Pfadauswahlalgorithmus, der komplizierte Entscheidungen trifft, und
eines Ausweiche-Algorithmus, der ins Spiel kommt, wenn der erste dem
Problem nicht gewachsen ist. Kann auch benutzt werden, um eine Liste
ausgewählter Objekte, die in Quelldateien gefunden wurden,
auszudrucken.

%description -l es.UTF-8
Un ctags mejor que crea tags para todos los tipos posibles de tag:
definiciones de macro, valores enumerados, definiciones de función y
método, tags enum/struct/union, prototipos de función externa
(opcional), typedefs y declaraciones variables. Es más difícil de ser
engañado en códigos que contenga la directiva condicional #if para el
preprocesador, pues utiliza un algoritmo condicional de camino para
solucionar decisiones complicadas, y un algoritmo de rescate cuando
este falla. También puede ser usado para enseñar una lista de objetos
seleccionados que esté en los archivos fuente.

%description -l fr.UTF-8
un ctags amélioré générant des tags pour tous les types de tags
possibles : définitions de macros, valeurs énumérées (valeurs dans
enum{...}), définitions de fonctions et de méthodes, enum/struct/union
tags, prototypes de fonctions externes (optionnel), typedefs, et
déclarations de variables. Peut aussi être utilisé pour afficher une
liste des objets choisis trouvés dans les fichiers source.

%description -l pl.UTF-8
Generator tabeli odwołań dla: makr, zmiennych, funkcji i procedur,
definicji typów, metod (C++) itp. Używany do generacji listy
wyspecyfikowanych obiektów znalezionych w plikach źródłowych. Tablica
owych odwołań może być wykorzystywana przez wiekszosć standardowych
edytorów tekstu (vim, joe, emacs), do przemieszczania się w źródłach
między deklaracją i użyciem danego symbolu.

%description -l pt_BR.UTF-8
Um ctags melhor que gera tags para todos os tipos possíveis de tag:
definições de macro, valores enumerados, definições de função e
método, tags enum/struct/union, protótipos de função externa
(opcional), typedefs e declarações variáveis. É mais difícil de ser
enganado em códigos que contenha a diretiva condicional #if para o
pré-processador, pois utiliza um algoritmo condicional de caminho para
resolver decisões complicadas, e um algoritmo de resgate quando este
falha. Também pode ser usado para mostrar uma lista de objetos
selecionados que estejam nos arquivos fonte.

%description -l tr.UTF-8
Olabilecek her türlü etiket çeşitleri - makro tanımlamaları, sayılı
(enumerated) değerler, fonksiyon ve yöntem (method) tanımlamaları, tip
ve değişken tanımları - için etiketler üretir. Kaynak kodlarında
bulunan, seçilmiş nesnelerin listesinin çıktısını yazıcıdan almak için
de kullanılabilir.

%prep
%setup -q

%build
autoconf
cp -f %{_datadir}/automake/install-sh .
cp -f %{_datadir}/automake/config.sub .
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

gzip -9nf FAQ NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
