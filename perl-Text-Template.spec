%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Template
Summary:	Text::Template - Expand template text with embedded Perl
Name:		perl-Text-Template
Version:	1.43
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a library for generating form letters, building HTML pages,
or filling in templates generally.  A `template' is a piece of text
that has little Perl programs embedded in it here and there.  When you
`fill in' a template, you evaluate the little programs and replace them
with their values.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/Text/Template.pm
%{perl_sitelib}/Text/Template
%{_mandir}/man3/*
