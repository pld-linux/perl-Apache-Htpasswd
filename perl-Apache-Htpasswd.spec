%include	/usr/lib/rpm/macros.perl
%define	pdir	Apache
%define	pnam	Htpasswd
Summary:	Manage Unix crypt-style password file
Summary(pl):	Obs³uga pliku hase³ w stylu uniksowego crypt
Name:		perl-%{pdir}-%{pnam}
Version:	1.5.5
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module comes with a set of methods to use with htaccess password
files. These files (and htaccess) are used to do Basic Authentication
on a web server.

%description -l pl
Ten modu³ dostarcza zestaw metod, których mo¿na u¿ywaæ z plikami hase³
htaccess. Te pliki (oraz htaccess) s± u¿ywane do uwierzytelnienia
Basic na serwerze WWW.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
