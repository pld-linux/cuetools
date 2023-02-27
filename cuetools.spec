Summary:	Set of utilities for working with cue files and toc files
Summary(pl.UTF-8):	Zestaw narzędzi do pracy z plikami cue i toc
Name:		cuetools
Version:	1.4.1
Release:	1
License:	GPL v2
Group:		Applications/Files
#Source0Download: https://github.com/svend/cuetools/tags
Source0:	https://github.com/svend/cuetools/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	b1f365fc7ab02eff4b58b6a54ecee080
URL:		https://github.com/svend/cuetools
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
Conflicts:	flac < 1.1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cuetools is a set of utilities for working with cue files and toc
files.

%description -l pl.UTF-8
cuetools to zestaw narzędzi do pracy z plikami cue i toc.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md TODO
%attr(755,root,root) %{_bindir}/cuebreakpoints
%attr(755,root,root) %{_bindir}/cueconvert
%attr(755,root,root) %{_bindir}/cueprint
%attr(755,root,root) %{_bindir}/cuetag.sh
%{_mandir}/man1/cuebreakpoints.1*
%{_mandir}/man1/cueconvert.1*
%{_mandir}/man1/cueprint.1*
