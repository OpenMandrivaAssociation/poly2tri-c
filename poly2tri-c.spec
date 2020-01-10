%define	api	0.1
%define	major	0
%define	libname	%mklibname %{name} %{api} %{major}
%define	devname	%mklibname -d %{name}

%define _disable_rebuild_configure 1

Summary:	Fast and powerful library for computing 2D constrained Delaunay triangulations
Name:		poly2tri-c
Version:	0.1.0
%define	gitdate	20141115
Release:	%{?gitdate:0.%{gitdate}.}2
Group:		System/Libraries
License:	BSD 3-Clause License
Url:		http://code.google.com/p/poly2tri-c/

# git clone https://code.google.com/p/poly2tri-c/
Source0:	%{name}-%{version}.tar.xz
Patch0:		poly2tri-c-0.1.0-compilefix.patch

BuildRequires:	pcre-devel
BuildRequires:	pkgconfig(glib-2.0)

%description
This is a C port of the poly2tri library - a fast and powerful library for
computing 2D constrained Delaunay triangulations. Instead of the standard C++
library (which included some utilities and template-based data structures),
this port depends on GLib for it's data structures and some of it's utilities.

%package -n     %{libname}
Summary:	%{summary}
Group:		System/Libraries

%description -n	%{libname}
This is a C port of the poly2tri library - a fast and powerful library for
computing 2D constrained Delaunay triangulations. Instead of the standard C++
library (which included some utilities and template-based data structures),
this port depends on GLib for it's data structures and some of it's utilities.

%package -n	%{devname}
Summary:	Header files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n	%{devname}
This package contains the development files for %{name}.

%prep
%setup -q 
%autopatch -p1
./autogen.sh
# Remove enforce Werror causing ftbfs on newer gcc
sed -i 's/Werror/Wno-error/' configure

%build
#CC=gcc
%configure
%make

%install
%makeinstall_std

%files
%doc COPYING README
%{_bindir}/p2tc

%files -n %{libname}
%{_libdir}/lib%{name}-%{api}.so.%{major}*

%files -n %{devname}
%{_libdir}/lib%{name}-%{api}.so
%{_includedir}/%{name}-%{api}/
%{_libdir}/pkgconfig/%{name}.pc
