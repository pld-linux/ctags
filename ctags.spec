Summary:	Exuberant ctags -- C cross-reference tool
Summary(de):	Exuberant ctags - C-Cross-Reference-Tool
Summary(es):	Ctags �exuberantes! Herramienta de referencia cruzada para C
Summary(fr):	ctags exub�rant
Summary(pl):	ctags - generator list odwo�a�
Summary(pt_BR):	Ctags exuberantes! Ferramenta de refer�ncia cruzada para C
Summary(ru):	������� ��� ���������� � ���������� ������ ��� ����� C
Summary(tr):	C dili i�in �apraz-ba�vuru (cross-reference) arac�
Summary(uk):	���̦�� ��� �������æ� �� �������� �������� ��� ���� C
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
#if-Pr�prozessor-Bedingungen enth�lt, dank eines konditionalen
Ein verbessertes ctags, das tags f�r alle m�glichen tag-Typen
generiert: Makrodefinitionen, aufgez�hlte Werte (Werte in enum{...}),
Funktions- und Methodendefinitionen, enum/struct/union-tags, externe
Funktionsprototypen (wahlweise), typedefs und variable Deklarationen.
Es l��t sich weit weniger gut durch Code t�uschen, der
Pfadauswahlalgorithmus, der komplizierte Entscheidungen trifft, und
eines Ausweiche-Algorithmus, der ins Spiel kommt, wenn der erste dem
Problem nicht gewachsen ist. Kann auch benutzt werden, um eine Liste
ausgew�hlter Objekte, die in Quelldateien gefunden wurden,
auszudrucken.

%description -l es
Un ctags mejor que crea tags para todos los tipos posibles de tag:
definiciones de macro, valores enumerados, definiciones de funci�n y
m�todo, tags enum/struct/union, prototipos de funci�n externa
(opcional), typedefs y declaraciones variables. Es m�s dif�cil de ser
enga�ado en c�digos que contenga la directiva condicional #if para el
preprocesador, pues utiliza un algoritmo condicional de camino para
solucionar decisiones complicadas, y un algoritmo de rescate cuando
este falla. Tambi�n puede ser usado para ense�ar una lista de objetos
seleccionados que est� en los archivos fuente.

%description -l fr
un ctags am�lior� g�n�rant des tags pour tous les types de tags
possibles : d�finitions de macros, valeurs �num�r�es (valeurs dans
enum{...}), d�finitions de fonctions et de m�thodes, enum/struct/union
tags, prototypes de fonctions externes (optionnel), typedefs, et
d�clarations de variables. Peut aussi �tre utilis� pour afficher une
liste des objets choisis trouv�s dans les fichiers source.

%description -l pl
Generator tabeli odwo�a� dla: makr, zmiennych, funkcji i procedur,
definicji typ�w, metod (C++) itp. U�ywany do generacji listy
wyspecyfikowanych obiekt�w znalezionych w plikach �r�d�owych. Tablica
owych odwo�a� mo�e by� wykorzystywana przez wiekszos� standardowych
edytor�w tekstu (vim, joe, emacs), do przemieszczania si� w �r�d�ach
mi�dzy deklaracj� i u�yciem danego symbolu.

%description -l pt_BR
Um ctags melhor que gera tags para todos os tipos poss�veis de tag:
defini��es de macro, valores enumerados, defini��es de fun��o e
m�todo, tags enum/struct/union, prot�tipos de fun��o externa
(opcional), typedefs e declara��es vari�veis. � mais dif�cil de ser
enganado em c�digos que contenha a diretiva condicional #if para o
pr�-processador, pois utiliza um algoritmo condicional de caminho para
resolver decis�es complicadas, e um algoritmo de resgate quando este
falha. Tamb�m pode ser usado para mostrar uma lista de objetos
selecionados que estejam nos arquivos fonte.

%description -l ru
Ctags ���������� ��������� (��� ���-) ���� �������� ����� C, �������
��������� � ������ �������� ������� � ������� �� ����� C. ����� ������
��������� ��������� ���������� � ������ �������� ����� ���������������
��������. Ctags ����� ����� ������������ ���� ������������ ������,
������� �������� ���������� � ��������� ��������, ������������ �
������ ������ �� ����� C � ��������� ��� ������ �����. Exuberant Ctags
������������ ����� ������������������ ������������ ctags, �.�. ��
�������� �������� ��� ���� ����� ����� C, ������� ����������������,
������������� �������� (�������� ������ enum{...}), �����������
������� � �������, ���� enum/struct/union, ��������� ������� �������,
����� typedef � ���������� ����������. Exuberant Ctags �����������
������� �������� �����, ���������� �������� ����������� �������������
#if, ��� ������������ ctags. Exuberant Ctags ������������ ����� �����
TAGS � ����� Emacs � ����� ���� ����������� ��� ������ ������
��������� ��������, ��������� � �������� ������.

%description -l tr
Olabilecek her t�rl� etiket �e�itleri - makro tan�mlamalar�, say�l�
(enumerated) de�erler, fonksiyon ve y�ntem (method) tan�mlamalar�, tip
ve de�i�ken tan�mlar� - i�in etiketler �retir. Kaynak kodlar�nda
bulunan, se�ilmi� nesnelerin listesinin ��kt�s�n� yaz�c�dan almak i�in
de kullan�labilir.

%description -l uk
Ctags �����դ ��������� (��� ���-) ���� ��'��Ԧ� ���� C, �˦
����������� � ������ ��Ȧ���� ����Ԧ� �� ������� �� ��צ C. �����
������ ������դ ��������� ���������� �� ����� ���̦��� �����
������������ ��'��Ԧ�. Ctags ����� ���� ���������� ���� �����������
��������, ���� ͦ����� �������æ� ��� Ҧ�Φ ��'����, �˦ ͦ������� �
����Ҧ ���̦� �� ��צ C � ������Φ� ��� ������� ���ͦ. Exuberant Ctags
���Ѥ ����� ������������� ������������ ctags, ��� �� צ� � ���Φ
��������� �Ӧ ���� ��Ǧ� ���� C, ��������� ���������������, ��������
�������Φ enum{...}, ���������� ����æ� �� ����Ħ�, ����
enum/struct/union, ��������� ���Φ�Φ� ����æ�, ����� typedef ��
�������æ� �ͦ����. Exuberant Ctags ������ ����� �������� �����, ��
ͦ����� ����Φ ��������æ� ������������ #if, Φ� ���Ǧ������� ctags.
Exuberant Ctags Ц�����դ ��צ� ����� TAGS � ���̦ Emacs � ���� ����
������������ ��� ������ ������ �������� ��'��Ԧ�, �˦ ����������� �
��Ȧ���� ������.

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
