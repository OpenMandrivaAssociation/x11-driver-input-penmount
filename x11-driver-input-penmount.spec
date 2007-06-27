Name: x11-driver-input-penmount
Version: 1.2.0
Release: %mkrel 1
Summary: X.org input driver for PenMount devices
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-input-penmount-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

Conflicts: xorg-x11-server < 7.0

%description
Penmount is an X.org input driver for PenMount devices.

%prep
%setup -q -n xf86-input-penmount-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/input/penmount_drv.la
%{_libdir}/xorg/modules/input/penmount_drv.so
%{_mandir}/man4/penmount.4.bz2


