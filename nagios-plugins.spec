# NOTE TO PLD DEVELOPERS:
# - if you use any plugin from -contrib package, move it to subpackage or main
#   package so we can support it better!
# TODO:
# - package requisites for unifished packages -nwstat
#   REQUIREMENTS explains the dependencies.
%include	/usr/lib/rpm/macros.perl
Summary:	Host/service/network monitoring program plugins for Nagios
Summary(pl.UTF-8):	Wtyczki do monitorowania hostów/usług/sieci dla Nagiosa
Name:		nagios-plugins
Version:	1.4.15
Release:	1
License:	GPL v2
Group:		Networking
Source0:	http://downloads.sourceforge.net/nagiosplug/%{name}-%{version}.tar.gz
# Source0-md5:	56abd6ade8aa860b38c4ca4a6ac5ab0d
Source1:	%{name}-config-20100219.tar.bz2
# Source1-md5:	7914664eee7d77be9b8f05347a276e0f
Source2:	nagios-utils.php
#Patch:		%{name}-shared.patch # needs finishing
Patch0:		%{name}-tainted.patch
Patch1:		%{name}-contrib-API.patch
Patch3:		%{name}-subst.patch
Patch4:		%{name}-noroot.patch
Patch5:		%{name}-check_ping-socket-filter-warning.patch
Patch6:		%{name}-path.patch
Patch7:		%{name}-pgsql.patch
Patch9:		%{name}-check_log_paths.patch
Patch12:	%{name}-implicit-basename.patch
Patch13:	%{name}-check_radius_segfault.patch
Patch18:	%{name}-configure.patch
Patch19:	%{name}-perlautodep.patch
Patch20:	%{name}-cosmetic.patch
Patch21:	%{name}-check_hpjd-no-paper-out.patch
Patch22:	%{name}-check_snmp_procs-fix.patch
Patch23:	%{name}-check_disk_smb-zero-cap.patch
Patch24:	%{name}-paths.patch
Patch25:	%{name}-check_snmp_disk_monitor-bulk.patch
Patch26:	%{name}-check_snmp_disk_monitor-opts.patch
Patch27:	%{name}-ping.patch
Patch28:	check_rbl.patch
URL:		http://www.nagiosplugins.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	file
BuildRequires:	gettext-devel >= 0.14.3
BuildRequires:	libtap-devel
BuildRequires:	libtool
BuildRequires:	mysql-devel
BuildRequires:	net-snmp-devel
BuildRequires:	openldap-devel >= 2.3.0
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	perl-Net-SNMP
BuildRequires:	postgresql-devel
BuildRequires:	radiusclient-devel
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.177
Requires:	nagios-common
Obsoletes:	netsaint-plugins
Conflicts:	nagios < 3.1.2-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir		/etc/nagios/plugins
%define		_pluginarchdir	%{_libdir}/nagios/plugins
%define		_pluginlibdir	%{_prefix}/lib/nagios/plugins
%define		_noautoprovfiles	utils.pm
%define		_noautoreq	'perl(DBD::Oracle)' 'perl(Net::Arping)' 'perl(RRD::File)' 'perl(a)' 'perl(packet_utils)' 'perl(snmputil)' 'perl(utils)'

%description
Nagios is a program that will monitor hosts and services on your
network, and to email or page you when a problem arises or is
resolved. Nagios runs on a Unix server as a background or daemon
process, intermittently running checks on various services that you
specify. The actual service checks are performed by separate "plugin"
programs which return the status of the checks to Nagios.

This package contains the basic plugins necessary for use with the
nagios package.

%description -l pl.UTF-8
Nagios to program monitorujący hosty i usługi w sieci i powiadamiający
pocztą elektroniczną lub na pager o wystąpieniu lub rozwiązaniu
problemów. Nagios działa na serwerze uniksowym w tle lub jako demon,
regularnie przeprowadzając kontrolę różnych podanych mu usług. Sama
kontrola usług jest wykonywana poprzez oddzielne "wtyczki" - programy
zwracajace stan danej usługi do Nagiosa.

Ten pakiet zawiera podstawowe wtyczki do używania z pakietem nagios.

%package libs
Summary:	Nagios plugins base libraries
Summary(pl.UTF-8):	Podstawowe biblioteki wtyczek Nagiosa
Group:		Networking

%description libs
This package contains nagios plugins base libraries that plugins
depend on.

%description libs -l pl.UTF-8
Ten pakiet zawiera podstawowe biblioteki wtyczek Nagiosa, wymagane
przez wtyczki.

%package devel
Summary:	Include files that Nagios plugins may compile against
Group:		Development/Libraries
# doesn't require base

%description devel
This package provides include files that Nagios plugins may compile
against.

# NOTE for sub package requires:
# Requires:	nagios-common for plugins directory and nagios group
# and add Requires:	%{name}-libs = %{version}-%{release} for utils.{sh,pm,php}
##############################################################################

%package mysql
Summary:	Nagios plugin to test a MySQL DBMS
Summary(pl.UTF-8):	Wtyczka Nagiosa do sprawdzania systemu baz danych MySQL
Group:		Networking
Requires:	nagios-common

