#
# TODO:
# - see anything useful from contrib/
# - package requisites for unifished packages -nsclient and -nwstat
#   REQUIREMENTS explains the dependencies.
#
Summary:	Host/service/network monitoring program plugins for Nagios
Summary(pl):	Wtyczki do monitorowania hostów/us³ug/sieci dla Nagiosa
Name:		nagios-plugins
Version:	1.3.1
Release:	3
License:	GPL v2
Group:		Networking
Source0:	http://dl.sourceforge.net/nagiosplug/%{name}-%{version}.tar.gz
# Source0-md5:	0078c9c8137694181a4cdf596fdbd74f
Patch0:		%{name}-configure.patch
Patch1:		%{name}-fping.patch
Patch2:		%{name}-subst.patch
Patch3:		%{name}-check_swap.c.patch
URL:		http://nagiosplug.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	mysql-devel
BuildRequires:	net-snmp-utils
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
Nagios is a program that will monitor hosts and services on your
network, and to email or page you when a problem arises or is
resolved. Nagios runs on a Unix server as a background or daemon
process, intermittently running checks on various services that you
specify. The actual service checks are performed by separate "plugin"
programs which return the status of the checks to Nagios.

This package contains the basic plugins necessary for use with the
nagios package.

%description -l pl
Nagios to program monitoruj±cy hosty i us³ugi w sieci i powiadamiaj±cy
poczt± elektroniczn± lub na pager o wyst±pieniu lub rozwi±zaniu
problemów. Nagios dzia³a na serwerze uniksowym w tle lub jako demon,
regularnie przeprowadzaj±c kontrolê ró¿nych podanych mu us³ug. Sama
kontrola us³ug jest wykonywana poprzez oddzielne "wtyczki" - programy
zwracajace stan danej us³ugi do Nagiosa.

Ten pakiet zawiera podstawowe wtyczki do u¿ywania z pakietem nagios.

%package snmp
Summary:	Nagios plugins using SNMP protocol to query information
Summary(pl):	Wtyczki Nagiosa u¿ywaj±ce protoko³u SNMP w celu uzyskania informacji
Group:		Networking
Requires:	%{name} = %{version}-%{release}
Requires:	net-snmp-utils
Requires:	perl-Net-SNMP

%description snmp
Nagios plugins using SNMP protocol to query information.

%description snmp -l pl
Wtyczki Nagiosa u¿ywaj±ce protoko³u SNMP w celu uzyskania informacji.

%package samba
Summary:	Nagios plugin to check remote disk using smbclient
Summary(pl):	Wtyczka Nagiosa do zdalnego sprawdzania dysku z u¿yciem smbclienta
Group:		Networking
Requires:	%{name} = %{version}-%{release}
Requires:	samba-client

%description samba
Perl Check SMB Disk plugin for Nagios.

%description samba -l pl
Perlowa wtyczka dla Nagiosa sprawdzaj±ca dyski SMB.

%package sensors
Summary:	Nagios plugin to check hardware status using the lm_sensors package
Summary(pl):	Wtyczka Nagiosa do sprawdzania stanu sprzêtu przy u¿yciu pakietu lm_sensors
Group:		Networking
Requires:	%{name} = %{version}-%{release}
Requires:	lm_sensors

%description sensors
This plugin checks hardware status using the lm_sensors package.

%description sensors -l pl
Ta wtyczka sprawdza stan sprzêtu przy u¿yciu pakietu lm_sensors.

%package mysql
Summary:	Nagios plugin to test a MySQL DBMS
Summary(pl):	Wtyczka Nagiosa do sprawdzania systemu baz danych MySQL
Group:		Networking
Requires:	%{name} = %{version}-%{release}
Requires:	mysql-libs

%description mysql
This plugin tests a MySQL DBMS to determine whether it is active and
accepting queries.

%description mysql -l pl
Ta wtyczka sprawdza serwer baz danych MySQL, aby okre¶liæ, czy jest
aktywny i przyjmuje zapytania.

%package pgsql
Summary:	Nagios plugin to test a PostgreSQL DBMS
Summary(pl):	Wtyczka Nagiosa do sprawdzania systemu baz danych PostgreSQL
Group:		Networking
Requires:	%{name} = %{version}-%{release}
Requires:	postgresql-libs

%description pgsql
This plugin tests a PostgreSQL DBMS to determine whether it is active
and accepting queries. In its current operation, it simply connects to
the specified database, and then disconnects. If no database is
specified, it connects to the template1 database, which is present in
every functioning PostgreSQL DBMS.

%description pgsql -l pl
Ta wtyczka sprawdza serwer baz danych PostgreSQL, aby okre¶liæ, czy
jest aktywny i przyjmuje zapytania. Aktualnie po prostu ³±czy siê do
okre¶lonej bazy danych i roz³±cza. Je¶li nie podano bazy danych, ³±czy
siê do bazy danych template1, obecnej w ka¿dym dzia³aj±cym systemie
PostgreSQL.

