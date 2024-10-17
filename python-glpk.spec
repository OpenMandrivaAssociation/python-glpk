%define name python-glpk
%define version 0.4.43
%define release 3
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
Url:		https://www.dcc.fc.up.pt/~jpp/code/python-glpk/
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
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=../FILE_LIST
popd

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc COPYING ChangeLog readme.txt examples/



%changelog
* Sun Nov 21 2010 Funda Wang <fwang@mandriva.org> 1:0.4.43-2mdv2011.0
+ Revision: 599397
- rebuild for py 2.7

* Tue Jul 13 2010 Lev Givon <lev@mandriva.org> 1:0.4.43-1mdv2011.0
+ Revision: 551465
- Update to 0.4.43.
- Update to 0.3.43.
- Update to 0.1.36.

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sat Jan 10 2009 Funda Wang <fwang@mandriva.org> 1:0.1.16-2mdv2009.1
+ Revision: 328010
- llink against py ver

* Fri Jul 25 2008 Lev Givon <lev@mandriva.org> 1:0.1.16-1mdv2009.0
+ Revision: 249838
- Since this package no longer builds, switch to the python-glpk
  software included in Debian.
  Update epoch to account for different version numbers.
- Tweak to rebuild with Python 2.5.

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 0.4-2mdk
- Rebuild for new python

* Mon Sep 06 2004 Yoshinori Okuji <yo@nexedi.com> 0.4-1mdk
- updated to use libglpk4.7

* Fri Feb 27 2004 Sebastien Robin <seb@nexedi.com> 0.3-1mdk
- updated to use libglpk4.4

* Tue Oct 21 2003 Yoshinori OKUJI <yo@nexedi.com> 0.2-1nxd
- new upstream release

* Mon Oct 20 2003 Yoshinori OKUJI <yo@nexedi.com> 0.1-1nxd
- initial version

