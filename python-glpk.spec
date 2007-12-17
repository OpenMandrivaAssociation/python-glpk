%define name python-glpk
%define version 0.4
%define release %mkrel 3

Summary: Python extension module for GLPK
Name: 	 %{name}
Version: %{version}
Release: %{release}
License: GPL
URL: 	 http://nexedi.com/
Group: 	 Development/Python
Source0: python-glpk-%{version}.tar.bz2
Requires: python >= 2.2
BuildRequires: python-devel, libglpk-devel, swig

%description
A extension module for GNU Linear Programming Kit to Python.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-, root, root)
%doc PKG-INFO README


