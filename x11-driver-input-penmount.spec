%define gitdate 20110609

Name: x11-driver-input-penmount
Version: 1.4.99
Release: %mkrel 1%{?gitdate:.%{gitdate}}
Summary: X.org input driver for PenMount devices
Group: System/X11
URL: http://xorg.freedesktop.org
%if 0%{?gitdate}
Source: xf86-input-penmount-%{gitdate}.tar.bz2
%else
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-input-penmount-%{version}.tar.bz2
%endif
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: x11-proto-devel >= 1.4
BuildRequires: x11-server-devel >= 1.4
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: x11-server < 1.4

Requires: x11-server-common %(xserver-sdk-abi-requires xinput)

%description
Penmount is an X.org input driver for PenMount devices.

%prep
%if 0%{gitdate}
%setup -q -n xf86-input-penmount-%{gitdate}
%else
%setup -q -n xf86-input-penmount-%{version}
%endif

%build
autoreconf -v --install || exit 1
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/input/penmount_drv.la
%{_libdir}/xorg/modules/input/penmount_drv.so
%{_mandir}/man4/penmount.*
