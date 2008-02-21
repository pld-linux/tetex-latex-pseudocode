%define short_name pseudocode
%define texhash [ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;

Summary:	Environment "pseudocode" for describing algorithms in a natural manner
Summary(pl.UTF-8):	Środowisko "pseudocode" do opisu algorytmu w sposób naturalny
Name:		tetex-latex-%{short_name}
Version:	1.0
Release:	1
License:	LaTeX Project Public License v3+
Group:		Applications/Publishing/TeX
Source0:	ftp://ftp.ctan.org/pub/tex-archive/macros/latex/contrib/%{short_name}.zip
# Source0-md5:	fd271b2c81d5bf88ff87096c61a27a82
BuildRequires:	unzip
Requires(post,postun):	/usr/bin/texhash
Requires:	tetex-latex
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides the environment "pseudocode" for describing
algorithms in a natural manner.

%description -l pl.UTF-8
Pakiet udostępnia środowisko "pseudocode" służące do opisu
algorytmów w naturalny sposób.

%prep
%setup -q -n %{short_name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/doc/latex/%{short_name}

install *.sty $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}
install *.pdf $RPM_BUILD_ROOT%{_datadir}/texmf/doc/latex/%{short_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc %{_datadir}/texmf/doc/latex/%{short_name}
%{_datadir}/texmf/tex/latex/%{short_name}