%description mysql
This plugin tests a MySQL DBMS to determine whether it is active and
accepting queries.

%description mysql -l pl.UTF-8
Ta wtyczka sprawdza serwer baz danych MySQL, aby określić, czy jest
aktywny i przyjmuje zapytania.

%package perl
Summary:	Nagios plugins written in Perl
Summary(pl.UTF-8):	Wtyczki Nagiosa napisane w Perlu
Group:		Networking
Requires:	nagios-common
# for utils.pm
Requires:	%{name}-libs = %{version}-%{release}

%description perl
This package contains Nagios plugins written in Perl.

%description perl -l pl.UTF-8
Ten pakiet zawiera wtyczki Nagiosa napisane w Perlu.

%package samba
Summary:	Nagios plugin to check remote disk using smbclient
Summary(pl.UTF-8):	Wtyczka Nagiosa do zdalnego sprawdzania dysku z użyciem smbclienta
Group:		Networking
Requires:	nagios-common
# for utils.pm
Requires:	%{name}-libs = %{version}-%{release}
Requires:	samba-client

%description samba
Perl Check SMB Disk plugin for Nagios.

%description samba -l pl.UTF-8
Perlowa wtyczka dla Nagiosa sprawdzająca dyski SMB.

%package snmp
Summary:	Nagios plugins using SNMP protocol to query information
Summary(pl.UTF-8):	Wtyczki Nagiosa używające protokołu SNMP w celu uzyskania informacji
Group:		Networking
Requires:	nagios-common
# for utils.pm
Requires:	%{name}-libs = %{version}-%{release}
Requires:	net-snmp-utils
Requires:	perl-Net-SNMP

%description snmp
Nagios plugins using SNMP protocol to query information.

%description snmp -l pl.UTF-8
Wtyczki Nagiosa używające protokołu SNMP w celu uzyskania informacji.

%package ssh
Summary:	Nagios plugins to check remote services via SSH
Summary(pl.UTF-8):	Wtyczki Nagiosa do sprawdzania zdalnych usług po SSH
Group:		Networking
Requires:	nagios-common
Requires:	openssh-clients

%description ssh
This plugin uses SSH to execute commands on a remote host.

%description ssh -l pl.UTF-8
Ta wtyczka używa SSH do wykonywania poleceń na zdalnym hoście.

%package -n nagios-plugin-check_dig
Summary:	Nagios plugin to check DNS servers with dig
Summary(pl.UTF-8):	Wtyczka Nagiosa do sprawdzania DNS-u przy użyciu programu dig
Group:		Networking
Requires:	bind-utils
Requires:	nagios-common
Provides:	nagios-plugins-dig = %{version}-%{release}
Obsoletes:	nagios-plugins-dig

%description -n nagios-plugin-check_dig
Test the DNS service on the specified host using dig.

%description -n nagios-plugin-check_dig -l pl.UTF-8
Ta wtyczka sprawdza usługę DNS na podanym hoście przy użyciu programu
dig.

%package -n nagios-plugin-check_dns
Summary:	Nagios plugin to check DNS with nslookup
Summary(pl.UTF-8):	Wtyczka Nagiosa do sprawdzania DNS-u przy użyciu nslookup
Group:		Networking
Requires:	bind-utils
Requires:	nagios-common
Provides:	nagios-plugins-dns = %{version}-%{release}
Obsoletes:	nagios-plugins-dns

%description -n nagios-plugin-check_dns
This plugin uses the nslookup program to obtain the IP address for the
given host/domain query. A optional DNS server to use may be
specified. If no DNS server is specified, the default server(s)
specified in /etc/resolv.conf will be used.

%description -n nagios-plugin-check_dns -l pl.UTF-8
Ta wtyczka używa programu nslookup do uzyskania adresu IP danego dla
danego zapytania o host/domenę. Można opcjonalnie podać serwer DNS,
który ma być użyty. Jeśli nie podano serwera DNS, używany jest
domyślny serwer (lub serwery) podany w /etc/resolv.conf.

%package -n nagios-plugin-check_file_age
Summary:	Nagios plugin to check host up state with fping
Group:		Networking
Requires:	nagios-common
# for utils.pm
Requires:	%{name}-libs = %{version}-%{release}

%description -n nagios-plugin-check_file_age
Nagios plugin to check local file age and size.

%package -n nagios-plugin-check_fping
Summary:	Nagios plugin to check host up state with fping
Summary(pl.UTF-8):	Wtyczka Nagiosa do sprawdzania działania hosta przy użyciu programu fping
Group:		Networking
Requires:	fping
Requires:	nagios-common
Provides:	nagios-plugins-fping = %{version}-%{release}
Obsoletes:	nagios-plugins-fping

%description -n nagios-plugin-check_fping
This plugin will use the /bin/fping command to ping the specified host
for a fast check if the host is alive.

%description -n nagios-plugin-check_fping -l pl.UTF-8
Ta wtyczka używa polecenia /bin/fping do szybkiego sprawdzenia, czy
dany host działa.

