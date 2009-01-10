%define name python-glpk
%define version 0.1.16
%define release %mkrel 2
%define epoch 1

Summary: A simple Python interface to GLPK
Name: %{name}
Version: %{version}
Release: %{release}
Epoch:	 %{epoch}
Source0: %{name}-%{version}.tar.lzma
Patch0: Makefile.patch
License: GPLv2
Group: Development/Python
Url: http://www.dcc.fc.up.pt/~jpp/code/python-glpk/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: glpk-devel swig
%py_requires -d

%description
A simple Python interface to GLPK.

%prep
%setup -q
%patch0 -p0 -b .build

%build
%make

%install
%__rm -rf %{buildroot}
%__install -m 755 -d %{buildroot}%{py_sitedir}
%__install -m 755 *.so %{buildroot}%{py_sitedir}
%__install -m 644 *.py %{buildroot}%{py_sitedir}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING ChangeLog readme.txt examples/
%py_sitedir/*glpk*
