# TODO
# - webapps
# - move cgi binary to /usr/lib/changepassword
# - write changepassword.conf for apache redirection + execution
#
# Conditional build:
%bcond_without	samba	# without samba passwords support
%bcond_without	squid	# without squid passwords support
#
Summary:	ChangePassword
Summary(pl.UTF-8):	ChangePassword - modyfikator haseł
Name:		changepassword
Version:	0.9
Release:	4
License:	GPL
Group:		Networking/Admin
Source0:	http://dl.sourceforge.net/changepassword/%{name}-%{version}.tar.gz
# Source0-md5:	7449a80c65db2e37c0aa3bb709926127
Source1:	pldlogo.png
Patch0:         build.patch
URL:		http://changepassword.sourceforge.net/
Requires:	webserver = apache
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_cgidir		/home/services/httpd/cgi-bin

%description
ChangePassword modifies the passwords of passwd, Samba, and Squid
through the Web. All passwords are syncronized and changed in real
time through browsers like Mozilla, Netscape, IE, Opera, and others.

%description -l pl.UTF-8
ChangePassword modyfikuje hasła dla passwd, Samby i Squida za
pośrednictwem interfejsu WWW. Wszystkie hasła są synchronizowane i
zmieniane w trybie rzeczywistym.

%prep
%setup -q
cp %{SOURCE1} .
tar -xf smbencrypt/libdes-4.04b.tar.gz
%patch0 -p1

%build
%configure \
	--enable-cgidir=%{_cgidir} \
	--enable-language=Polish \
	--enable-logo=pldlogo.png \
	--enable-smbpasswd=/etc/samba/smbpasswd \
	--enable-squidpasswd=/etc/squid/passwd \
%if %{without samba}
	--disable-smbpasswd \
%endif
%if %{without squid}
	--disable-squidpasswd
%endif

%{__make} -C des \
	CC="%{__cc}" \
%ifarch %{ix86}
	DES_INC="asm/dx86-elf.o asm/yx86-elf.o" \
	CFLAG="%{rpmcflags} -DELF"
%else
	CFLAG="%{rpmcflags}"
%endif
install des/libdes.a smbencrypt

%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

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
/home/services/httpd/html/pldlogo.png
