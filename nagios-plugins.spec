#
# TODO:
# - swap patch from gentoo (for 2.6 kernels)
# - see anything useful from contrib/
Summary:	Host/service/network monitoring program plugins for Nagios
Summary(pl):	Wtyczki dla Nagiosa
Name:		nagios-plugins
Version:	1.3.1
Release:	2.10
License:	GPL v2
Group:		Networking
Source0:	http://dl.sourceforge.net/nagiosplug/%{name}-%{version}.tar.gz
# Source0-md5:	0078c9c8137694181a4cdf596fdbd74f
Patch0:		%{name}-configure.patch
Patch1:		%{name}-fping.patch
Patch2:		%{name}-subst.patch
URL:		http://nagiosplug.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	mysql-devel
BuildRequires:	net-snmp-devel
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel >= 0.9.7d
# Not really neccesary at build time
BuildRequires:	iputils-ping
BuildRequires:	postgresql-devel
BuildRequires:	perl-Net-SNMP
BuildRequires:	radiusclient-devel
BuildRequires:	fping
BuildRequires:	qstat
BuildRequires:	samba-client
# for rpcinfo
BuildRequires:	glibc-misc
# for host and nslookup
BuildRequires:	bind-utils
BuildRequires:	ntp
Requires:	nagios
Conflicts:	iputils-ping < 1:ss020124
Obsoletes:	netsaint-plugins
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nagios is a program that will monitor hosts and services on your network, and
to email or page you when a problem arises or is resolved. Nagios runs on a
unix server as a background or daemon process, intermittently running checks on
various services that you specify. The actual service checks are performed by
separate "plugin" programs which return the status of the checks to Nagios.

This package contains the basic plugins necessary for use with the Nagios
package.

%description -l pl
Wtyczki dla Nagiosa.

%package snmp
Summary:	snmp
Group:		Networking
Requires:	%{name} = %{version}
Requires:	perl-Net-SNMP

%description snmp
snmp

%package samba
Summary:	Nagios plugin to check remote disk using smbclient.
Group:		Networking
Requires:	%{name} = %{version}
Requires:	samba-client

%description samba
Perl Check SMB Disk plugin for Nagios.

%package sensors
Summary:	Nagios plugin to check hardware status using the lm_sensors package.
Group:		Networking
Requires:	%{name} = %{version}
Requires:	lm_sensors

%description sensors
This plugin checks hardware status using the lm_sensors package.

%package mysql
Summary:	Nagios plugin to tests a MySQL DBMS.
Group:		Networking
Requires:	%{name} = %{version}
Requires:	mysql-libs

%description mysql
This plugin tests a MySQL DBMS to determine whether it is active and accepting
queries.

%package pgsql
Summary:	Nagios plugin to tests a PostgreSQL DBMS.
Group:		Networking
Requires:	%{name} = %{version}
Requires:	postgresql-libs

%description pgsql
This plugin tests a PostgreSQL DBMS to determine whether it is active and
accepting queries. In its current operation, it simply connects to the
specified database, and then disconnects. If no database is specified, it
connects to the template1 database, which is present in every functioning
PostgreSQL DBMS.

%package radius
Summary:	Nagios plugin to test a radius server to see if it is accepting connections.
Group:		Networking
Requires:	%{name} = %{version}
Requires:	radiusclient

%description radius
This plugin tests a radius server to see if it is accepting connections.

%package qstat
Summary:	Nagios plugin to check status of Internet game servers.
Group:		Networking
Requires:	%{name} = %{version}
Requires:	qstat

%description qstat
This plugin uses the 'qstat' command, the popular game server status query
tool.

QStat is a command-line program that displays information about Internet game
servers.

The servers are either down, non-responsive, or running a game.  For servers
running a game, the server name, map name, current number of players, and
response time are displayed.  Server rules and player information may also be
displayed.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p0

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