%package -n nagios-plugin-check_game
Summary:	Nagios plugin to check status of Internet game servers
Summary(pl.UTF-8):	Wtyczka Nagiosa do sprawdzania stanu serwerów gier internetowych
Group:		Networking
Requires:	nagios-common
Requires:	qstat
Provides:	nagios-plugins-qstat = %{version}-%{release}
Obsoletes:	nagios-plugins-qstat

%description -n nagios-plugin-check_game
This plugin uses the 'qstat' command, the popular game server status
query tool.

QStat is a command-line program that displays information about
Internet game servers.

The servers are either down, non-responsive, or running a game. For
servers running a game, the server name, map name, current number of
players, and response time are displayed. Server rules and player
information may also be displayed.

%description -n nagios-plugin-check_game -l pl.UTF-8
Ta wtyczka używa polecenia 'qstat' - popularnego narzędzia do zapytań
o stan serwerów gier.

QStat to program działający z linii poleceń wyświetlający informacje o
serwerach gier internetowych.

Serwery mogą być wyłączone, nie odpowiadać, bądź mieć uruchomioną grę.
Dla serwerów z grami wyświetlanea są: nazwa serwera, nazwa mapy,
aktualna liczba graczy i czas odpowiedzi. Mogą być dodatkowo
wyświetlone reguły serwera i informacje o graczach.

%package -n nagios-plugin-check_ldap
Summary:	Nagios plugin to check LDAP servers
Summary(pl.UTF-8):	Wtyczka Nagiosa do sprawdzania serwerów LDAP
Group:		Networking
Requires:	nagios-common
Provides:	nagios-plugins-ldap = %{version}-%{release}
Obsoletes:	nagios-plugins-ldap
%if "%{pld_release}" == "ac"
Requires:	openldap
%else
Requires:	openldap-nss-config
%endif

%description -n nagios-plugin-check_ldap
Nagios plugin to check LDAP servers.

%description -n nagios-plugin-check_ldap -l pl.UTF-8
Wtyczka Nagiosa do sprawdzania serwerów LDAP.

%package -n nagios-plugin-check_load
Summary:	Nagios plugin to check uptime using procps
Summary(pl.UTF-8):	Wtyczka Nagiosa do sprawdzania uptime'u przy użyciu procps
Group:		Networking
Requires:	nagios-common
Requires:	procps
Provides:	nagios-plugins-procps = %{version}-%{release}
Obsoletes:	nagios-plugins-procps

%description -n nagios-plugin-check_load
Nagios plugin to check uptime using procps.

%description -n nagios-plugin-check_load -l pl.UTF-8
Wtyczka Nagiosa do sprawdzania uptime'u przy użyciu procps.

%package -n nagios-plugin-check_mailq
Summary:	Nagios plugin to check the number of messages in the local mail queue
Group:		Networking
Requires:	nagios-common
# for utils.pm
Requires:	%{name}-libs = %{version}-%{release}

%description -n nagios-plugin-check_mailq
Checks the number of messages in the mail queue (supports multiple
sendmail queues, qmail).

%package -n nagios-plugin-check_nt
Summary:	Nagios plugin to check NT server with NSClient
Summary(pl):	Wtyczka Nagiosa do sprawdzania serwera NT przy użyciu NSClienta
Group:		Networking
Requires:	%{name}-libs = %{version}-%{release}
Requires:	nagios-common

%description -n nagios-plugin-check_nt
Nagios plugin to check NT server with NSClient.

%description -n nagios-plugin-check_nt -l pl.UTF-8
Wtyczka Nagiosa do sprawdzania serwera NT przy użyciu NSClienta.

%package -n nagios-plugin-check_ntp
Summary:	Nagios plugin to check time using NTP protocol
Summary(pl.UTF-8):	Wtyczka Nagiosa do sprawdzania czasu przy użyciu protokołu NTP
Group:		Networking
Requires:	nagios-common
# for utils.pm
Requires:	%{name}-libs = %{version}-%{release}
Requires:	ntp-client
Provides:	nagios-plugins-ntp = %{version}-%{release}
Obsoletes:	nagios-plugins-ntp

%description -n nagios-plugin-check_ntp
Checks the local timestamp offset versus <host> with ntpdate. Checks
the jitter/dispersion of clock signal between <host> and its sys.peer
with ntpq.

%description -n nagios-plugin-check_ntp -l pl.UTF-8
Ta wtyczka sprawdza przesunięcie lokalnego czasu względem danego hosta
przy użyciu ntpdate. Sprawdza wahania/dyspersję sygnału zegara
pomiędzy hostem a jego sys.peer przy użyciu ntpq.

%package -n nagios-plugin-check_pgsql
Summary:	Nagios plugin to test a PostgreSQL DBMS
Summary(pl.UTF-8):	Wtyczka Nagiosa do sprawdzania systemu baz danych PostgreSQL
Group:		Networking
Requires:	nagios-common
Provides:	nagios-plugins-pgsql = %{version}-%{release}
Obsoletes:	nagios-plugins-pgsql

%description -n nagios-plugin-check_pgsql
This plugin tests a PostgreSQL DBMS to determine whether it is active
and accepting queries. In its current operation, it simply connects to
the specified database, and then disconnects. If no database is
specified, it connects to the template1 database, which is present in
every functioning PostgreSQL DBMS.

