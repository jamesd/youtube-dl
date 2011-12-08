Name:           youtube-dl
Version:        2011.11.23
Release:        1%{?dist}
Summary:        Small command-line program to download videos from YouTube
Summary(pl):    Tekstowy program do pobierania filmów z youtube.com
Group:          Applications/Multimedia
License:        Public Domain
URL:            http://rg3.github.com/youtube-dl/
Source0:        https://github.com/rg3/youtube-dl/raw/%{version}/youtube-dl
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       python >= 2.4

%description
Small command-line program to download videos from YouTube.

%description -l pl
youtube-dl to mały tekstowy program służący do pobierania filmów z
youtube.com.

%prep
#nothing to prep

%build
#nothing to build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -p -m 755 %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}

%changelog
* Thu Dec 08 2011 Till Maas <opensource@till.name> - 2011.11.23-1
- Update to new release (fixed Red Hat Bug #758679)

* Fri Oct 21 2011 Till Maas <opensource@till.name> - 2011.10.19-1
- Update to latest release

* Thu Aug 04 2011 Till Maas <opensource@till.name> - 2011.08.04-1
- Update to latest release to adjust to backend changes (Red Hat Bug
  #728378)

* Fri May 13 2011 Till Maas <opensource@till.name> - 2011.03.29-1
- Update to latest release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2011.01.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 31 2011 Till Maas <opensource@till.name> - 2010.01.30-1
- Update to latest release

* Sun Dec 12 2010 Till Maas <opensource@till.name> - 2010.12.09-1
- Update to latest release to adjust with youtube changes

* Sat Nov 06 2010 Till Maas <opensource@till.name> - 2010.10.24-1
- Update to latest release
- Adjust to new upstream location at github instead of bitbucket
- add -p to install
- remove index.html

* Thu Oct 07 2010 Till Maas <opensource@till.name> - 2010.10.03-1
- Update to latest release

* Thu Aug 05 2010 Till Maas <opensource@till.name> - 2010.08.04-1
- Update to latest release

* Fri Jul 23 2010 Till Maas <opensource@till.name> - 2010.07.22-1
- Update to latest release

* Thu Jul 15 2010 Till Maas <opensource@till.name> - 2010.07.14-1
- Update to latest release

* Mon Jun 07 2010 Till Maas <opensource@till.name> - 2010.06.06-1
- Update to latest release

* Thu Apr 29 2010 Till Maas <opensource@till.name> - 2010.04.04-1
- Update to latest release to fix some download issues RH #582372

* Fri Oct 09 2009 Rafał Psota <rafalzaq@gmail.com> - 2009.09.13-2
- Small fix in %%prep

* Sun Sep 27 2009 Rafał Psota <rafalzaq@gmail.com> - 2009.09.13-1
- Update to 2009.09.13
- License change to Public Domain

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2008.01.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2008.01.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 26 2008 Krzysztof Kurzawski <kurzawax at gmail.com> 2008.01.24-1
- Update to v2008.01.24
- Add polish summary and description.

* Wed Jan 02 2008 Krzysztof Kurzawski <kurzawax at gmail.com> 2007.10.12-5
- Correct install.
- Correct documentation.

* Sat Dec 29 2007 Krzysztof Kurzawski <kurzawax at gmail.com> 2007.10.12-4
- Correct requires.
- Add documentation.

* Sun Dec 23 2007 Krzysztof Kurzawski <kurzawax at gmail.com> 2007.10.12-3
- Correct version tag.

* Fri Dec 14 2007 Krzysztof Kurzawski <kurzawax at gmail.com> 1-2
- Update to v2007.10.12, correct license and update summary.

* Sun Dec 9 2007 Krzysztof Kurzawski <kurzawax at gmail.com> 1-1
- First release
