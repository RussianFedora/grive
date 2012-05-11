%global date 20120510
%global gitcommit 0c3fdaa

Name:           grive
Version:        0.0.4
Release:        1.%{date}git%{gitcommit}%{?dist}
Summary:        An open source Linux client for Google Drive

License:        GPLv2
URL:            http://match065.github.com/grive/
Source0:        https://github.com/match065/%{name}/tarball/%{gitcommit}

BuildRequires:  cmake
BuildRequires:  libstdc++-devel
BuildRequires:  libcurl-devel
BuildRequires:  json-c-devel
BuildRequires:  expat-devel
BuildRequires:  openssl-devel

%description
The purpose of this project is to provide an independent implementation
of Google Drive client. It uses the Google Document List API to talk to
the servers in Google. The code is written in standard C++.


%package        devel
Summary:        Development files for grive
Requires:       %{name} = %{version}

%description    devel
Development files for grive

%prep
%setup -q -n match065-%{name}-%{gitcommit}


%build
%cmake .
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc COPYING README
%{_bindir}/%{name}
%{_libdir}/libgrive.so.*

%files devel
%{_includedir}/%{name}*
%{_libdir}/libgrive.so



%changelog
* Tue May 10 2012 Vasiliy N. Glazov <vascom2@gmail.com> 0.0.4-20120510git0c3fdaa.1.R
- Initial release
