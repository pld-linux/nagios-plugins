# TODO:
# - package requisites for unifished packages -nsclient and -nwstat
#   REQUIREMENTS explains the dependencies.
%include	/usr/lib/rpm/macros.perl
Summary:	Host/service/network monitoring program plugins for Nagios
Summary(pl):	Wtyczki do monitorowania hostów/us³ug/sieci dla Nagiosa
Name:		nagios-plugins
Version:	1.4.3
Release:	2.1
License:	GPL v2
Group:		Networking
Source0:	http://dl.sourceforge.net/nagiosplug/%{name}-%{version}.tar.gz
# Source0-md5:	2c40fc69d51cc979e85150870a1daa93
Patch0:		%{name}-tainted.patch
Patch1:		%{name}-contrib-API.patch
Patch2:		%{name}-gettext.patch
Patch3:		%{name}-subst.patch
Patch4:		%{name}-noroot.patch
Patch5:		%{name}-check_ping-socket-filter-warning.patch
URL:		http://nagiosplug.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel >= 0.14.3
BuildRequires:	mysql-devel
BuildRequires:	net-snmp-devel
BuildRequires:	openldap-devel >= 2.3.0
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	perl-Net-SNMP
BuildRequires:	postgresql-devel
BuildRequires:	radiusclient-devel
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.177
Requires:	nagios-core
Obsoletes:	netsaint-plugins
Conflicts:	iputils-ping < 1:ss021109-3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_libdir}/nagios/plugins
# Not available in Ac
%define		_noautoreq	'perl(DBD::Oracle)' 'perl(Net::Arping)' 'perl(RRD::File)' 'perl(a)' 'perl(packet_utils)' 'perl(snmputil)'

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

# NOTE for sub package requires:
# use Requires:	%{name} = %{epoch}:%{version}-%{release} for utils.sh or utils.pm
# and Requires:	nagios-core if just plugins directory needed

%package snmp
Summary:	Nagios plugins using SNMP protocol to query information
Summary(pl):	Wtyczki Nagiosa u¿ywaj±ce protoko³u SNMP w celu uzyskania informacji
Group:		Networking
# for utils.pm
Requires:	%{name} = %{epoch}:%{version}-%{release}
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
# for utils.pm
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	samba-client

%description samba
Perl Check SMB Disk plugin for Nagios.

%description samba -l pl
Perlowa wtyczka dla Nagiosa sprawdzaj±ca dyski SMB.

%package sensors
Summary:	Nagios plugin to check hardware status using the lm_sensors package
Summary(pl):	Wtyczka Nagiosa do sprawdzania stanu sprzêtu przy u¿yciu pakietu lm_sensors
Group:		Networking
# for utils.sh
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	lm_sensors

%description sensors
This plugin checks hardware status using the lm_sensors package.

%description sensors -l pl
Ta wtyczka sprawdza stan sprzêtu przy u¿yciu pakietu lm_sensors.

%package mysql
Summary:	Nagios plugin to test a MySQL DBMS
Summary(pl):	Wtyczka Nagiosa do sprawdzania systemu baz danych MySQL
Group:		Networking
Requires:	mysql-libs
Requires:	nagios-core

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
Requires:	nagios-core
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
Requires:	nagios-core
Requires:	radiusclient

%description radius
This plugin tests a radius server to see if it is accepting
connections.

%description radius -l pl
Ta wtyczka sprawdza serwer us³ugi radius, aby zobaczyæ, czy przyjmuje
po³±czenia.

%package qstat
Summary:	Nagios plugin to check status of Internet game servers
Summary(pl):	Wtyczka Nagiosa do sprawdzania stanu serwerów gier internetowych
Group:		Networking
Requires:	nagios-core
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
Ta wtyczka u¿ywa polecenia 'qstat' - popularnego narzêdzia do zapytañ
o stan serwerów gier.

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
Requires:	nagios-core
Requires:	openldap-libs

%description ldap
Nagios plugin to check LDAP servers.

%description ldap -l pl
Wtyczka Nagiosa do sprawdzania serwerów LDAP.

%package ntp
Summary:	Nagios plugin to check time using NTP protocol
Summary(pl):	Wtyczka Nagiosa do sprawdzania czasu przy u¿yciu protoko³u NTP
Group:		Networking
# for utils.pm
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	ntp-client

%description ntp
Checks the local timestamp offset versus <host> with ntpdate. Checks
the jitter/dispersion of clock signal between <host> and its sys.peer
with ntpq.

