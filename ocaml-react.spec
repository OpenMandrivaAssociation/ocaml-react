Name:           ocaml-react
Version:        0.9.2
Release:        3
Summary:        OCaml module for Functional Reactive Programming (FRP)
License:        BSD
Group:          Development/Other
URL:            http://erratique.ch/software/react
Source0:        http://erratique.ch/software/react/releases/react-%{version}.tbz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml

%description
React is an OCaml module for functional reactive programming (FRP).
It provides support to program with time varying values : applicative
events and signals. React doesn't define any primitive event or signal,
this lets the client chooses the concrete timeline.

React is made of a single, independent, module and distributed under
the new BSD license.

Given an absolute notion of time Rtime helps you to manage a timeline
and provides time stamp events, delayed events and delayed signals.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n react-%{version}

%build
chmod u+x build
./build

%check
./build test.native
./test.native

%install
rm -rf %{buildroot}
INSTALLDIR=%{buildroot}/%{_libdir}/ocaml/react ./build install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%dir %{_libdir}/ocaml/react
%{_libdir}/ocaml/react/META
%{_libdir}/ocaml/react/react.cmi
%{_libdir}/ocaml/react/react.cmo

%files devel
%defattr(-,root,root)
%doc doc
%{_libdir}/ocaml/react/react.cmx
%{_libdir}/ocaml/react/react.o
%{_libdir}/ocaml/react/react.mli
%{_libdir}/ocaml/react/react.ml



%changelog
* Fri Sep 16 2011 Alexandre Lissy <alissy@mandriva.com> 0.9.2-3
+ Revision: 700028
- Release bump, rebuilding against latest ocaml

* Wed Oct 06 2010 Funda Wang <fwang@mandriva.org> 0.9.2-2mdv2011.0
+ Revision: 583707
- rebuild

* Thu Aug 12 2010 Florent Monnier <blue_prawn@mandriva.org> 0.9.2-1mdv2011.0
+ Revision: 569281
- updated version

* Thu Apr 22 2010 Florent Monnier <blue_prawn@mandriva.org> 0.9.1-1mdv2010.1
+ Revision: 537968
- updated to version 0.9.1

* Tue Aug 11 2009 Florent Monnier <blue_prawn@mandriva.org> 0.9.0-1mdv2010.0
+ Revision: 414502
- buildrequires ocaml, and cmxs now supported
- import ocaml-react

