%define ruby_dist ruby-enterprise
%define ruby_dist_dash %{ruby_dist}-
%define _prefix /opt/ruby-enterprise
%define _gem %{_prefix}/bin/gem
%define _ruby %{_prefix}/bin/ruby

# Generated from haml-3.1.1.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(%{_ruby} -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(%{_ruby} -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname haml
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: An elegant, structured XHTML/XML templating engine
Name: %{?ruby_dist_dash}rubygem-%{gemname}
Version: 3.1.1
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://haml-lang.com/
Source0: http://gemcutter.orggems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: %{?ruby_dist_dash}rubygems
Requires: %{?ruby_dist_dash}rubygem(yard) >= 0.5.3
Requires: %{?ruby_dist_dash}rubygem(maruku) >= 0.5.9
BuildRequires: %{?ruby_dist_dash}rubygems
BuildArch: noarch
Provides: %{?ruby_dist_dash}rubygem(%{gemname}) = %{version}

%description
Haml (HTML Abstraction Markup Language) is a layer on top of XHTML or
XML
that's designed to express the structure of XHTML or XML documents
in a non-repetitive, elegant, easy way,
using indentation rather than closing tags
and allowing Ruby to be embedded with ease.
It was originally envisioned as a plugin for Ruby on Rails,
but it can function as a stand-alone templating engine.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
%{_gem} install --local --install-dir %{buildroot}%{gemdir} \
                --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gemdir}/bin
find %{buildroot}%{geminstdir}/bin -type f | xargs chmod a+x

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/haml
%{_bindir}/html2haml
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Mon Oct  3 2011 Jeff Goldschrafe <jeff@holyhandgrenade.org> - 3.1.1-1.hhg
- Rebuild for Ruby Enterprise Edition

* Thu Apr 28 2011 Sergio Rubio <rubiojr@frameos.org> - 3.1.1-1
- Initial package