%description ntp -l pl
Ta wtyczka sprawdza przesuniêcie lokalnego czasu wzglêdem danego hosta
przy u¿yciu ntpdate. Sprawdza wahania/dyspersjê sygna³u zegara
pomiêdzy hostem a jego sys.peer przy u¿yciu ntpq.

%package dns
Summary:	Nagios plugin to check DNS with nslookup
Summary(pl):	Wtyczka Nagiosa do sprawdzania DNS-u przy u¿yciu nslookup
Group:		Networking
Requires:	bind-utils
Requires:	nagios-core

%description dns
This plugin uses the nslookup program to obtain the IP address for the
given host/domain query. A optional DNS server to use may be
specified. If no DNS server is specified, the default server(s)
specified in /etc/resolv.conf will be used.

%description dns -l pl
Ta wtyczka u¿ywa programu nslookup do uzyskania adresu IP danego dla
danego zapytania o host/domenê. Mo¿na opcjonalnie podaæ serwer DNS,
który ma byæ u¿yty. Je¶li nie podano serwera DNS, u¿ywany jest
domy¶lny serwer (lub serwery) podany w /etc/resolv.conf.

%package dig
Summary:	Nagios plugin to check DNS servers with dig
Summary(pl):	Wtyczka Nagiosa do sprawdzania DNS-u przy u¿yciu programu dig
Group:		Networking
Requires:	bind-utils
Requires:	nagios-core

%description dig
Test the DNS service on the specified host using dig.

%description dig -l pl
Ta wtyczka sprawdza us³ugê DNS na podanym ho¶cie przy u¿yciu programu
dig.

%package ssh
Summary:	Nagios plugins to check remote services via SSH
Summary(pl):	Wtyczki Nagiosa do sprawdzania zdalnych us³ug po SSH
Group:		Networking
Requires:	nagios-core
Requires:	openssh-clients

%description ssh
This plugin uses SSH to execute commands on a remote host.

%description ssh -l pl
Ta wtyczka u¿ywa SSH do wykonywania poleceñ na zdalnym ho¶cie.

%package procps
Summary:	Nagios plugin to check uptime using procps
Summary(pl):	Wtyczka Nagiosa do sprawdzania uptime'u przy u¿yciu procps
Group:		Networking
Requires:	nagios-core
Requires:	procps

%description procps
Nagios plugin to check uptime using procps.

%description procps -l pl
Wtyczka Nagiosa do sprawdzania uptime'u przy u¿yciu procps.

%package fping
Summary:	Nagios plugin to check host up state with fping
Summary(pl):	Wtyczka Nagiosa do sprawdzania dzia³ania hosta przy u¿yciu programu fping
Group:		Networking
Requires:	nagios-core
Requires:	procps

%description fping
This plugin will use the /bin/fping command to ping the specified host
for a fast check if the host is alive.

%description fping -l pl
Ta wtyczka u¿ywa polecenia /bin/fping do szybkiego sprawdzenia, czy
dany host dzia³a.

%package perl
Summary:	Nagios plugins written in Perl
Group:		Networking
# for utils.pm
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description perl
This package contains Nagios plugins written in Perl.

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

%package contrib
Summary:	Contributed nagios plugins
Summary(pl):	Wtyczki przekazane do projektu Nagios
Group:		Networking
# for utils.pm, utils.sh
Requires:	%{name} = %{epoch}:%{version}-%{release}
# check_apache
Requires:	perl-URI
Requires:	perl-libwww
# check_apc_ups.pl
Requires:	net-snmp-utils
# check_arping.pl
#Requires:	perl(Net::Arping) - not found
# check_bgpstate.pl
Requires:	perl-Net-SNMP
Requires:	whois
# check_traceroute.pl
Requires:	traceroute
# check_traceroute-pure_perl.pl
Requires:	perl-Net-Traceroute
# check_temp_fsc
Requires:	perl-SNMP_Session
# check_smart.pl
Requires:	smartmontools
# check_smb.sh
Requires:	samba
# check_adptraid.sh
#Requires:	dptutil
# unfinished... more deps are actually needed.

%description contrib
Contributed nagios plugins. Some of them work, some do not. Use at
your own risk.

%description contrib -l pl
Wtyczki przekazane do projektu Nagios. Czê¶æ z nich dzia³a, czê¶æ nie.

%prep
%setup -q %{?_snap:-n %{name}-HEAD-%{_snap}}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

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

