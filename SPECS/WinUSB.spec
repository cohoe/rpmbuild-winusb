Name:		WinUSB
Version:	1.0.11
Release:	1%{?dist}
Summary:	WinUSB is a simple tool that enable you to create your own usb stick windows installer from an iso image or a real DVD.

Group:		Applications/Utilities
License:	GPS-3.0
URL:		https://github.com/slacka/WinUSB
Source0:	https://github.com/slacka/WinUSB/archive/72aa1d9a36fb88a3f678e68be07c133818b86f39.zip

BuildRequires:	wxGTK3-devel

%description
A Linux program to create Windows USB stick installer from a real Windows DVD or an image._
This package contains two programs:

* WinUSB-gui: a simple tool that enable you to create your own usb stick windows installer from iso image or a real DVD.
* winusb: the command line tool.

Supported images:
* Windows Vista
* Windows 7
* Windows 8
* Windows 10

All languages and any version (home, pro...) and Windows PE are supported.

Supported bootmodes:
* Legacy/MBR-style/IBM PC compatible bootmode
* Native UEFI booting is supported for Windows 7 and later images(with a limitation of only FAT filesystem can be used as target filesystem)

This project is a fork of Congelli501's WinUSB software, which is not maintained since 2012, according to the official website.

%prep
echo "Hello World"
%setup -q

%build
%configure
make %{?_smp_mflags}


%install
%make_install
# @TODO Make this install a desktop file

%files
%doc README.md
# @TODO something im sure

%changelog

