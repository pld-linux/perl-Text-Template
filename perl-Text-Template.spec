%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Template
Summary:	Text::Template - Expand template text with embedded Perl
Summary(pl):	Text::Template - przetwarzanie szablonów tekstowych przez wbudowany Perl
Name:		perl-Text-Template
Version:	1.43
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b8026c119a491975ec02853862957f61
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a library for generating form letters, building HTML pages,
or filling in templates generally.  A `template' is a piece of text
that has little Perl programs embedded in it here and there.  When you
`fill in' a template, you evaluate the little programs and replace
them with their values.

%description -l pl
To jest biblioteka do generowania listów z formularzy, budowania stron
HTML lub ogólnie wype³niania szablonów. Szablon (template) to kawa³ek
tekstu, który ma wbudowane gdzieniegdzie ma³e programy w Perlu. Przy
"wype³nianiu" szablonu te ma³e programy s± wykonywane i zastêpowane
zwracanymi przez nie warto¶ciami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Text/Template.pm
%{perl_vendorlib}/Text/Template
%{_mandir}/man3/*
