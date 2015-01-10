Name: cobbler-all
Version: {{item}}
Release: 0%{?_dist_release}
Summary: Virtual Package includes Cobbler, cman,and libvirt

Group: Applications/Internet
License: None
URL: https://github.com/gracefullife/virtual-cobbler-all
Source0: %{name}-%{version}.tar.gz
# Source: https://github.com/peco/peco/releases/download/v%{Version}/peco_v%{Version}_linux_amd64.tar.gz
Vendor: Cobbler, and other contributers on github.
Packager: Kazushige TAKEUCHI

BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires: cobbler, cobbler-web, cman, libvirt, koan, tftp, dnsmasq, syslinux
BuildArch: noarch

%description

%prep
%setup
%build
%install
%clean
%files
%doc

%changelog
* Sun Dec 28 2015 Kazushige TAKEUCHI <kazushige.takeuchi@gmail.com>
- rpm release of version 1.0
