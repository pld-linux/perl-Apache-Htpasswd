#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Apache
%define	pnam	Htpasswd
Summary:	Manage Unix crypt-style password file
Summary(pl):	Obs³uga pliku hase³ w stylu uniksowego crypt
Name:		perl-%{pdir}-%{pnam}
Version:	1.5.5
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5215d02e4a075535929279f9a0bc98c7
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
