Name: x11-driver-input-penmount
Version: 1.5.0
Release: 5
Summary: X.org input driver for PenMount devices
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-input-penmount-%{version}.tar.bz2

BuildRequires: x11-proto-devel >= 1.4
BuildRequires: pkgconfig(xorg-server) >= 1.13
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: x11-server < 1.4

Requires: x11-server-common %(xserver-sdk-abi-requires xinput)

%description
Penmount is an X.org input driver for PenMount devices.

%prep
%setup -qn xf86-input-penmount-%{version}

%build
autoreconf -v --install || exit 1
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%doc COPYING
%{_libdir}/xorg/modules/input/penmount_drv.so
%{_mandir}/man4/penmount.*

