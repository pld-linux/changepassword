Summary:	ChangePassword
Summary(pl):	ChangePassword - modyfikator hase³
Name:		changepassword
Version:	0.5
Release:	1
License:	GPL
Group:		Networking/Admin
Source0:	http://dl.sourceforge.net/changepassword/%{name}-%{version}.tar.gz
# Source0-md5:	c730d9878f65ada0b81e16e4150cb6a7
URL:		http://changepassword.sourceforge.net/
Requires:	apache
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _cgidir         /home/services/httpd/html/cgi-bin

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
	--enable-cgidir=/home/services/httpd/html/cgi-bin \
	--enable-language=Polish \
	--enable-smbpasswd=%{_sysconfdir}/smbpasswd \
	--enable-squidpasswd=%{_sysconfdir}/squid/passwd

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_cgidir}

install changepassword.cgi     $RPM_BUILD_ROOT%{_cgidir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,CHANGELOG,LICENSE,BUGS,TODO}
%attr(755,root,root) %{_cgidir}/changepassword.cgi
