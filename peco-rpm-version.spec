Name: peco
Version: {{item}}
Release: 0%{?_dist_release}
Summary: Selective UI

Group: Applications/Internet
License: MIT
URL: https://github.com/peco/peco
Source0: %{name}-%{version}.tar.gz
# Source: https://github.com/peco/peco/releases/download/v%{Version}/peco_v%{Version}_linux_amd64.tar.gz
Vendor: Daisuke Maki, mattn, syohex, and other contributers on github.
Packager: Kazushige TAKEUCHI

# Distribution:

#BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Prefix: /var/lib/%{name}/v%{version}
#BuildRequires:
#Requires:

%description


%prep
rm -rf %{buildroot}
%setup


%build
# make %{?_smp_mflags}
mkdir -p ./%{prefix}/
mv peco ./%{prefix}/
mkdir -p %{buildroot}
mkdir -p %{buildroot}/usr/bin
#mkdir -p ${RPM_BUILD_ROOT}/%{prefix}

%install
mkdir -p %{buildroot}/usr/bin
cp -r ./var ${RPM_BUILD_ROOT}/
ls -la %{buildroot}
ln -s %{prefix}/peco %{buildroot}/usr/bin/peco
# mv ./var ${RPM_BUILD_ROOT}/
#make install DESTDIR=%{buildroot}


%clean
#rm -rf %{buildroot}
#rm %{prefix}/peco

%files
%defattr(-,root,root,-)
%{prefix}/peco
/usr/bin/peco
%doc



%changelog
* Sun Dec 28 2014 Kazushige TAKEUCHI <kazushige.takeuchi@gmail.com>
- rpm release of version 0.2.11
