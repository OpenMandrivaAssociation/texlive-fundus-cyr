# revision 26019
# category Package
# catalog-ctan /macros/latex/contrib/fundus/cyr/cyr.sty
# catalog-date 2012-04-15 11:57:05 +0200
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-fundus-cyr
Version:	20120415
Release:	5
Summary:	Support for Washington University Cyrillic fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fundus/cyr/cyr.sty
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fundus-cyr.tar.xz
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
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120415-2
+ Revision: 813548
- Update to latest release.
- Import texlive-fundus-cyr
- Import texlive-fundus-cyr