%description -n nagios-plugin-check_pgsql -l pl.UTF-8
Ta wtyczka sprawdza serwer baz danych PostgreSQL, aby określić, czy
jest aktywny i przyjmuje zapytania. Aktualnie po prostu łączy się do
określonej bazy danych i rozłącza. Jeśli nie podano bazy danych, łączy
się do bazy danych template1, obecnej w każdym działającym systemie
PostgreSQL.

%package -n nagios-plugin-check_ping
Summary:	Nagios plugin to check host up state with ping
Summary(pl.UTF-8):	Wtyczka Nagiosa do sprawdzania działania hosta przy użyciu programu ping
Group:		Networking
Requires:	iputils-ping >= 1:s20070202-1
Requires:	nagios-common

%description -n nagios-plugin-check_ping
This plugin will use the /bin/ping command to ping the specified host
if the host is alive.

%description -n nagios-plugin-check_ping -l pl.UTF-8
Ta wtyczka używa polecenia /bin/ping do sprawdzenia, czy dany host
działa.

%package -n nagios-plugin-check_radius
Summary:	Nagios plugin to test a radius server to see if it is accepting connections
Summary(pl.UTF-8):	Wtyczka Nagiosa do sprawdzania serwera radius pod kątem przyjmowania połączeń
Group:		Networking
Requires:	nagios-common
Requires:	radiusclient
Provides:	nagios-plugins-radius = %{version}-%{release}
Obsoletes:	nagios-plugins-radius

%description -n nagios-plugin-check_radius
This plugin tests a radius server to see if it is accepting
connections.

%description -n nagios-plugin-check_radius -l pl.UTF-8
Ta wtyczka sprawdza serwer usługi radius, aby zobaczyć, czy przyjmuje
połączenia.

%package -n nagios-plugin-check_sensors
Summary:	Nagios plugin to check hardware status using the lm_sensors package
Summary(pl.UTF-8):	Wtyczka Nagiosa do sprawdzania stanu sprzętu przy użyciu pakietu lm_sensors
Group:		Networking
Requires:	nagios-common
# for utils.sh
Requires:	%{name}-libs = %{version}-%{release}
Requires:	lm_sensors
Provides:	nagios-plugins-sensors = %{version}-%{release}
Obsoletes:	nagios-plugins-sensors

%description -n nagios-plugin-check_sensors
This plugin checks hardware status using the lm_sensors package.

%description -n nagios-plugin-check_sensors -l pl.UTF-8
Ta wtyczka sprawdza stan sprzętu przy użyciu pakietu lm_sensors.

# requisite not packaged in PLD
%package nwstat
Summary:	Nagios plugin nwstat
Summary(pl):	Wtyczka nwstat do Nagiosa
Group:		Networking
Requires:	%{name}-libs = %{version}-%{release}
Requires:	mrtgext
Requires:	nagios-common

%description nwstat
Nagios plugin using MRTGEXT module
<http://forge.novell.com/modules/xfmod/project/?mrtgext>.

%description nwstat -l pl
Wtyczka nagiosa używająca modułu MRTGEXT
<http://forge.novell.com/modules/xfmod/project/?mrtgext>.

%package contrib
Summary:	Contributed nagios plugins
Summary(pl.UTF-8):	Wtyczki przekazane do projektu Nagios
Group:		Networking
Requires:	nagios-common
# for utils.pm, utils.sh, utils.py
Requires:	%{name}-libs = %{version}-%{release}
# check_apache
Suggests:	perl-URI
Suggests:	perl-libwww
# check_apc_ups
Suggests:	net-snmp-utils
# check_arping
Suggests:	perl-Net-Arping
# check_bgpstate
Suggests:	perl-Net-SNMP
Suggests:	whois
# check_traceroute
Suggests:	traceroute
# check_traceroute-pure_perl
Suggests:	perl-Net-Traceroute
# check_temp_fsc
Suggests:	perl-SNMP_Session
# check_smart
Suggests:	smartmontools
# check_smb
Suggests:	samba
# check_adptraid
#Suggests:	dptutil
# unfinished... more deps are actually needed.

%description contrib
Contributed nagios plugins. Some of them work, some do not. Use at
your own risk.

%description contrib -l pl.UTF-8
Wtyczki przekazane do projektu Nagios. Część z nich działa, część nie.

%prep
%setup -q -a1
mv nagios-plugins-config-*/* .
%patch0 -p1
%patch1 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch12 -p1
%patch13 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p0
%patch23 -p0
%patch24 -p1
%patch25 -p0
%patch26 -p0
%patch27 -p1
%patch28 -p1

# bring contribs into shape...
cd contrib
mv check_compaq_insight.{pl,msg}
sed -ne '/--- cut ---/,/--- cut ---/{/--- cut ---/!p}' < \
	check_compaq_insight.msg > check_compaq_insight.pl

sed -i -e '1s,#!.*/bin/perl,#!%{__perl},' \
	check_{oracle_tbs,{snmp_{{disk,process}_monitor,printer},nagios_db,flexlm}.pl}

sed -i -e '1s,#!.*/bin/env,#!%{__python},' \
	check_pcpmetric.py

