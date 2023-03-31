Name:		texlive-fundus-cyr
Version:	26019
Release:	2
Summary:	Support for Washington University Cyrillic fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fundus/cyr/cyr.sty
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fundus-cyr.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package supports the use of the Washington Cyrillic fonts
with LaTeX (Note that standard LateX has support, too, as
encoding OT2). The package is distributed as part of the fundus
bundle.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fundus-cyr/cyr.sty

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
