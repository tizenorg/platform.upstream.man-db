Name:           man-db
Version:        2.6.3
Release:        1
License:        GPL-2.0+
Summary:        A set of documentation tools: man, apropos and whatis
Url:            http://man-db.nongnu.org/
Group:          System/Base
Source:         %{name}-%{version}.tar.xz
BuildRequires:  db4-devel
BuildRequires:  gettext
BuildRequires:  groff
BuildRequires:  pkgconfig(libpipeline)
Requires:       bzip2
Requires:       coreutils
Requires:       groff >= 1.18
Requires:       gzip
Requires:       less
Requires:       lzma
Provides:       man

%description
The man package includes three tools for finding information and/or
documentation about your Linux system: man, apropos, and whatis. The
man system formats and displays on-line manual pages about commands or
functions on your system. Apropos searches the whatis database
(containing short descriptions of system commands) for a string.
Whatis searches its own database for a complete word.

The man package should be installed on your system because it is the
primary way to find documentation on a Linux system.

%prep
%setup -q

%build
%configure --libdir=%{_libdir} \
	--libexecdir=%{_libdir} \
	--sysconfdir=%{_sysconfdir} \
	--with-db=db4 \
	--disable-setuid \
	--enable-mandirs=GNU \
	--enable-mb-groff \
	--with-sections="1 n l 8 3 0 2 5 4 9 6 7"

make %{?_smp_mflags}

%install
%make_install

%find_lang %{name} --with-man --all-name

rm -rf %{buildroot}%{_datadir}/doc/man-db

# groff provides this file
rm %{buildroot}%{_bindir}/zsoelim


%lang_package

%docs_package

%files
%config(noreplace) %{_sysconfdir}/man_db.conf
%{_bindir}/apropos
%{_bindir}/catman
%{_bindir}/lexgrog
%{_bindir}/man
%{_bindir}/mandb
%{_bindir}/manpath
%{_bindir}/whatis
%{_sbindir}/accessdb
%{_libdir}/man-db/libman-2.6.3.so
%{_libdir}/man-db/libman.so
%{_libdir}/man-db/libmandb-2.6.3.so
%{_libdir}/man-db/libmandb.so
%{_libdir}/man-db/globbing
%{_libdir}/man-db/manconv
