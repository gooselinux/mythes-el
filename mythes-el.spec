Name: mythes-el
Summary: Greek thesaurus
%define upstreamid 20070412
Version: 0.%{upstreamid}
Release: 5.1%{?dist}
Source: http://www.ellak.gr/pub/oo_extras/th_el.zip
Group: Applications/Text
URL: http://www.openthesaurus.gr/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+
BuildArch: noarch

%description
Greek thesaurus.

%prep
%setup -q -c

%build
for i in README_th_el_GR_v2.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-7 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_el_GR_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes

pushd $RPM_BUILD_ROOT/%{_datadir}/mythes/
el_GR_aliases="el_CY"
for lang in $el_GR_aliases; do
        ln -s th_el_GR_v2.dat "th_"$lang"_v2.dat"
        ln -s th_el_GR_v2.idx "th_"$lang"_v2.idx"
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_th_el_GR_v2.txt
%dir %{_datadir}/mythes
%{_datadir}/mythes/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20070412-5.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20070412-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolan McNamara <caolanm@redhat.com> - 0.20070412-4
- tidy spec

* Fri Jun 12 2009 Caolan McNamara <caolanm@redhat.com> - 0.20070412-3
- extend coverage

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20070412-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 15 2009 Caolan McNamara <caolanm@redhat.com> - 0.20070412-1
- initial version
