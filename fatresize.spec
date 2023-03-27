# (tpg) optimize it a bit
%global optflags %{optflags} -Oz --rtlib=compiler-rt

Summary:	Text mode tool for resizing FAT partitions
Name:		fatresize
Version:	1.1.0
Release:	3
License:	GPLv2+
Group:		System/Base
URL:		https://github.com/ya-mouse/fatresize
Source0:	https://github.com/ya-mouse/fatresize/archive/v%{version}.tar.gz
BuildRequires:	pkgconfig(libparted)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	autoconf automake libtool
BuildRequires:	make

%description
Text mode tool for resizing FAT partitions.

%package devel
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{name} = %{EVRD}

%description devel
The %{name}-devel package contains header files developing sudo
plugins that use %{name}.

%prep
%autosetup -p1

aclocal
autoheader
automake -a
autoconf
%configure
# Take care of indirect dependencies -- parted uses uuid
sed -i -e 's,-lparted-fs-resize,-lparted-fs-resize -luuid,g' Makefile

%build
%make_build

%install
%make_install

%files
%{_sbindir}/*
%doc %{_mandir}/man1/*
