Summary:	Set of utilities for working with cue files and toc files
Name:		cuetools
Version:	1.3.1
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://download.berlios.de/cuetools/%{name}-%{version}.tar.gz
# Source0-md5:	45575f7a1bdc6615599fa6cb49845cca
URL:		http://developer.berlios.de/projects/cuetools/
#BuildRequires:	-
#Requires:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cuetools is a set of utilities for working with cue files and toc files.

%prep
%setup -q

%build
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
%doc AUTHORS NEWS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
