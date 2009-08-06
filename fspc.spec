%define snapshot r36

Name:		fspc
Version:	1.0.1
Release:	%mkrel 0.%{snapshot}
Summary:	Utility to configure sentelic touchpad devices
License:	BSD
Group:		System/Configuration/Hardware
URL:		http://fsp-lnxdrv.sourceforge.net
# checkout from https://fsp-lnxdrv.svn.sourceforge.net/svnroot/fsp-lnxdrv
Source:		fspc-1.0.1-r36.tar.lzma
Patch:		fspc-format-security.patch
BuildRequires:	cmake
BuildRequires:	libwxgtk-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
fspc is an utility to configure features of sentelic touchpad devices.

%prep
%setup -q -n %{name}-%{version}-%{snapshot}
%patch -p1 -b .format-security

%build
pushd src/libfsp
%make
popd
pushd src/fspc
cmake .
%make
popd

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}{%{_bindir},%{_datadir}/fspc}
pushd src/fspc
cp fspcui{,_zh_CN,_zh_TW}.xrc %{buildroot}%{_datadir}/fspc
cp -R pic %{buildroot}%{_datadir}/fspc
cp fspc %{buildroot}%{_bindir}
popd

%files
%defattr(0755,root,root,0755)
%{_bindir}/fspc
%defattr(0644,root,root,0755)
%{_datadir}/fspc
