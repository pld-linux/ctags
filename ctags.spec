Summary:	Exuberant ctags -- C cross-reference tool
Summary(de):	Exuberant ctags - C-Cross-Reference-Tool
Summary(es):	Ctags ¡exuberantes! Herramienta de referencia cruzada para C
Summary(fr):	ctags exubérant
Summary(pl):	ctags - generator list odwo³añ
Summary(pt_BR):	Ctags exuberantes! Ferramenta de referência cruzada para C
Summary(ru):	õÔÉÌÉÔÁ ÄÌÑ ÉÎÄÅËÓÁÃÉÉ É ÐÏÓÔÒÏÅÎÉÑ ÓÓÙÌÏË ÄÌÑ ÑÚÙËÁ C
Summary(tr):	C dili için çapraz-baþvuru (cross-reference) aracý
Summary(uk):	õÔÉÌ¦ÔÁ ÄÌÑ ¦ÎÄÅËÓÁÃ¦§ ÔÁ ÐÏÂÕÄÏ×É ÐÏÓÉÌÁÎØ ÄÌÑ ÍÏ×É C
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

%description -l de
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

%description -l es
Un ctags mejor que crea tags para todos los tipos posibles de tag:
definiciones de macro, valores enumerados, definiciones de función y
método, tags enum/struct/union, prototipos de función externa
(opcional), typedefs y declaraciones variables. Es más difícil de ser
engañado en códigos que contenga la directiva condicional #if para el
preprocesador, pues utiliza un algoritmo condicional de camino para
solucionar decisiones complicadas, y un algoritmo de rescate cuando
este falla. También puede ser usado para enseñar una lista de objetos
seleccionados que esté en los archivos fuente.

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

%description -l pt_BR
Um ctags melhor que gera tags para todos os tipos possíveis de tag:
definições de macro, valores enumerados, definições de função e
método, tags enum/struct/union, protótipos de função externa
(opcional), typedefs e declarações variáveis. É mais difícil de ser
enganado em códigos que contenha a diretiva condicional #if para o
pré-processador, pois utiliza um algoritmo condicional de caminho para
resolver decisões complicadas, e um algoritmo de resgate quando este
falha. Também pode ser usado para mostrar uma lista de objetos
selecionados que estejam nos arquivos fonte.

%description -l ru
Ctags ÇÅÎÅÒÉÒÕÅÔ ÉÎÄÅËÓÎÙÊ (ÉÌÉ ÔÜÇ-) ÆÁÊÌ ÏÂßÅËÔÏ× ÑÚÙËÁ C, ËÏÔÏÒÙÅ
ÎÁÈÏÄÑÔÓÑ × ÆÁÊÌÁÈ ÉÓÈÏÄÎÙÈ ÔÅËÓÔÏ× É ÈÅÄÅÒÁÈ ÎÁ ÑÚÙËÅ C. ôÁËÏÊ ÉÎÄÅËÓ
ÏÂÌÅÇÞÁÅÔ ÔÅËÓÔÏ×ÙÍ ÒÅÄÁËÔÏÒÁÍ É ÄÒÕÇÉÍ ÕÔÉÌÉÔÁÍ ÐÏÉÓË ÉÎÄÅËÓÉÒÏ×ÁÎÎÙÈ
ÏÂßÅËÔÏ×. Ctags ÔÁËÖÅ ÍÏÖÅÔ ÇÅÎÅÒÉÒÏ×ÁÔØ ÆÁÊÌ ÐÅÒÅËÒÅÓÔÎÙÈ ÓÓÙÌÏË,
ËÏÔÏÒÙÊ ÓÏÄÅÒÖÉÔ ÉÎÆÏÒÍÁÃÉÀ Ï ÒÁÚÌÉÞÎÙÈ ÏÂßÅËÔÁÈ, ÓÏÄÅÒÖÁÝÉÈÓÑ ×
ÎÁÂÏÒÅ ÆÁÊÌÏ× ÎÁ ÑÚÙËÅ C × ÐÒÉÇÏÄÎÏÊ ÄÌÑ ÞÔÅÎÉÑ ÆÏÒÍÅ. Exuberant Ctags
ÐÒÅÄÓÔÁ×ÌÑÅÔ ÓÏÂÏÊ ÕÓÏ×ÅÒÛÅÎÓÔ×Ï×ÁÎÉÅ ÓÔÁÎÄÁÒÔÎÏÇÏ ctags, Ô.Ë. ÏÎ
ÓÐÏÓÏÂÅÎ ÎÁÈÏÄÉÔØ ×ÓÅ ÔÉÐÙ ÔÜÇÏ× ÑÚÙËÁ C, ×ËÌÀÞÁÑ ÍÁËÒÏÏÐÒÅÄÅÌÅÎÉÑ,
ÐÅÒÅÞÉÓÌÑÅÍÙÅ ÚÎÁÞÅÎÉÑ (ÚÎÁÞÅÎÉÑ ×ÎÕÔÒÉ enum{...}), ÏÐÒÅÄÅÌÅÎÉÑ
ÆÕÎËÃÉÊ É ÍÅÔÏÄÏ×, ÔÜÇÉ enum/struct/union, ÐÒÏÔÏÔÉÐÙ ×ÎÅÛÎÉÈ ÆÕÎËÃÉÊ,
ÉÍÅÎÁ typedef É ÄÅËÌÁÒÁÃÉÉ ÐÅÒÅÍÅÎÎÙÈ. Exuberant Ctags ÚÎÁÞÉÔÅÌØÎÏ
ÔÒÕÄÎÅÅ ÏÂÍÁÎÕÔØ ËÏÄÏÍ, ÓÏÄÅÒÖÁÝÉÍ ÕÓÌÏ×ÎÙÅ ËÏÎÓÔÒÕËÃÉÉ ÐÒÅÐÒÏÃÅÓÓÏÒÁ
#if, ÞÅÍ ÏÒÉÇÉÎÁÌØÎÙÊ ctags. Exuberant Ctags ÐÏÄÄÅÒÖÉ×ÁÅÔ ×Ù×ÏÄ ÆÁÊÌÁ
TAGS × ÓÔÉÌÅ Emacs É ÍÏÖÅÔ ÂÙÔØ ÉÓÐÏÌØÚÏ×ÁÎ ÄÌÑ ×Ù×ÏÄÁ ÓÐÉÓËÁ
×ÙÂÒÁÎÎÙÈ ÏÂßÅËÔÏ×, ÎÁÊÄÅÎÎÙÈ × ÉÓÈÏÄÎÙÈ ÆÁÊÌÁÈ.

