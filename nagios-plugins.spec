Summary:	Plugins for Nagios
Summary(pl):	Wtyczki dla Nagiosa
Name:		nagios-plugins
Version:	1.3.1
Release:	1
License:	GPL v2
Group:		Networking
Source0:	http://dl.sourceforge.net/nagiosplug/%{name}-%{version}.tar.gz
# Source0-md5:	0078c9c8137694181a4cdf596fdbd74f
Patch0:		%{name}-configure.patch
URL:		http://nagiosplug.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	mysql-devel
BuildRequires:	net-snmp-devel
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	postgresql-devel
Requires:	nagios
Obsoletes:	netsaint-plugins
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugins for Nagios.

%description -l pl
Wtyczki dla Nagiosa.

%prep
%setup -q
%patch0 -p0

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--libexecdir=%{_libdir}/nagios/plugins \
	--with-ping-command="/bin/ping" \
	--with-df-command="/bin/df" \
	--with-mailq-command="/usr/bin/mailq" \
	--with-host-command="/usr/bin/host" \
	--with-nslookup-command="/usr/bin/nslookup -sil" \
	--with-uptime-command="/usr/bin/uptime" \
	--with-smbclient-command="/usr/bin/smbclient" \
	--with-ps-command="/bin/ps -weo 'vsz comm'" \
	--with-ps-format="%d %s" \
	--with-ps-raw-command="/bin/ps -weo 'stat user ppid args'" \
	--with-ps-varlist="procstat,&procuid,&procppid,procprog,&pos" \
	--with-rss-command="/bin/ps -weo \'vsz comm\' -weo \'rss comm'" \
	--with-rss-format="%d %s" \
	--with-vsz-command="/bin/ps -weo 'vsz comm' -weo 'vsz comm'" \
	--with-vsz-format="%d %s" \
	--with-ssh-command="/usr/bin/ssh"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README REQUIREMENTS SUPPORT
%attr(755,root,root) %{_libdir}/nagios/plugins/*
