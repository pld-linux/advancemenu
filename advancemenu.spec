#
# Conditional build:
%bcond_without	svga	# SVGAlib support

Summary:	AdvanceMENU - frontend for AdvanceMAME, AdvanceMESS and any other emulator
Summary(pl.UTF-8):	AdvanceMENU - interfejs dla AdvanceMAME, AdvanceMESS i innych emulatorów
Name:		advancemenu
Version:	2.9
Release:	1
License:	GPL v2+
Group:		Applications/Emulators
Source0:	https://downloads.sourceforge.net/advancemame/%{name}-%{version}.tar.gz
# Source0-md5:	8c508a7e862afd015ed9553f18f01294
URL:		http://www.advancemame.it/menu-readme.html
BuildRequires:	SDL-devel >= 1.2.4
BuildRequires:	alsa-lib-devel
BuildRequires:	expat-devel >= 1.95.6
BuildRequires:	freetype-devel >= 2.1.7
BuildRequires:	gcc >= 5:3.2.3
BuildRequires:	libstdc++-devel
BuildRequires:	make >= 1:3.79.1
BuildRequires:	nasm >= 0.98.33
BuildRequires:	ncurses-devel >= 5.4
BuildRequires:	slang-devel >= 1.4.3
%{?with_svga:BuildRequires:	svgalib-devel >= 1.9.14}
BuildRequires:	zlib-devel >= 1.1.4
Requires:	SDL >= 1.2.4
Requires:	expat >= 1.95.6
Requires:	freetype >= 2.1.7
Requires:	ncurses >= 5.4
Requires:	slang >= 1.4.3
%{?with_svga:Requires:	svgalib >= 1.9.14}
Requires:	zlib >= 1.1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AdvanceMENU is a frontend for the AdvanceMAME, AdvanceMESS and
any other emulator.

%description -l pl.UTF-8
AdvanceMENU to interfejs (frontend) dla AdvanceMAME, AdvanceMESS i
innych emulatorów.

%prep
%setup -q

%build
%configure \
	ac_lib_sdl_config=/usr/bin/sdl-config \
	%{!?with_svga:--disable-svgalib}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	docdir=$RPM_BUILD_ROOT%{_docdir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

# plaintext versions packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/advance

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HISTORY README RELEASE
%attr(755,root,root) %{_bindir}/advcfg
%attr(755,root,root) %{_bindir}/advmenu
%attr(755,root,root) %{_bindir}/advv
%{_mandir}/man1/advcfg.1*
%{_mandir}/man1/advmenu.1*
%{_mandir}/man1/advv.1*