sed -i -e '1s,#!.*/bin/bash,#!/bin/sh,' \
	check_smb.sh
mv check_appletalk.{pl,orig}
sed -ne '/---/!p;/---/q' < check_appletalk.orig > check_appletalk.pl

chmod a+x check_*.{pl,sh,py}
chmod a+x check_{fan_{cpq,fsc}_present,frontpage,oracle_tbs,pfstate,temp_{cpq,fsc}}

# exists in main
rm check_{breeze,wave}.pl
rm check_flexlm.pl

# more appropriate name
mv check_nagios{,_mysql}.pl

sed -i -e "
	s,use lib '.*/nagios/libexec/?',use lib '%{_pluginlibdir}',
	s,use lib \".*/nagios/libexec/?\",use lib '%{_pluginlibdir}',
	s,require '/usr/libexec/nagios/plugins,require '%{_pluginlibdir},
	s,use lib utils.pm,use lib '%{_pluginlibdir}', # subst not applied to contrib/ dir
	s,/usr/libexec/nagios/plugins,%{_pluginlibdir},
	s,/usr/local/nagios/libexec,%{_pluginlibdir},
	s,/opt/nagios/libexec,%{_pluginlibdir},
	s,/some/path/libexec,%{_pluginlibdir},
	s,/usr/local/libexec/nagios,%{_pluginlibdir},
	s,/usr/local/netsaint/libexec,%{_pluginlibdir},
	s,/usr/local/libexec,%{_pluginlibdir},
" check_* *.pl

cd ..

# remove libtool m4 macro copies, breaks when system libtool is older
rm -rf gl/m4/libtool.m4 gl/m4/lt*.m4

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

# force regen in build
rm -f configure

%build
if [ ! -f configure ]; then
	%{__gettextize}
	%{__libtoolize}
	%{__aclocal} -I m4 -I gl/m4
	%{__autoconf}
	%{__autoheader}
	%{__automake}
fi

%configure \
	--libexecdir=%{_pluginarchdir} \
	--enable-libtap=/usr \
	--with-cgiurl=/nagios/cgi-bin \
	--with-mysql=/usr \
	--with-pgsql=/usr \
	--with-openssl=/usr \
	--with-ping-command='/bin/ping -n -U -w %%d -c %%d %%s' \
	--with-ping6-command='/bin/ping6 -n -U -w %%d -c %%d %%s' \
	--with-ps-command="/bin/ps axwo 'stat uid ppid vsz rss pcpu comm args'" \
	--with-ps-format="%%s %%d %%d %%d %%d %%f %%s %%n" \
	--with-ps-cols=8 \
	--with-ps-varlist="procstat,&procuid,&procppid,&procvsz,&procrss,&procpcpu,procprog,&pos" \
	--with-proc-meminfo=/proc/meminfo \
	--with-proc-loadavg=/proc/loadavg \
	--with-nslookup-command="/usr/bin/nslookup -sil" \
	--with-uptime-command=/usr/bin/uptime \
	--with-rpcinfo-command=/usr/sbin/rpcinfo \
	--with-ntpdate-command=/usr/sbin/ntpdate \
	--with-smbclient-command=/usr/bin/smbclient \
	--with-dig-command=/usr/bin/dig \
	--with-fping-command=/usr/sbin/fping \
	--with-qstat-command=/usr/bin/qstat \
	--with-ssh-command=/usr/bin/ssh \
	--with-snmpget-command=/usr/bin/snmpget \
	--with-snmpgetnext-command=/usr/bin/snmpgetnext \
	--with-df-command='/bin/df -P' \
	--with-apt-get-command=/usr/bin/apt-get \
	--with-qmail-qstat-command=/usr/bin/qmail-qstat \
	--with-mailq-command=/usr/bin/mailq \
	--without-included-regex

%{__make}

# contrib. mostly useless. but you'll never know
cd contrib

%{__cc} %{rpmcflags} check_cluster2.c -o check_cluster2

%{__cc} %{rpmcflags} -I../plugins -I.. -I../gl -I../lib -c check_rbl.c
%{__cc} %{rpmcflags} check_rbl.o -o check_rbl ../plugins/popen.o ../plugins/utils.o ../plugins/netutils.o ../lib/utils_base.o ../gl/libgnu.a

%{__cc} %{rpmcflags} check_timeout.c -o check_timeout

%{__cc} %{rpmcflags} -I../plugins -I.. -I../gl -I../lib -c check_uptime.c
%{__cc} %{rpmcflags} check_uptime.o -o check_uptime ../plugins/popen.o ../plugins/utils.o ../lib/utils_base.o ../gl/libgnu.a

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} install-root -C plugins-root \
	DESTDIR=$RPM_BUILD_ROOT