# need /usr/sbin in PATH,
# otherwise configure will fail locating ntpq and few others.
%configure PATH=${PATH}:/usr/sbin \
	--libexecdir=%{_libdir}/nagios/plugins \
	--with-cgiurl=/nagios/cgi-bin \
	--with-ping_command='/bin/ping -n %%s -c %%d' \
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
	--with-ssh-command="/usr/bin/ssh" \
	--with-mysql \
	--with-pgsql \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README REQUIREMENTS SUPPORT CODING
%defattr(755,root,root,755)

# utils
%{_libdir}/nagios/plugins/negate
%{_libdir}/nagios/plugins/urlize
%{_libdir}/nagios/plugins/utils.pm
%{_libdir}/nagios/plugins/utils.sh

# plugins
%{_libdir}/nagios/plugins/check_by_ssh
%{_libdir}/nagios/plugins/check_dig
%{_libdir}/nagios/plugins/check_disk
%{_libdir}/nagios/plugins/check_dns
%{_libdir}/nagios/plugins/check_dummy
%{_libdir}/nagios/plugins/check_fping
%{_libdir}/nagios/plugins/check_ftp
%{_libdir}/nagios/plugins/check_hpjd
%{_libdir}/nagios/plugins/check_http
%{_libdir}/nagios/plugins/check_imap
%{_libdir}/nagios/plugins/check_ircd
%{_libdir}/nagios/plugins/check_ldap
%{_libdir}/nagios/plugins/check_load
%{_libdir}/nagios/plugins/check_log
%{_libdir}/nagios/plugins/check_mailq
%{_libdir}/nagios/plugins/check_mrtg
%{_libdir}/nagios/plugins/check_mrtgtraf
%{_libdir}/nagios/plugins/check_nntp
%{_libdir}/nagios/plugins/check_nt
%{_libdir}/nagios/plugins/check_ntp
%{_libdir}/nagios/plugins/check_nwstat
%{_libdir}/nagios/plugins/check_overcr
%{_libdir}/nagios/plugins/check_ping
%{_libdir}/nagios/plugins/check_pop
%{_libdir}/nagios/plugins/check_real
%{_libdir}/nagios/plugins/check_rpc
%{_libdir}/nagios/plugins/check_simap
%{_libdir}/nagios/plugins/check_smtp
%{_libdir}/nagios/plugins/check_snmp
%{_libdir}/nagios/plugins/check_spop
%{_libdir}/nagios/plugins/check_ssh
%{_libdir}/nagios/plugins/check_tcp
%{_libdir}/nagios/plugins/check_time
%{_libdir}/nagios/plugins/check_udp
%{_libdir}/nagios/plugins/check_ups
%{_libdir}/nagios/plugins/check_users
%{_libdir}/nagios/plugins/check_vsz

# 2.6 patch needed
%{_libdir}/nagios/plugins/check_swap

# segfaults under 2.6
%{_libdir}/nagios/plugins/check_procs

# syntax errors
%{_libdir}/nagios/plugins/check_breeze

# requries license.dat
%{_libdir}/nagios/plugins/check_flexlm

# Cannot determine ORACLE_HOME for sid
# probably needs some external programs. can't test
%{_libdir}/nagios/plugins/check_oracle

# not there.
#%{_libdir}/nagios/plugins/check_nagios


# Not to be confused with nagios-snmp-plugins
%files snmp
%defattr(755,root,root,755)
# syntax errors, incomplete file paths
%{_libdir}/nagios/plugins/check_wave
%{_libdir}/nagios/plugins/check_ifoperstatus
%{_libdir}/nagios/plugins/check_ifstatus

%files samba
%defattr(755,root,root,755)
%{_libdir}/nagios/plugins/check_disk_smb

%files sensors
%defattr(755,root,root,755)
%{_libdir}/nagios/plugins/check_sensors

%files mysql
%defattr(755,root,root,755)
%{_libdir}/nagios/plugins/check_mysql

%files pgsql
%defattr(755,root,root,755)
%{_libdir}/nagios/plugins/check_pgsql

%files radius
%defattr(755,root,root,755)
%{_libdir}/nagios/plugins/check_radius

%files qstat
%defattr(755,root,root,755)
%{_libdir}/nagios/plugins/check_game