sed -i -e "
	s,use lib '.*/nagios/libexec/',use lib '%{_plugindir}',
	s,require '/usr/libexec/nagios/plugins,require '%{_plugindir},
	s,use lib utils.pm,use lib '%{_plugindir}',
" *.pl

mv check_appletalk.{pl,orig}
sed -ne '/---/!p;/---/q' < check_appletalk.orig > check_appletalk.pl

chmod a+x check_*.{pl,sh,py}
chmod a+x check_{fan_{cpq,fsc}_present,frontpage,oracle_tbs,pfstate,temp_{cpq,fsc}}

# exists in main
rm check_{breeze,wave}.pl

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	--libexecdir=%{_plugindir} \
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

%{__make}


# contrib. mostly useless. but you'll never know
cd contrib

%{__cc} %{rpmcflags} check_cluster2.c -o check_cluster2

%{__cc} %{rpmcflags} -I../plugins -I.. -I../lib -c check_rbl.c
%{__cc} %{rpmcflags} check_rbl.o -o check_rbl ../plugins/popen.o ../plugins/utils.o ../plugins/netutils.o

%{__cc} %{rpmcflags} check_timeout.c -o check_timeout

%{__cc} %{rpmcflags} -I../plugins -I.. -I../lib -c check_uptime.c
%{__cc} %{rpmcflags} check_uptime.o -o check_uptime ../plugins/popen.o ../plugins/utils.o

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} install-root -C plugins-root \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