# for nagios-plugin-check_mysql_perf (at least)
cp -a lib/libnagiosplug.a $RPM_BUILD_ROOT%{_libdir}
cp -a gl/libgnu.a $RPM_BUILD_ROOT%{_libdir}
cp -a plugins/utils.o $RPM_BUILD_ROOT%{_libdir}
cp -a plugins/netutils.o $RPM_BUILD_ROOT%{_libdir}
install -d $RPM_BUILD_ROOT%{_includedir}/nagiosplug/{plugins,gl,lib}
cp -a *.h $RPM_BUILD_ROOT%{_includedir}/nagiosplug
cp -a plugins/*.h $RPM_BUILD_ROOT%{_includedir}/nagiosplug/plugins
cp -a gl/*.h $RPM_BUILD_ROOT%{_includedir}/nagiosplug/gl
cp -a lib/*.h $RPM_BUILD_ROOT%{_includedir}/nagiosplug/lib

install -d $RPM_BUILD_ROOT%{_sysconfdir}
cp -a commands/*.cfg $RPM_BUILD_ROOT%{_sysconfdir}

%find_lang %{name}

# all files with exec permissions are plugins.
install -d $RPM_BUILD_ROOT%{_pluginarchdir}
find contrib -name 'check_*' -type f -perm +1 | while read a; do
	s=$RPM_BUILD_ROOT%{_pluginarchdir}/${a##*/}
	# strip without extensions, if eventually merged to main wouldn't need to rename plugins
	s=${s%.pl}
	s=${s%.sh}
	if [ -f $s ]; then
		# we don't want file from contrib overwrite one from main
		: Duplicate file from contrib: $s
		exit 1
	fi
	install $a $s
done

%if "%{_pluginarchdir}" != "%{_pluginlibdir}"
# move arch independat files to _pluginlibdir
install -d $RPM_BUILD_ROOT%{_pluginlibdir}
mv $(find $RPM_BUILD_ROOT%{_pluginarchdir} -type f | xargs file | awk -F: '!/ELF/{print $1}') $RPM_BUILD_ROOT%{_pluginlibdir}
%{__sed} -i -e 's,use lib "%{_pluginarchdir}",use lib "%{_pluginlibdir}",' $RPM_BUILD_ROOT%{_pluginlibdir}/check_*
%endif

