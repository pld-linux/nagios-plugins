Summary:	Plugins for Nagios
Summary(pl):	Wtyczki dla Nagiosa
Name:		nagios-plugins
Version:	1.3.0
Release:	0.9
License:	GPL v2
Group:		Networking
Source0:	http://dl.sourceforge.net/nagiosplug/%{name}-%{version}.tar.gz
# Source0-md5:	74ce3383cb39c85df78a1db7ac50838b
URL:		http://nagiosplug.sourceforge.net/
BuildRequires:	mysql-devel
BuildRequires:	net-snmp-devel
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel
BuildRequires:	postgresql-devel
Requires:	nagios
Obsoletes:	netsaint-plugins
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugins for Nagios

%description -l pl
Wtyczki dla Nagiosa

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--libexecdir=%{_libdir}/nagios/plugins
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README REQUIREMENTS SUPPORT
%attr(755,root,root) %{_libdir}/nagios/plugins/*
