Summary:	Text mode tool for resizing FAT partitions
Name:		fatresize
Version:	1.0.4
Release:	1
License:	GPLv2+
Group:		System/Base
URL:		https://github.com/ya-mouse/fatresize
Source0:	https://github.com/ya-mouse/fatresize/archive/v%{version}.tar.gz
BuildRequires:	pkgconfig(libparted)
BuildRequires:	autoconf automake libtool

%description
Text mode tool for resizing FAT partitions

%package devel
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{name} = %{EVRD}

%description devel
The %{name}-devel package contains header files developing sudo
plugins that use %{name}.

%prep
%setup -q
aclocal
autoheader
automake -a
autoconf

%configure

%build
%make_build

%install
%make_install

%files
%{_sbindir}/*
%{_mandir}/man1/*