cd contrib
# all files with exec permissions are plugins.
find -name 'check_*' -type f -perm +1 | xargs -ri install {} $RPM_BUILD_ROOT%{_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%triggerun -- %{name} <= 1.4-0.34
%banner -e %{name} <<EOF
Several Nagios plugins have been separated to multiple packages to cut
down unneccessary deps on main package.

Please install %{name}-PACKAGE if you need these plugins.
To revert to previous state just run:
poldek -u nagios-plugins-{snmp,samba,sensors,mysql,pgsql,radius,qstat,ldap,ntp,dns,ssh,procps,fping}

EOF

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ACKNOWLEDGEMENTS AUTHORS BUGS CHANGES CODING ChangeLog
%doc FAQ LEGAL NEWS README REQUIREMENTS SUPPORT THANKS

%defattr(755,root,root,755)
# utils
%{_plugindir}/negate
%{_plugindir}/urlize
%{_plugindir}/utils.pm
%{_plugindir}/utils.sh

# plugins
%{_plugindir}/check_cluster2
%{_plugindir}/check_disk
%{_plugindir}/check_dummy
%{_plugindir}/check_ftp
%{_plugindir}/check_http
%{_plugindir}/check_imap
%{_plugindir}/check_log
%{_plugindir}/check_mrtg
%{_plugindir}/check_mrtgtraf
%{_plugindir}/check_nagios
%{_plugindir}/check_nntp
# req: over-cr >= 0.99.53 http://www.molitor.org/overcr
%{_plugindir}/check_overcr
%attr(2755,root,adm) %{_plugindir}/check_ping
%{_plugindir}/check_pop
%{_plugindir}/check_procs
%{_plugindir}/check_real
%{_plugindir}/check_simap
%{_plugindir}/check_smtp
%{_plugindir}/check_spop
%{_plugindir}/check_ssh
%{_plugindir}/check_tcp
%{_plugindir}/check_time
%{_plugindir}/check_udp
%{_plugindir}/check_ups
%{_plugindir}/check_users
%{_plugindir}/check_swap

# these plugins need suid bit to operate
%{_plugindir}/check_dhcp
%{_plugindir}/check_icmp


# Cannot determine ORACLE_HOME for sid
# probably needs some external programs. can't test
%{_plugindir}/check_oracle

%files perl
%defattr(755,root,root,755)
%{_plugindir}/check_file_age
%{_plugindir}/check_ircd
%{_plugindir}/check_mailq
%{_plugindir}/check_rpc

# requires license.dat
%{_plugindir}/check_flexlm

# Not to be confused with nagios-snmp-plugins
%files snmp
%defattr(755,root,root,755)
%{_plugindir}/check_snmp
%{_plugindir}/check_hpjd
%{_plugindir}/check_ifoperstatus
%{_plugindir}/check_ifstatus
%{_plugindir}/check_wave
%{_plugindir}/check_breeze

%files samba
%defattr(755,root,root,755)
%{_plugindir}/check_disk_smb

%files sensors
%defattr(755,root,root,755)
%{_plugindir}/check_sensors

%files mysql
%defattr(755,root,root,755)
%{_plugindir}/check_mysql
%{_plugindir}/check_mysql_query

%files pgsql
%defattr(755,root,root,755)
%{_plugindir}/check_pgsql

%files radius
%defattr(755,root,root,755)
%{_plugindir}/check_radius

%files qstat
%defattr(755,root,root,755)
%{_plugindir}/check_game

%files ldap
%defattr(755,root,root,755)
%{_plugindir}/check_ldap

%files ntp
%defattr(755,root,root,755)
%{_plugindir}/check_ntp

%files dns
%defattr(755,root,root,755)
%{_plugindir}/check_dns

%files dig
%defattr(755,root,root,755)
%{_plugindir}/check_dig

%files ssh
%defattr(755,root,root,755)
%{_plugindir}/check_by_ssh

%files procps
%defattr(755,root,root,755)
%{_plugindir}/check_load

%files fping
%defattr(755,root,root,755)
%attr(2755,root,adm) %{_plugindir}/check_fping

%files contrib
%defattr(755,root,root,755)
%{_plugindir}/check_adptraid.sh
%{_plugindir}/check_apache.pl
%{_plugindir}/check_apc_ups.pl
%{_plugindir}/check_appletalk.pl
%{_plugindir}/check_arping.pl
%{_plugindir}/check_asterisk.pl
%{_plugindir}/check_axis.sh
%{_plugindir}/check_backup.pl
%{_plugindir}/check_bgpstate.pl
%{_plugindir}/check_compaq_insight.pl
%{_plugindir}/check_digitemp.pl
%{_plugindir}/check_disk_snmp.pl
%{_plugindir}/check_dlswcircuit.pl
%{_plugindir}/check_dns_random.pl
%{_plugindir}/check_email_loop.pl
%{_plugindir}/check_fan_cpq_present
%{_plugindir}/check_fan_fsc_present
%{_plugindir}/check_flexlm.pl
%{_plugindir}/check_frontpage
%{_plugindir}/check_hprsc.pl
%{_plugindir}/check_hw.sh
%{_plugindir}/check_ica_master_browser.pl
%{_plugindir}/check_ica_metaframe_pub_apps.pl
%{_plugindir}/check_ica_program_neigbourhood.pl
%{_plugindir}/check_inodes-freebsd.pl
%{_plugindir}/check_inodes.pl
%{_plugindir}/check_javaproc.pl
%{_plugindir}/check_joy.sh
%{_plugindir}/check_linux_raid.pl
%{_plugindir}/check_lmmon.pl
%{_plugindir}/check_log2.pl
%{_plugindir}/check_lotus.pl
%{_plugindir}/check_maxchannels.pl
%{_plugindir}/check_maxwanstate.pl
%{_plugindir}/check_mem.pl
%{_plugindir}/check_ms_spooler.pl
%{_plugindir}/check_mssql.sh
%{_plugindir}/check_nagios.pl
%{_plugindir}/check_nagios_db.pl
%{_plugindir}/check_nagios_db_pg.pl
%{_plugindir}/check_netapp.pl
%{_plugindir}/check_nmap.py
%{_plugindir}/check_nt
%{_plugindir}/check_nwstat
%{_plugindir}/check_ora_table_space.pl
%{_plugindir}/check_oracle_instance.pl
%{_plugindir}/check_oracle_tbs
%{_plugindir}/check_pcpmetric.py
%{_plugindir}/check_pfstate
%{_plugindir}/check_qmailq.pl
%{_plugindir}/check_rbl
%{_plugindir}/check_remote_nagios_status.pl
%{_plugindir}/check_rrd_data.pl
%{_plugindir}/check_sap.sh
%{_plugindir}/check_smart.pl
%{_plugindir}/check_smb.sh
%{_plugindir}/check_snmp_disk_monitor.pl
%{_plugindir}/check_snmp_printer.pl
%{_plugindir}/check_snmp_process_monitor.pl
%{_plugindir}/check_snmp_procs.pl
%{_plugindir}/check_sockets.pl
%{_plugindir}/check_sybase
%{_plugindir}/check_temp_cpq
%{_plugindir}/check_temp_fsc
%{_plugindir}/check_timeout
%{_plugindir}/check_traceroute-pure_perl.pl
%{_plugindir}/check_traceroute.pl
%{_plugindir}/check_uptime
%{_plugindir}/check_vcs.pl
%{_plugindir}/check_wins.pl
