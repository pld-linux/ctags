Summary:	Exuberant ctags -- C cross-reference tool
Summary(de.UTF-8):	Exuberant ctags - C-Cross-Reference-Tool
Summary(es.UTF-8):	ctags - generador de listas de referencia
Summary(fr.UTF-8):	ctags exubérant
Summary(ko.UTF-8):	여러 언어로 된 소스 코드에 색인을 만들어주는 도구
Summary(pl.UTF-8):	ctags - generator list odwołań
Summary(pt_BR.UTF-8):	Ctags exuberantes! Ferramenta de referência cruzada para C
Summary(ru.UTF-8):	Утилита для индексации и построения ссылок для языка C
Summary(tr.UTF-8):	C dili için çapraz-başvuru (cross-reference) aracı
Summary(uk.UTF-8):	Утиліта для індексації та побудови посилань для мови C
Name:		ctags
Version:	5.8
Release:	4
License:	GPL v2+
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/ctags/%{name}-%{version}.tar.gz
# Source0-md5:	c00f82ecdcc357434731913e5b48630d
Patch0:		format-security.patch
URL:		http://ctags.sourceforge.net/
BuildRequires:	autoconf >= 1.12
BuildRequires:	automake
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
'#if'-Präprozessor-Bedingungen enthält, dank eines konditionalen Ein
verbessertes ctags, das tags für alle möglichen tag-Typen generiert:
Makrodefinitionen, aufgezählte Werte (Werte in enum{...}), Funktions-
und Methodendefinitionen, enum/struct/union-tags, externe
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
owych odwołań może być wykorzystywana przez większość standardowych
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

%description -l ru.UTF-8
Ctags генерирует индексный (или тэг-) файл объектов языка C, которые
находятся в файлах исходных текстов и хедерах на языке C. Такой индекс
облегчает текстовым редакторам и другим утилитам поиск индексированных
объектов. Ctags также может генерировать файл перекрестных ссылок,
который содержит информацию о различных объектах, содержащихся в
наборе файлов на языке C в пригодной для чтения форме. Exuberant Ctags
представляет собой усовершенствование стандартного ctags, т.к. он
способен находить все типы тэгов языка C, включая макроопределения,
перечисляемые значения (значения внутри enum{...}), определения
функций и методов, тэги enum/struct/union, прототипы внешних функций,
имена typedef и декларации переменных. Exuberant Ctags значительно
труднее обмануть кодом, содержащим условные конструкции препроцессора
'#if', чем оригинальный ctags. Exuberant Ctags поддерживает вывод
файла TAGS в стиле Emacs и может быть использован для вывода списка
выбранных объектов, найденных в исходных файлах.

%description -l tr.UTF-8
Olabilecek her türlü etiket çeşitleri - makro tanımlamaları, sayılı
(enumerated) değerler, fonksiyon ve yöntem (method) tanımlamaları, tip
ve değişken tanımları - için etiketler üretir. Kaynak kodlarında
bulunan, seçilmiş nesnelerin listesinin çıktısını yazıcıdan almak için
de kullanılabilir.

%description -l uk.UTF-8
Ctags генерує індексний (або тег-) файл об'єктів мови C, які
знаходяться у файлах вихідних текстів та хедерах на мові C. Такий
індекс полегшує текстовим редакторам та іншим утилітам пошук
індексованих об'єктів. Ctags також може генерувати файл перехресних
посилань, який містить інформацію про різні об'єкти, які містяться у
наборі файлів на мові C у придатній для читання формі. Exuberant Ctags
являє собою вдосконалення стандартного ctags, так як він у стані
знаходити всі типи тегів мови C, включаючи макровизначення, значення
всередині enum{...}, визначення функцій та методів, теги
enum/struct/union, прототипи зовнішніх функцій, імена typedef та
декларації змінних. Exuberant Ctags значно тяжче обманути кодом, що
містить умовні конструкцію препроцесора #if, ніж оригінальний ctags.
Exuberant Ctags підтримує вивід файлу TAGS у стилі Emacs і може бути
використаний для виводу списку вибраних об'єктів, які знаходяться у
вихідних файлах.

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
cp -f /usr/share/automake/install-sh .
cp -f /usr/share/automake/config.sub .
%configure \
	--enable-etags \
	--enable-tmpdir=/tmp

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -j1 install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/etags.1
echo ".so man1/ctags.1" > $RPM_BUILD_ROOT%{_mandir}/man1/etags.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc EXTENDING.html FAQ NEWS README
%attr(755,root,root) %{_bindir}/ctags
%attr(755,root,root) %{_bindir}/etags
%{_mandir}/man1/ctags.1*
%{_mandir}/man1/etags.1*
