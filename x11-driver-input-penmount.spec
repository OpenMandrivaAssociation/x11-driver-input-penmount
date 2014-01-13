Summary:	X.org input driver for PenMount devices
Name:		x11-driver-input-penmount
Version:	1.5.0
Release:	9
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-penmount-%{version}.tar.bz2

BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xorg-macros)
Requires:	x11-server-common %(xserver-sdk-abi-requires xinput)

%description
Penmount is an X.org input driver for PenMount devices.

%prep
%setup -qn xf86-input-penmount-%{version}
autoreconf -fiv

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/input/penmount_drv.so
%{_mandir}/man4/penmount.*

