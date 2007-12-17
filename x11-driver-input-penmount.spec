Name: x11-driver-input-penmount
Version: 1.2.1
Release: %mkrel 2
Summary: X.org input driver for PenMount devices
Group: System/X11

########################################################################
# git clone git//git.mandriva.com/people/pcpa/xorg/drivers/xf86-input-penmount  xorg/drivers/xf86-input-penmount
# cd xorg/drivers/xf86-input/penmount
# git-archive --format=tar --prefix=xf86-input-penmount-1.2.1/ master | bzip2 -9 > xf86-input-penmount-1.2.1.tar.bz2
########################################################################
Source0: xf86-input-penmount-%{version}.tar.bz2

License: MIT

########################################################################
# git-format-patch master..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################

BuildRequires: x11-proto-devel >= 1.4
BuildRequires: x11-server-devel >= 1.4
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: x11-server < 1.4

%description
Penmount is an X.org input driver for PenMount devices.
THIS DRIVER IS BROKEN:
Missing symbol xf86XInputSetSendCoreEvents no longer present due to X Input Hotplug
rework.

%prep
%setup -q -n xf86-input-penmount-%{version}

%patch1 -p1

%build
autoreconf -ifs
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
