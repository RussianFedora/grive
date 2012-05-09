%global gitcommit b0f5769

Name:           grive
Version:        0.0.4
Release:        1%{?dist}
Summary:        An open source Linux client for Google Drive

License:        GPLv2
URL:            http://match065.github.com/grive/
#Source0:        https://github.com/%{name}/%{name}/tarball/%{gitcommit}
Source0:        https://github.com/match065/grive/tarball/master

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


%prep
%setup -q -n match065-%{name}-%{gitcommit}


%build
%cmake .
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc COPYING README
#%{_bindir}/%{name}
#%{_libdir}



%changelog