%description -l tr
Olabilecek her türlü etiket çeþitleri - makro tanýmlamalarý, sayýlý
(enumerated) deðerler, fonksiyon ve yöntem (method) tanýmlamalarý, tip
ve deðiþken tanýmlarý - için etiketler üretir. Kaynak kodlarýnda
bulunan, seçilmiþ nesnelerin listesinin çýktýsýný yazýcýdan almak için
de kullanýlabilir.

%description -l uk
Ctags ÇÅÎÅÒÕ¤ ¦ÎÄÅËÓÎÉÊ (ÁÂÏ ÔÅÇ-) ÆÁÊÌ ÏÂ'¤ËÔ¦× ÍÏ×É C, ÑË¦
ÚÎÁÈÏÄÑÔØÓÑ Õ ÆÁÊÌÁÈ ×ÉÈ¦ÄÎÉÈ ÔÅËÓÔ¦× ÔÁ ÈÅÄÅÒÁÈ ÎÁ ÍÏ×¦ C. ôÁËÉÊ
¦ÎÄÅËÓ ÐÏÌÅÇÛÕ¤ ÔÅËÓÔÏ×ÉÍ ÒÅÄÁËÔÏÒÁÍ ÔÁ ¦ÎÛÉÍ ÕÔÉÌ¦ÔÁÍ ÐÏÛÕË
¦ÎÄÅËÓÏ×ÁÎÉÈ ÏÂ'¤ËÔ¦×. Ctags ÔÁËÏÖ ÍÏÖÅ ÇÅÎÅÒÕ×ÁÔÉ ÆÁÊÌ ÐÅÒÅÈÒÅÓÎÉÈ
ÐÏÓÉÌÁÎØ, ÑËÉÊ Í¦ÓÔÉÔØ ¦ÎÆÏÒÍÁÃ¦À ÐÒÏ Ò¦ÚÎ¦ ÏÂ'¤ËÔÉ, ÑË¦ Í¦ÓÔÑÔØÓÑ Õ
ÎÁÂÏÒ¦ ÆÁÊÌ¦× ÎÁ ÍÏ×¦ C Õ ÐÒÉÄÁÔÎ¦Ê ÄÌÑ ÞÉÔÁÎÎÑ ÆÏÒÍ¦. Exuberant Ctags
Ñ×ÌÑ¤ ÓÏÂÏÀ ×ÄÏÓËÏÎÁÌÅÎÎÑ ÓÔÁÎÄÁÒÔÎÏÇÏ ctags, ÔÁË ÑË ×¦Î Õ ÓÔÁÎ¦
ÚÎÁÈÏÄÉÔÉ ×Ó¦ ÔÉÐÉ ÔÅÇ¦× ÍÏ×É C, ×ËÌÀÞÁÀÞÉ ÍÁËÒÏ×ÉÚÎÁÞÅÎÎÑ, ÚÎÁÞÅÎÎÑ
×ÓÅÒÅÄÉÎ¦ enum{...}, ×ÉÚÎÁÞÅÎÎÑ ÆÕÎËÃ¦Ê ÔÁ ÍÅÔÏÄ¦×, ÔÅÇÉ
enum/struct/union, ÐÒÏÔÏÔÉÐÉ ÚÏ×Î¦ÛÎ¦È ÆÕÎËÃ¦Ê, ¦ÍÅÎÁ typedef ÔÁ
ÄÅËÌÁÒÁÃ¦§ ÚÍ¦ÎÎÉÈ. Exuberant Ctags ÚÎÁÞÎÏ ÔÑÖÞÅ ÏÂÍÁÎÕÔÉ ËÏÄÏÍ, ÝÏ
Í¦ÓÔÉÔØ ÕÍÏ×Î¦ ËÏÎÓÔÒÕËÃ¦À ÐÒÅÐÒÏÃÅÓÏÒÁ #if, Î¦Ö ÏÒÉÇ¦ÎÁÌØÎÉÊ ctags.
Exuberant Ctags Ð¦ÄÔÒÉÍÕ¤ ×É×¦Ä ÆÁÊÌÕ TAGS Õ ÓÔÉÌ¦ Emacs ¦ ÍÏÖÅ ÂÕÔÉ
×ÉËÏÒÉÓÔÁÎÉÊ ÄÌÑ ×É×ÏÄÕ ÓÐÉÓËÕ ×ÉÂÒÁÎÉÈ ÏÂ'¤ËÔ¦×, ÑË¦ ÚÎÁÈÏÄÑÔØÓÑ Õ
×ÉÈ¦ÄÎÉÈ ÆÁÊÌÁÈ.

%prep
%setup -q

%build
%{__autoconf}
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc FAQ NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
