Name:           ocaml-react
Version:        0.9.2
Release:        %mkrel 1
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

