Summary:	Set of utilities for working with cue files and toc files
Summary(pl.UTF-8):	Zestaw narzędzi do pracy z plikami cue i toc
Name:		cuetools
Version:	1.3.1
Release:	1
License:	GPL
Group:		Applications
Source0:	http://download.berlios.de/cuetools/%{name}-%{version}.tar.gz
# Source0-md5:	45575f7a1bdc6615599fa6cb49845cca
Patch0:		%{name}-flac.patch
URL:		http://developer.berlios.de/projects/cuetools/
Conflicts:	flac < 1.1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cuetools is a set of utilities for working with cue files and toc
files.

%description -l pl.UTF-8
cuetools to zestaw narzędzi do pracy z plikami cue i toc.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -m755 extras/cuetag.sh $RPM_BUILD_ROOT/%{_bindir}/cuetag

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
