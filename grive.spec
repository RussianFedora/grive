Name:           grive
Version:        0.2.0
Release:        3%{?dist}
Summary:        An open source Linux client for Google Drive

Group:          Applications/Internet
License:        GPLv2
URL:            http://www.lbreda.com/grive/
Source0:        http://www.lbreda.com/grive/_media/packages/%{version}/%{name}-%{version}.tar.gz

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
%setup -q
# Workaround to compile for Fedora 18
# https://github.com/Grive/grive/issues/72
sed -i -e '/find_package(BFD)/d' libgrive/CMakeLists.txt


%build
%cmake .
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc COPYING README
%{_bindir}/%{name}
%{_mandir}/man1/grive.1.gz


%changelog
* Mon Aug 13 2012 Vasiliy N. Glazov <vascom2@gmail.com> 0.2.0-3
- Added Group

* Fri Jun 22 2012 Vasiliy N. Glazov <vascom2@gmail.com> 0.2.0-2
- Currected URL and Source0 paths

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
