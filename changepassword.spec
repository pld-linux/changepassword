#
# Conditional build:
%bcond_without	samba	# without samba passwords support
%bcond_without	squid	# without squid passwords support

#TODO
# - move cgi binary to /usr/share/changepassword
# - write changepassword.conf for apache redirection + execution
# - get sources for libdes and compile then instead of using
#   precompiled version for x86!!!
Summary:	ChangePassword
Summary(pl):	ChangePassword - modyfikator hase³
Name:		changepassword
Version:	0.9
Release:	1
License:	GPL
Group:		Networking/Admin
Source0:	http://dl.sourceforge.net/changepassword/%{name}-%{version}.tar.gz
# Source0-md5:	7449a80c65db2e37c0aa3bb709926127
# Source0-size:	220145
Source1:	pldlogo.png
URL:		http://changepassword.sourceforge.net/
Requires:	apache
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_cgidir		/home/services/httpd/cgi-bin

%description
ChangePassword modifies the passwords of passwd, Samba, and Squid
through the Web. All passwords are syncronized and changed in real
time through browsers like Mozilla, Netscape, IE, Opera, and others.

%description -l pl
ChangePassword modyfikuje has³a dla passwd, Samby i Squida za
po¶rednictwem interfejsu WWW. Wszystkie has³a s± synchronizowane i
zmieniane w trybie rzeczywistym.

%prep
%setup -q
cp %{SOURCE1} .

%build
%configure \
	--enable-cgidir=%{_cgidir} \
	--enable-language=Polish \
	--enable-logo=pldlogo.png \
	--enable-smbpasswd=%{_sysconfdir}/smbpasswd \
	--enable-squidpasswd=%{_sysconfdir}/squid/passwd \
%if %{without samba}
	--disable-smbpasswd \
%endif
%if %{without squid}
	--disable-squidpasswd
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_cgidir}
install -d $RPM_BUILD_ROOT/home/services/httpd/html

install changepassword.cgi $RPM_BUILD_ROOT%{_cgidir}
install %{SOURCE1} $RPM_BUILD_ROOT/home/services/httpd/html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGELOG README TODO
%lang(pt_BR) %doc README.brazilian
%attr(755,root,root) %{_cgidir}/changepassword.cgi
%attr(644,root,root) /home/services/httpd/html/pldlogo.png