plugins=$(grep -Eoh 'command_line.*USER1\$/[^ ]+' $RPM_BUILD_ROOT%{_sysconfdir}/*.cfg | awk -F/ '{print $NF}' | sort -u)
for plugin in $plugins; do
	[ -x $RPM_BUILD_ROOT%{_pluginarchdir}/$plugin ] && libdir=%{_pluginarchdir} || libdir=%{_pluginlibdir}
	sed -i -e "s,\\\$USER1\\\$/$plugin ,$libdir/$plugin ," $RPM_BUILD_ROOT%{_sysconfdir}/*.cfg
done

cp -a %{SOURCE2} $RPM_BUILD_ROOT%{_pluginlibdir}/utils.php
cp -a contrib/utils.py $RPM_BUILD_ROOT%{_pluginlibdir}
chmod a-x $RPM_BUILD_ROOT%{_pluginlibdir}/utils.*

rm -f $RPM_BUILD_ROOT%{_libdir}/libnagiosplug.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs	-p /sbin/ldconfig
%postun	libs	-p /sbin/ldconfig

%triggerun -- %{name} < 1.4-0.35
%banner -e %{name} <<EOF
Several Nagios plugins have been separated to multiple packages to cut
down unneccessary deps on main package.

Please install %{name}-PACKAGE if you need these plugins.
To revert to previous state just run:
poldek -u nagios-plugins-{snmp,samba,sensors,mysql,pgsql,radius,qstat,ldap,ntp,dns,ssh,procps,fping}

EOF

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ACKNOWLEDGEMENTS AUTHORS BUGS CODING ChangeLog
%doc FAQ LEGAL NEWS README REQUIREMENTS SUPPORT THANKS

# plugins
%attr(755,root,root) %{_pluginarchdir}/check_apt
%attr(755,root,root) %{_pluginarchdir}/check_cluster
%attr(755,root,root) %{_pluginarchdir}/check_cluster2
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/check_disk.cfg
%attr(755,root,root) %{_pluginarchdir}/check_disk
%attr(755,root,root) %{_pluginarchdir}/check_dummy
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/check_http.cfg
%attr(755,root,root) %{_pluginarchdir}/check_http
%attr(755,root,root) %{_pluginarchdir}/check_ide_smart
%attr(755,root,root) %{_pluginarchdir}/check_mrtg
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/check_mrtgtraf.cfg
%attr(755,root,root) %{_pluginarchdir}/check_mrtgtraf
%attr(755,root,root) %{_pluginarchdir}/check_nagios
# req: over-cr >= 0.99.53 http://www.molitor.org/overcr
%attr(755,root,root) %{_pluginarchdir}/check_overcr
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/check_procs.cfg
%attr(755,root,root) %{_pluginarchdir}/check_procs
%attr(755,root,root) %{_pluginarchdir}/check_real
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/check_smtp.cfg
%attr(755,root,root) %{_pluginarchdir}/check_smtp
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/check_ssh.cfg
%attr(755,root,root) %{_pluginarchdir}/check_ssh
%attr(755,root,root) %{_pluginarchdir}/check_time
%attr(755,root,root) %{_pluginarchdir}/check_ups
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/check_users.cfg
%attr(755,root,root) %{_pluginarchdir}/check_users
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/check_swap.cfg
%attr(755,root,root) %{_pluginarchdir}/check_swap
%attr(755,root,root) %{_pluginlibdir}/check_log

# check_tcp and symlinks
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/check_tcp.cfg
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/check_telnet.cfg
%attr(755,root,root) %{_pluginarchdir}/check_tcp
%attr(755,root,root) %{_pluginarchdir}/check_clamd
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/check_ftp.cfg
%attr(755,root,root) %{_pluginarchdir}/check_ftp
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/check_imap.cfg
%attr(755,root,root) %{_pluginarchdir}/check_imap
%attr(755,root,root) %{_pluginarchdir}/check_jabber
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/check_nntp.cfg
%attr(755,root,root) %{_pluginarchdir}/check_nntp
%attr(755,root,root) %{_pluginarchdir}/check_nntps
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/check_pop.cfg
%attr(755,root,root) %{_pluginarchdir}/check_pop
%attr(755,root,root) %{_pluginarchdir}/check_simap
%attr(755,root,root) %{_pluginarchdir}/check_spop
%attr(755,root,root) %{_pluginarchdir}/check_ssmtp
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/check_udp.cfg
%attr(755,root,root) %{_pluginarchdir}/check_udp

# these plugins need suid bit to operate
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/check_dhcp.cfg
%attr(755,root,root) %{_pluginarchdir}/check_dhcp
%attr(755,root,root) %{_pluginarchdir}/check_icmp

# Cannot determine ORACLE_HOME for sid
# probably needs some external programs. can't test
%attr(755,root,root) %{_pluginlibdir}/check_oracle

%files libs
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/libnagiosplug.so.0.0.0
%attr(755,root,root) %{_pluginarchdir}/negate
%attr(755,root,root) %{_pluginarchdir}/urlize

%{_pluginlibdir}/utils.pm
%{_pluginlibdir}/utils.php
%{_pluginlibdir}/utils.sh
%{_pluginlibdir}/utils.py

%files devel
%defattr(644,root,root,755)
%{_libdir}/libgnu.a
%{_libdir}/libnagiosplug.a
%{_libdir}/netutils.o
%{_libdir}/utils.o
%{_includedir}/nagiosplug

%files mysql
%defattr(644,root,root,755)
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/check_mysql.cfg
%attr(755,root,root) %{_pluginarchdir}/check_mysql
%attr(755,root,root) %{_pluginarchdir}/check_mysql_query

%files perl
%defattr(644,root,root,755)
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/check_ircd.cfg
%attr(755,root,root) %{_pluginlibdir}/check_ircd
%attr(755,root,root) %{_pluginlibdir}/check_rpc

# requires license.dat
%attr(755,root,root) %{_pluginlibdir}/check_flexlm

%files samba
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginlibdir}/check_disk_smb

# Not to be confused with nagios-snmp-plugins
%files snmp
%defattr(644,root,root,755)
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/check_snmp.cfg
%attr(755,root,root) %{_pluginarchdir}/check_snmp
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/check_hpjd.cfg
%attr(755,root,root) %{_pluginarchdir}/check_hpjd
%attr(755,root,root) %{_pluginlibdir}/check_ifoperstatus
%attr(755,root,root) %{_pluginlibdir}/check_ifstatus
%attr(755,root,root) %{_pluginlibdir}/check_wave
%attr(755,root,root) %{_pluginlibdir}/check_breeze

%files ssh
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginarchdir}/check_by_ssh

%files -n nagios-plugin-check_dig
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginarchdir}/check_dig

%files -n nagios-plugin-check_dns
%defattr(644,root,root,755)
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/check_dns.cfg
%attr(755,root,root) %{_pluginarchdir}/check_dns

%files -n nagios-plugin-check_file_age
%defattr(644,root,root,755)
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/check_file_age.cfg
%attr(755,root,root) %{_pluginlibdir}/check_file_age

%files -n nagios-plugin-check_fping
%defattr(644,root,root,755)
%attr(2755,root,adm) %{_pluginarchdir}/check_fping

%files -n nagios-plugin-check_game
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginarchdir}/check_game

%files -n nagios-plugin-check_ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginarchdir}/check_ldap
%attr(755,root,root) %{_pluginarchdir}/check_ldaps

%files -n nagios-plugin-check_load
%defattr(644,root,root,755)
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/check_load.cfg
%attr(755,root,root) %{_pluginarchdir}/check_load

%files -n nagios-plugin-check_mailq
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginlibdir}/check_mailq

%files -n nagios-plugin-check_nt
%defattr(644,root,root,755)
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/check_nt.cfg
%attr(755,root,root) %{_pluginarchdir}/check_nt

%files -n nagios-plugin-check_ntp
%defattr(644,root,root,755)
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/check_ntp.cfg
%attr(755,root,root) %{_pluginarchdir}/check_ntp
%attr(755,root,root) %{_pluginarchdir}/check_ntp_peer
%attr(755,root,root) %{_pluginarchdir}/check_ntp_time

%files -n nagios-plugin-check_pgsql
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginarchdir}/check_pgsql

%files -n nagios-plugin-check_ping
%defattr(644,root,root,755)
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/check_ping.cfg
%attr(2755,root,adm) %{_pluginarchdir}/check_ping

%files -n nagios-plugin-check_radius
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginarchdir}/check_radius

%files -n nagios-plugin-check_sensors
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginlibdir}/check_sensors

%files contrib
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginarchdir}/check_nwstat
%attr(755,root,root) %{_pluginarchdir}/check_rbl
%attr(755,root,root) %{_pluginarchdir}/check_timeout
%attr(755,root,root) %{_pluginarchdir}/check_uptime

%attr(755,root,root) %{_pluginlibdir}/check_adptraid
%attr(755,root,root) %{_pluginlibdir}/check_apache
%attr(755,root,root) %{_pluginlibdir}/check_apc_ups
%attr(755,root,root) %{_pluginlibdir}/check_appletalk
%attr(755,root,root) %{_pluginlibdir}/check_arping
%attr(755,root,root) %{_pluginlibdir}/check_asterisk
%attr(755,root,root) %{_pluginlibdir}/check_axis
%attr(755,root,root) %{_pluginlibdir}/check_backup
%attr(755,root,root) %{_pluginlibdir}/check_bgpstate
%attr(755,root,root) %{_pluginlibdir}/check_compaq_insight
%attr(755,root,root) %{_pluginlibdir}/check_digitemp
%attr(755,root,root) %{_pluginlibdir}/check_dlswcircuit
%attr(755,root,root) %{_pluginlibdir}/check_dns_random
%attr(755,root,root) %{_pluginlibdir}/check_email_loop
%attr(755,root,root) %{_pluginlibdir}/check_fan_cpq_present
%attr(755,root,root) %{_pluginlibdir}/check_fan_fsc_present
%attr(755,root,root) %{_pluginlibdir}/check_flexlm
%attr(755,root,root) %{_pluginlibdir}/check_frontpage
%attr(755,root,root) %{_pluginlibdir}/check_hprsc
%attr(755,root,root) %{_pluginlibdir}/check_hw
%attr(755,root,root) %{_pluginlibdir}/check_ica_master_browser
%attr(755,root,root) %{_pluginlibdir}/check_ica_metaframe_pub_apps
%attr(755,root,root) %{_pluginlibdir}/check_ica_program_neigbourhood
%attr(755,root,root) %{_pluginlibdir}/check_inodes-freebsd
%attr(755,root,root) %{_pluginlibdir}/check_inodes
%attr(755,root,root) %{_pluginlibdir}/check_javaproc
%attr(755,root,root) %{_pluginlibdir}/check_joy
%attr(755,root,root) %{_pluginlibdir}/check_linux_raid
%attr(755,root,root) %{_pluginlibdir}/check_lmmon
%attr(755,root,root) %{_pluginlibdir}/check_log2
%attr(755,root,root) %{_pluginlibdir}/check_lotus
%attr(755,root,root) %{_pluginlibdir}/check_maxchannels
%attr(755,root,root) %{_pluginlibdir}/check_maxwanstate
%attr(755,root,root) %{_pluginlibdir}/check_mem
%attr(755,root,root) %{_pluginlibdir}/check_ms_spooler
%attr(755,root,root) %{_pluginlibdir}/check_mssql
%attr(755,root,root) %{_pluginlibdir}/check_nagios_db
%attr(755,root,root) %{_pluginlibdir}/check_nagios_db_pg
%attr(755,root,root) %{_pluginlibdir}/check_nagios_mysql
%attr(755,root,root) %{_pluginlibdir}/check_netapp
%attr(755,root,root) %{_pluginlibdir}/check_nmap.py
%attr(755,root,root) %{_pluginlibdir}/check_ora_table_space
%attr(755,root,root) %{_pluginlibdir}/check_oracle_instance
%attr(755,root,root) %{_pluginlibdir}/check_oracle_tbs
%attr(755,root,root) %{_pluginlibdir}/check_pcpmetric.py
%attr(755,root,root) %{_pluginlibdir}/check_pfstate
%attr(755,root,root) %{_pluginlibdir}/check_qmailq
%attr(755,root,root) %{_pluginlibdir}/check_remote_nagios_status
%attr(755,root,root) %{_pluginlibdir}/check_rrd_data
%attr(755,root,root) %{_pluginlibdir}/check_sap
%attr(755,root,root) %{_pluginlibdir}/check_smart
%attr(755,root,root) %{_pluginlibdir}/check_smb
%attr(755,root,root) %{_pluginlibdir}/check_snmp_disk_monitor
%attr(755,root,root) %{_pluginlibdir}/check_snmp_printer
%attr(755,root,root) %{_pluginlibdir}/check_snmp_process_monitor
%attr(755,root,root) %{_pluginlibdir}/check_snmp_procs
%attr(755,root,root) %{_pluginlibdir}/check_sockets
%attr(755,root,root) %{_pluginlibdir}/check_temp_cpq
%attr(755,root,root) %{_pluginlibdir}/check_temp_fsc
%attr(755,root,root) %{_pluginlibdir}/check_traceroute-pure_perl
%attr(755,root,root) %{_pluginlibdir}/check_traceroute
%attr(755,root,root) %{_pluginlibdir}/check_vcs
%attr(755,root,root) %{_pluginlibdir}/check_wins