%package radius
Summary:	Nagios plugin to test a radius server to see if it is accepting connections
Summary(pl):	Wtyczka Nagiosa do sprawdzania serwera radius pod k±tem przyjmowania po³±czeñ
Group:		Networking
Requires:	%{name} = %{version}-%{release}
Requires:	radiusclient

%description radius
This plugin tests a radius server to see if it is accepting connections.

%description radius -l pl
Ta wtyczka sprawdza serwer us³ugi radius, aby zobaczyæ, czy przyjmuje
po³±czenia.

%package qstat
Summary:	Nagios plugin to check status of Internet game servers
Summary(pl):	Wtyczka Nagiosa do sprawdzania stanu serwerów gier internetowych
Group:		Networking
Requires:	%{name} = %{version}-%{release}
Requires:	qstat

%description qstat
This plugin uses the 'qstat' command, the popular game server status
query tool.

QStat is a command-line program that displays information about
Internet game servers.

The servers are either down, non-responsive, or running a game. For
servers running a game, the server name, map name, current number of
players, and response time are displayed. Server rules and player
information may also be displayed.

%description qstat -l pl
Ta wtyczka u¿ywa polecenia 'qstat' - popularnego narzêdzia do
zapytañ o stan serwerów gier.

QStat to program dzia³aj±cy z linii poleceñ wy¶wietlaj±cy informacje o
serwerach gier internetowych.

Serwery mog± byæ wy³±czone, nie odpowiadaæ, b±d¼ mieæ uruchomion± grê.
Dla serwerów z grami wy¶wietlanea s±: nazwa serwera, nazwa mapy,
aktualna liczba graczy i czas odpowiedzi. Mog± byæ dodatkowo
wy¶wietlone regu³y serwera i informacje o graczach.

%package ldap
Summary:	Nagios plugin to check LDAP servers
Summary(pl):	Wtyczka Nagiosa do sprawdzania serwerów LDAP
Group:		Networking
Requires:	%{name} = %{version}-%{release}
Requires:	openldap-libs

%description ldap
Nagios plugin to check LDAP servers.

%description ldap -l pl
Wtyczka Nagiosa do sprawdzania serwerów LDAP.

# nsclient not packaged in PLD
#%package nsclient
#Summary:	Nagios plugin to check NT server with NSClient
#Summary(pl):	Wtyczka Nagiosa do sprawdzania serwera NT przy u¿yciu NSClienta
#Group:		Networking
#Requires:	%{name} = %{version}-%{release}
#Requires:	nsclient
#
#%description nsclient
#Nagios plugin to check NT server with NSClient.
#
#%description nsclient -l pl
#Wtyczka Nagiosa do sprawdzania serwera NT przy u¿yciu NSClienta.

# requisite not packaged in PLD
#%package nwstat
#Summary:	Nagios plugin nwstat
#Summary(pl):	Wtyczka nwstat do Nagiosa
#Group:		Networking
#Requires:	%{name} = %{version}-%{release}
#Requires:	mrtgext
#
#%description nsclient
#Nagios plugin using MRTGEXT module
#(http://forge.novell.com/modules/xfmod/project/?mrtgext).
#
#%description nsclient -l pl
#Wtyczka nagiosa u¿ywaj±ca modu³u MRTGEXT
#(http://forge.novell.com/modules/xfmod/project/?mrtgext).

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

# need /usr/sbin in PATH,
# otherwise configure will fail locating ntpq and few others.
%configure \
	PATH=${PATH}:/usr/sbin \
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
%{_libdir}/nagios/plugins/check_http
%{_libdir}/nagios/plugins/check_imap
%{_libdir}/nagios/plugins/check_ircd
%{_libdir}/nagios/plugins/check_load
%{_libdir}/nagios/plugins/check_log
%{_libdir}/nagios/plugins/check_mailq
%{_libdir}/nagios/plugins/check_mrtg
%{_libdir}/nagios/plugins/check_mrtgtraf
%{_libdir}/nagios/plugins/check_nntp
%{_libdir}/nagios/plugins/check_ntp
%{_libdir}/nagios/plugins/check_overcr
%{_libdir}/nagios/plugins/check_ping
%{_libdir}/nagios/plugins/check_pop
%{_libdir}/nagios/plugins/check_real
%{_libdir}/nagios/plugins/check_rpc
%{_libdir}/nagios/plugins/check_simap
%{_libdir}/nagios/plugins/check_smtp
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
%{_libdir}/nagios/plugins/check_snmp
%{_libdir}/nagios/plugins/check_hpjd
%{_libdir}/nagios/plugins/check_ifoperstatus
%{_libdir}/nagios/plugins/check_ifstatus

# syntax errors, incomplete file paths
%{_libdir}/nagios/plugins/check_wave
# syntax errors
%{_libdir}/nagios/plugins/check_breeze

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

%files ldap
%defattr(755,root,root,755)
%{_libdir}/nagios/plugins/check_ldap

#%files nsclient
#%defattr(755,root,root,755)
#%{_libdir}/nagios/plugins/check_nt

#%files nwstat
#%defattr(755,root,root,755)
#%{_libdir}/nagios/plugins/check_nwstat
