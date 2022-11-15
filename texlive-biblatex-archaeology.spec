Name:		texlive-biblatex-archaeology
Version:	53281
Release:	1
Summary:	A collection of BibLaTeX styles for German prehistory
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-archaeology
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-archaeology.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-archaeology.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-archaeology.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides additional BibLaTeX styles for German
humanities. Its core purpose is to enable the referencing rules
of the Romano-Germanic Commission (>Romisch-Germanische
Kommission), the department of prehistory of the German
Archaeological Institute (Deutsches Archaologisches Institut),
since these are referenced by most guidelines in German
prehistory and medieval archaeology and serve as a kind of
template. biblatex-archaeology provides verbose, numeric and
author date styles as well and adaptions to specific document
types like exhibition and auction catalogues.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/biblatex-archaeology
%{_texmfdistdir}/tex/latex/biblatex-archaeology
%doc %{_texmfdistdir}/doc/latex/biblatex-archaeology

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
