# TODO:
# - package requisites for unifished packages -nsclient and -nwstat
#   REQUIREMENTS explains the dependencies.
# - check_ping doesn't work on my test machine, somewhy

%bcond_without	gettext0143		# without gettext-0.14.3
Summary:	Host/service/network monitoring program plugins for Nagios
Summary(pl):	Wtyczki do monitorowania hostów/us³ug/sieci dla Nagiosa
Name:		nagios-plugins
Version:	1.4
Release:	0.26
License:	GPL v2
Group:		Networking
Source0:	http://dl.sourceforge.net/nagiosplug/%{name}-%{version}.tar.gz
# Source0-md5:	9b21b92acc4b2b0dbb2d12bca6b27582
Patch0:		%{name}-configure.patch
Patch2:		%{name}-tainted.patch
Patch3:		%{name}-contrib-API.patch
Patch4:		%{name}-gettext.patch
Patch5:		%{name}-subst.patch
URL:		http://nagiosplug.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	mysql-devel
BuildRequires:	net-snmp-utils
BuildRequires:	net-snmp-devel
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel >= 0.9.7d
%if %{with gettext0143}
BuildRequires:	gettext-devel >= 0.14.3
%else
BuildRequires:	gettext-devel
%endif
BuildRequires:	iputils-ping
BuildRequires:	postgresql-devel
BuildRequires:	perl-Net-SNMP
BuildRequires:	radiusclient-devel
BuildRequires:	rpmbuild(macros) >= 1.177
PreReq:		nagios-core
Conflicts:	iputils-ping < 1:ss020124
Obsoletes:	netsaint-plugins
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_libdir}/nagios/plugins

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
Requires:	%{name} = %{epoch}:%{version}-%{release}
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
Requires:	%{name} = %{epoch}:%{version}-%{release}
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
Requires:	%{name} = %{epoch}:%{version}-%{release}
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
Requires:	%{name} = %{epoch}:%{version}-%{release}
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
Requires:	%{name} = %{epoch}:%{version}-%{release}
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

%package contrib
Summary:	Contributed nagios plugins
Group:		Networking
# for utils.pm, utils.sh
Requires:	%{name} = %{epoch}:%{version}-%{release}
# check_apache
Requires:	perl-libwww
Requires:	perl-URI
# check_apc_ups.pl
Requires:	net-snmp-utils
# check_arping.pl
#Requires:	perl(Net::Arping) - not found
# check_bgpstate.pl
Requires:	whois
Requires:	perl-Net-SNMP
# check_traceroute.pl
Requires:	traceroute
# check_traceroute-pure_perl.pl
Requires:	perl-Net-Traceroute
# check_mysqlslave.pl
Requires:	perl-DBI
# check_temp_fsc
Requires:	perl-SNMP_Session
# check_smart.pl
Requires:	smartmontools
# check_smb.sh
Requires:	samba
# check_adptraid.sh
#Requires:	dptutil

%description contrib
Contributed nagios plugins. Some of them work, some do not.

%prep
%setup -q
%patch0 -p1
%patch2 -p1
%patch3 -p1
%{?with_gettext0143:%patch4 -p1}
%patch5 -p1

# bring contribs into shape...
cd contrib
mv check_compaq_insight.{pl,msg}
sed -ne '/--- cut ---/,/--- cut ---/{/--- cut ---/!p}' < \
	check_compaq_insight.msg > check_compaq_insight.pl

sed -i -e '1s,#!.*/bin/perl,#!%{__perl},' \
	check_{oracle_tbs,{snmp_{{disk,process}_monitor,printer},nagios_db,flexlm,mysql}.pl}

sed -i -e "
	s,use lib '/usr/local/nagios/libexec/',use lib '%{_plugindir}',
	s,require '/usr/libexec/nagios/plugins',require '%{_plugindir}',
	s,use lib utils.pm,use lib '%{_plugindir}',
" *.pl

mv check_appletalk.{pl,orig}
sed -ne '/---/!p;/---/q' < check_appletalk.orig > check_appletalk.pl

chmod a+x check_*.{pl,sh,py}
chmod a+x check_{fan_{cpq,fsc}_present,frontpage,oracle_tbs,pfstate,temp_{cpq,fsc}}

# same as in main
rm -f check_{breeze,wave}.pl

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	--libexecdir=%{_plugindir} \
	--with-cgiurl=/nagios/cgi-bin \
	--with-mysql=%{_prefix} \
	--with-pgsql=%{_prefix} \
	--with-ping-command='/bin/ping -n -U -w %%d -c %%d %%s' \
	--with-ping6-command='/bin/ping6 -n -U -w %%d -c %%d %%s' \
	--with-ps-command="/bin/ps axwo 'stat uid ppid vsz rss pcpu comm args'" \
	--with-ps-format="%%s %%d %%d %%d %%d %%f %%s %%n" \
	--with-ps-cols=8 \
	--with-ps-varlist="procstat,&procuid,&procppid,&procvsz,&procrss,&procpcpu,procprog,&pos" \
	--with-proc-meminfo=/proc/meminfo \
	--with-nslookup-command="/usr/bin/nslookup -sil" \
	--with-uptime-command=/usr/bin/uptime \
	--with-rpcinfo-command=/usr/sbin/rpcinfo \
	--with-ntpdate-command=/usr/sbin/ntpdate \
	--with-smbclient-command=/usr/bin/smbclient \
	--with-dig-command=/usr/bin/dig \
	--with-fping-command=/usr/sbin/fping \
	--with-qstat-command=/usr/bin/qstat \

%{__make}


# contrib. mostly useless. but you'll never know
cd contrib

