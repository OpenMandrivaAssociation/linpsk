%define name	linpsk

%define version	1.1
%define rel	1

Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
Summary:	Analysis of the electromagnetic properties of structures
Group:		Sciences/Physics 
License:	GPL
URL:		http://www.physics.otago.ac.nz/research/electronics/nec/index.html
Source:		http://alioth.debian.org/frs/download.php/2690/%{name}-%{version}.tar.gz
BuildRequires:	gcc-c++
BuildRequires:	fftw-devel
BuildRequires:	make
BuildRequires:	python
#Provides:	

%description
The Numerical Electromagnetics Code (NEC-2) is a comprehensive 
package for the analysis of the electromagnetic properties of 
structures. It can analyse radiating properties i.e. antenna gain,
as well as scattering properties (radar cross section) of structures.
NEC-2 was originally written in FORTRAN.
NEC2++ is an extensive rewrite of NEC-2 in C++ by Tim Molteno. 
This work was helped tremendously by the work of N. Kyriazis who 
ported NEC-2 to C. The new portions of code are licensed under the 
GNU Public License (GPL). 

%prep
%setup -q -n %{name}

#fix permissions for debuginfo files
chmod 0644 $RPM_BUILD_DIR/%{name}/src/{rttydemodulator.cpp,cpskdemodulator.cpp,cpskdemodulator.h,rttydemodulator.h}


%build

qmake linpsk.pro 

%make

%install
rm -rf %{buildroot}


mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -m 755 bin/linpsk $RPM_BUILD_ROOT%{_bindir}
install -m 755 images/linpsk.png $RPM_BUILD_ROOT%{_datadir}/pixmaps


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING ChangeLog README
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png

