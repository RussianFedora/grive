#Correct it to 1 if you want git snapshot version
%global git 0

%if !%{git}
#Should be corrected to match the Version
    %global gitcommit f4b3e48
%else
    %global gitcommit 271dd95
    %global gitfull 271dd95b2494dd13b6064dd4aac41fb9fb560a66
    %global date 20120608
%endif

Name:           grive
Version:        0.2.0
%if %{git}
Release:        1.%{date}git%{gitcommit}%{?dist}
%else
Release:        1%{?dist}
%endif

Summary:        An open source Linux client for Google Drive

License:        GPLv2
URL:            http://match065.github.com/grive/
%if %{git}
Source0:        https://github.com/Grive/%{name}/tarball/%{gitfull}
%else
Source0:        https://github.com/Grive/%{name}/tarball/v%{version}
%endif

BuildRequires:  cmake
BuildRequires:  libstdc++-devel
BuildRequires:  libcurl-devel
BuildRequires:  json-c-devel
BuildRequires:  expat-devel
BuildRequires:  openssl-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  boost-devel
BuildRequires:  binutils-devel


%description
The purpose of this project is to provide an independent implementation
of Google Drive client. It uses the Google Document List API to talk to
the servers in Google. The code is written in standard C++.


%prep
%setup -q -n Grive-%{name}-%{gitcommit}


%build
%cmake .
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc COPYING README
%{_bindir}/%{name}
%{_mandir}/man1/grive.1.gz


%changelog
* Thu Jun 21 2012 Vasiliy N. Glazov <vascom2@gmail.com> 0.2.0-1
- Update to 0.2.0
- Drop devel subpackage

* Mon Jun 11 2012 Vasiliy N. Glazov <vascom2@gmail.com> 0.1.1-1
- Update to 0.1.1

* Thu Jun 07 2012 Vasiliy N. Glazov <vascom2@gmail.com> 0.1.0-1
- Jump to release versioning

* Tue May 10 2012 Vasiliy N. Glazov <vascom2@gmail.com> 0.1.0-1.20120528git07553e5.R
- Update to 0.1.0

* Tue May 10 2012 Vasiliy N. Glazov <vascom2@gmail.com> 0.0.4-20120510git0c3fdaa.1.R
- Initial release
