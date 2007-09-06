Summary:	Access to OBEX FTP via gnome-vfs
Summary(pl.UTF-8):	Dostęp do OBEX FTP za pomocą gnome-vfs
Name:		gnome-vfs-obexftp
Version:	0.4
Release:	1
License:	LGPL
Group:		Applications/Communications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-vfs-obexftp/0.4/%{name}-%{version}.tar.bz2
# Source0-md5:	6e38828738301fb3ec88c0461ff53a60
URL:		https://launchpad.net/gnome-vfs-obexftp
BuildRequires:	bluez-libs-devel >= 3.7
BuildRequires:	dbus-glib-devel >= 0.60
BuildRequires:	expat-devel
BuildRequires:	glib2-devel >= 1:2.6.0
BuildRequires:	gnome-vfs2-devel >= 2.12.0.1
BuildRequires:	openobex-devel >= 1.2
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides an OBEX FTP client for GNOME-VFS applications.
In practice, this lets you access the file system Bluetooth equipped
mobile phones and PDAs in GNOME applications such as the file manager.

%description -l pl.UTF-8
Ten pakiet dostarcza klienta OBEX FTP dla aplikacji GNOME-VFS. W
praktyce pozwala to na dostęp do systemów plików telefonów komórkowych
i PDA wyposażonych w Bluetooth z poziomu aplikacji GNOME, takich jak
zarządca plików.

%prep
%setup -q

%build
%configure \
	--enable-nautilus-workaround \
	--sysconfdir=%{_sysconfdir} \
	--libdir=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_sysconfdir}/gnome-vfs-2.0/modules/obex-module.conf
%attr(755,root,root) %{_libdir}/gnome-vfs-2.0/modules/libobex.so
