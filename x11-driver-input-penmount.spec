%define Werror_cflags %nil

Summary:	X.org input driver for CMT devices
Name:		x11-driver-input-cmt
Version:	0.1
Release:	0.2
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-cmt-%{version}.tar.bz2

BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	libgestures-devel
BuildRequires:	evdevc-devel
Requires:	x11-server-common %(xserver-sdk-abi-requires xinput)

%description
Is an X.org input driver for CMT devices.

%package	devel
Summary:	Development files for %{name}
Group:		Development/C	

%description
Header files for %{name}

%prep
%setup -qn xf86-input-cmt-%{version}
autoreconf -fiv

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_libdir}/xorg/modules/input/cmt_drv.so

%files devel
%{_includedir}/xorg/cmt-properties.h
%{_libdir}/pkgconfig/xorg-cmt.pc