%{__cc} %{rpmcflags} check_cluster.c -o check_cluster
%{__cc} %{rpmcflags} check_cluster2.c -o check_cluster2

%{__cc} %{rpmcflags} check_mysql.c -c $(mysql_config --cflags) -I../plugins -I.. -I../lib
%{__cc} %{rpmcflags} check_mysql.o -o check_mysql2 $(mysql_config --libs)

%{__cc} %{rpmcflags} -I../plugins -I.. -I../lib -c check_rbl.c
%{__cc} %{rpmcflags} check_rbl.o -o check_rbl ../plugins/popen.o ../plugins/utils.o ../plugins/netutils.o

%{__cc} %{rpmcflags} check_timeout.c -o check_timeout

%{__cc} %{rpmcflags} -I../plugins -I.. -I../lib -c check_uptime.c
%{__cc} %{rpmcflags} check_uptime.o -o check_uptime ../plugins/popen.o ../plugins/utils.o

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

cd contrib
# all files with exec permissions are plugins.
find -name 'check_*' -type f -perm +1 | xargs -ri install {} $RPM_BUILD_ROOT%{_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%triggerun -- %{name} <= 1.3.1-2
%banner -e %{name} <<EOF
Plugins for snmp, samba, sensors, mysql, pgsql, radius, qstat
have been separated into subpackages.
Please install %{name}-PACKAGE if you need these plugins.

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
%{_plugindir}/check_by_ssh
%{_plugindir}/check_dhcp
%{_plugindir}/check_dig
%{_plugindir}/check_disk
%{_plugindir}/check_dns
%{_plugindir}/check_dummy
%{_plugindir}/check_file_age
%{_plugindir}/check_fping
%{_plugindir}/check_ftp
%{_plugindir}/check_http
%{_plugindir}/check_icmp
%{_plugindir}/check_imap
%{_plugindir}/check_ircd
%{_plugindir}/check_load
%{_plugindir}/check_log
%{_plugindir}/check_mailq
%{_plugindir}/check_mrtg
%{_plugindir}/check_mrtgtraf
%{_plugindir}/check_nagios
%{_plugindir}/check_nntp
%{_plugindir}/check_ntp
%{_plugindir}/check_overcr
%attr(2755,root,adm) %{_plugindir}/check_ping
%{_plugindir}/check_pop
%{_plugindir}/check_procs
%{_plugindir}/check_real
%{_plugindir}/check_rpc
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

# requries license.dat
%{_plugindir}/check_flexlm

# Cannot determine ORACLE_HOME for sid
# probably needs some external programs. can't test
%{_plugindir}/check_oracle

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

#%files nsclient
#%defattr(755,root,root,755)
#%{_plugindir}/check_nt

#%files nwstat
#%defattr(755,root,root,755)
#%{_plugindir}/check_nwstat

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
%{_plugindir}/check_cluster
%{_plugindir}/check_cluster2
%{_plugindir}/check_compaq_insight.pl
#%{_plugindir}/check_cpqarray
%{_plugindir}/check_digitemp.pl
%{_plugindir}/check_disk_snmp.pl
%{_plugindir}/check_dl_size.pl
%{_plugindir}/check_dlswcircuit.pl
%{_plugindir}/check_dns_random.pl
%{_plugindir}/check_email_loop.pl
%{_plugindir}/check_fan_cpq_present
%{_plugindir}/check_fan_fsc_present
%{_plugindir}/check_flexlm.pl
%{_plugindir}/check_frontpage
%{_plugindir}/check_ftpget.pl
#%{_plugindir}/check_hltherm.c
%{_plugindir}/check_hprsc.pl
#%{_plugindir}/check_http-with-client-certificate.c
%{_plugindir}/check_hw.sh
%{_plugindir}/check_ica_master_browser.pl
%{_plugindir}/check_ica_metaframe_pub_apps.pl
%{_plugindir}/check_ica_program_neigbourhood.pl
%{_plugindir}/check_inodes-freebsd.pl
%{_plugindir}/check_inodes.pl
#%{_plugindir}/check_ipxping.c
%{_plugindir}/check_javaproc.pl
%{_plugindir}/check_joy.sh
%{_plugindir}/check_linux_raid.pl
%{_plugindir}/check_lmmon.pl
%{_plugindir}/check_log2.pl
#%{_plugindir}/check_logins.c
%{_plugindir}/check_lotus.pl
%{_plugindir}/check_maxchannels.pl
%{_plugindir}/check_maxwanstate.pl
%{_plugindir}/check_mem.pl
%{_plugindir}/check_ms_spooler.pl
%{_plugindir}/check_mssql.sh
#%{_plugindir}/check_mysql.c
%{_plugindir}/check_mysql.pl
%{_plugindir}/check_mysqlslave.pl
%{_plugindir}/check_nagios.pl
%{_plugindir}/check_nagios_db.pl
%{_plugindir}/check_nagios_db_pg.pl
%{_plugindir}/check_netapp.pl
%{_plugindir}/check_nmap.py
%{_plugindir}/check_nt
%{_plugindir}/check_nwstat
%{_plugindir}/check_nwstat.pl
%{_plugindir}/check_ora_table_space.pl
%{_plugindir}/check_oracle_instance.pl
%{_plugindir}/check_oracle_tbs
%{_plugindir}/check_pcpmetric.py
%{_plugindir}/check_pfstate
%{_plugindir}/check_pop3.pl
%{_plugindir}/check_procl.sh
%{_plugindir}/check_procr.sh
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
%{_plugindir}/check_mysql2
%{_plugindir}/check_wins.pl
