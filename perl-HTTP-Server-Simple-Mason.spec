#
# Conditional build:
%bcond_with	tests		# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTTP
%define	pnam	Server-Simple-Mason
Summary:	HTTP::Server::Simple::Mason - An abstract baseclass for a standalone mason server
Name:		perl-HTTP-Server-Simple-Mason
Version:	0.09
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/J/JE/JESSE/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	89801442d5ed9b39a80605546461712e
URL:		http://search.cpan.org/dist/HTTP-Server-Simple-Mason/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTTP::Server::Simple::Mason - An abstract baseclass for a standalone
mason server.

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
%doc Changes
%{perl_vendorlib}/HTTP/Server/Simple/Mason.pm
%{_mandir}/man3/*
