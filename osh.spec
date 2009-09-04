Name:		osh
Summary:	V6 Thompson Shell Port
Version:	20080629
Release:	%mkrel 2
License:	BSD with advertising
Source:		http://v6shell.org/src/osh-%{version}.tar.gz
URL:		http://v6shell.org/
Group:		Shells
BuildRoot:	%{_tmppath}/%{name}-%{version}
%description
The osh project is hereby dedicated to the individuals at Bell Labs who
started the UNIX ball rolling in 1969.

The objective of the osh project is to honor our shared computing history
by maintaining two different ports of the original sh(1) as it appeared
in Sixth Edition (V6) UNIX. One of the ports, osh, contains enhancements
to make it usable as an interactive login shell while also remaining
backward compatible. The other port, sh6, simply provides a
backward-compatible user interface without any obvious enhancements. In
addition, the shell utilities necessary for globbing and flow control
in command files (aka shell scripts) are also included.

%prep
%setup -q

%build
%make PREFIX=/usr MANDIR=%{_mandir}/man1 SYSCONFDIR=%{_sysconfdir} \
      BINDIR=%{_bindir}

%install
%{__rm} -Rf %{buildroot}
%{__make} DESTDIR=%{buildroot} PREFIX=/usr MANDIR=%{_mandir}/man1 \
	  SYSCONFDIR=%{_sysconfdir} BINDIR=%{_bindir} install

%clean
%{__rm} -Rf %{buildroot}


%files
%doc AUTHORS CHANGES CHANGES-sh_to_sh6 INSTALL LICENSE NOTES README
%{_bindir}/fd2
%{_bindir}/glob6
%{_bindir}/goto
%{_bindir}/if
%{_bindir}/osh
%{_bindir}/sh6
%{_mandir}/man1/fd2.1.*
%{_mandir}/man1/glob6.1.*
%{_mandir}/man1/goto.1.*
%{_mandir}/man1/if.1.*
%{_mandir}/man1/osh.1.*
%{_mandir}/man1/sh6.1.*
