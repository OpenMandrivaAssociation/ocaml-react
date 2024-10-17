%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	OCaml module for Functional Reactive Programming (FRP)
Name:		ocaml-react
Version:	0.9.4
Release:	2
License:	BSD
Group:		Development/Other
Url:		https://erratique.ch/software/react
Source0:	http://erratique.ch/software/react/releases/react-%{version}.tbz
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib

%description
React is an OCaml module for functional reactive programming (FRP).
It provides support to program with time varying values : applicative
events and signals. React doesn't define any primitive event or signal,
this lets the client chooses the concrete timeline.

React is made of a single, independent, module and distributed under
the new BSD license.

Given an absolute notion of time Rtime helps you to manage a timeline
and provides time stamp events, delayed events and delayed signals.

%files
%doc README
%dir %{_libdir}/ocaml/react
%{_libdir}/ocaml/react/META
%{_libdir}/ocaml/react/react.cmi
%{_libdir}/ocaml/react/react.cma
%{_libdir}/ocaml/react/react.cmxs

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%doc doc
%{_libdir}/ocaml/react/react.cmx
%{_libdir}/ocaml/react/react.cmxa
%{_libdir}/ocaml/react/react.a
%{_libdir}/ocaml/react/react.mli

#----------------------------------------------------------------------------

%prep
%setup -q -n react-%{version}

%build
ocaml setup.ml -configure \
	--prefix %{_prefix} \
	--libdir %{_libdir} \
	--destdir %{buildroot}

ocaml setup.ml -build

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
ocaml setup.ml -install

