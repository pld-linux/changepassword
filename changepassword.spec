#TODO
# - move cgi binary to /usr/share/changepassword
# - write changepassword.conf for apache redirection + execution
# - get sources for libdes and compile then instead of using
#   precompiled version for x86!!!
Summary:	ChangePassword
Summary(pl):	ChangePassword - modyfikator hase³
Name:		changepassword
Version:	0.7
Release:	2
License:	GPL
Group:		Networking/Admin
Source0:	http://dl.sourceforge.net/changepassword/%{name}-%{version}.tar.gz
# Source0-md5:	b68a179e64dcffbfc4e410a84b6d3ecb
URL:		http://changepassword.sourceforge.net/
Requires:	apache
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _cgidir         /srv/httpd/cgi-bin

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

%build
%configure \
	--enable-cgidir=%{_cgidir} \
	--enable-language=Polish \
	--enable-smbpasswd=%{_sysconfdir}/smbpasswd \
	--enable-squidpasswd=%{_sysconfdir}/squid/passwd

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_cgidir}

install changepassword.cgi $RPM_BUILD_ROOT%{_cgidir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGELOG README TODO
%lang(pt_BR) README.brazilian
%attr(755,root,root) %{_cgidir}/changepassword.cgi
