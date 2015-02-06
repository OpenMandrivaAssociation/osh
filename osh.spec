Summary:	V6 Thompson Shell Port
Name:		osh
Version:	20080629
Release:	4
License:	BSD with advertising
Group:		Shells
Url:		http://v6shell.org/
Source0:	http://v6shell.org/src/osh-%{version}.tar.gz
Patch0:		osh-20080629-no-strip.patch

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

%files
%doc AUTHORS CHANGES CHANGES-sh_to_sh6 LICENSE NOTES README
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

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%make \
	PREFIX=%{_prefix} \
	CFLAGS="%{optflags}" \
	LDFLAGS="%{ldflags}"

%install
%makeinstall_std \
	PREFIX=%{_prefix} \
	MANDIR=%{_mandir}/man1 \
	BINMODE="-m 0755" \
	MANMODE="-m 0644"

