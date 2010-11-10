Name: x11-driver-input-penmount
Version: 1.4.1
Release: %mkrel 3
Summary: X.org input driver for PenMount devices
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-input-penmount-%{version}.tar.bz2
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
%setup -q -n xf86-input-penmount-%{version}

%build
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
