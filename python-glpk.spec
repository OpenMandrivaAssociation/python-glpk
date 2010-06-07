%define name python-glpk
%define version 0.4.43
%define release %mkrel 1
%define epoch 1

Summary:	A simple Python interface to GLPK
Name:		%{name}
Version:	%{version}
Release:	%{release}
Epoch:		%{epoch}
Source0:        http://www.dcc.fc.up.pt/~jpp/code/python-glpk/%{name}-%{version}.tar.gz
Patch0:		Makefile.patch
License:	GPLv2
Group:		Development/Python
Url:		http://www.dcc.fc.up.pt/~jpp/code/python-glpk/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	python-ply
BuildRequires:	glpk-devel >= 4.43, swig
%py_requires -d

%description
A simple Python interface to GLPK.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 

%build
%make -C src all

%install
%__rm -rf %{buildroot}
pushd src
%__python setup.py install --root=%{buildroot} --record=../FILE_LIST
popd

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc COPYING ChangeLog readme.txt examples/

