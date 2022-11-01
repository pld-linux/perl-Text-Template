#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Text
%define		pnam	Template
Summary:	Text::Template - expand template text with embedded Perl
Summary(pl.UTF-8):	Text::Template - przetwarzanie szablonów tekstowych z wbudowanym kodem w Perlu
Name:		perl-Text-Template
Version:	1.61
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	de5146c2001214cb0a251e627f5b185d
URL:		http://search.cpan.org/dist/Text-Template/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-More-UTF8
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a library for generating form letters, building HTML pages,
or filling in templates generally.  A `template' is a piece of text
that has little Perl programs embedded in it here and there.  When you
`fill in' a template, you evaluate the little programs and replace
them with their values.

%description -l pl.UTF-8
To jest biblioteka do generowania listów z formularzy, budowania stron
HTML lub ogólnie wypełniania szablonów. Szablon (template) to kawałek
tekstu, który ma wbudowane gdzieniegdzie małe programy w Perlu. Przy
"wypełnianiu" szablonu te małe programy są wykonywane i zastępowane
zwracanymi przez nie wartościami.

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
%doc README
%{perl_vendorlib}/Text/Template.pm
%{perl_vendorlib}/Text/Template
%{_mandir}/man3/Text::Template*.3pm*
